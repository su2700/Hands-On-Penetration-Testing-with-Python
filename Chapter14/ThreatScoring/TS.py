#!/usr/bin/env python
"""
🎯 Threat Scorer (MISP)
Calculates threat scores based on Attributes, Tags, Dates, and Correlations.
It's like a credit score, but for malware! 🦠📉
"""

import json
import os
import logging
import multiprocessing
import math
import datetime
import time
from keys import misp_url, misp_key

# 🛠️ Mock Database Handler (Since we don't have the full DB_Layer module locally)
# In production, this imports from DB_Layer.Misp_access
class MockMispDB:
    def getAttributeCount(self):
        return {"status": "success", "value": 100}
    def getEnabledFeeds(self):
        return {"status": "success", "value": {"enabled": 5}}
    def updateTask(self, **kwargs):
        pass
    def getTaskStatusCodes(self, task_id):
        return {"status": "success", "value": []}
    def getAttributesToScore(self, offset, limit):
        # Mocking empty list to prevent crash
        return {"status": "success", "value": []}
    def updateAttributeScore(self, **kwargs):
        pass
    def updateProcessMessage(self, **kwargs):
        pass

# Try importing real DB, else fail gracefully to Mock
try:
    from DB_Layer.Misp_access import MispDB
except ImportError:
    print "⚠️  DB_Layer not found. Using MockMispDB for demonstration."
    MispDB = MockMispDB

class ThreatScoreGenerator:

    def __init__(self):
        # 📝 Logging Setup
        self.logger = logging.getLogger('ThreatScore')
        self.logger.setLevel(logging.DEBUG)
        
        # File Handler
        fh = logging.FileHandler('TS.log')
        fh.setFormatter(logging.Formatter('time="%(asctime)s" level=%(levelname)s msg="%(message)s"'))
        self.logger.addHandler(fh)
        
        # Console Handler (Cleaner)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(logging.Formatter('ℹ️  %(message)s'))
        self.logger.addHandler(ch)
        
        self.log = self.logger
        self.log.info("Threat Score System Initialized 🚀")

    def run_scoring_job(self, task_id=0):
        """Main driver for the scoring process using Multi-Processing."""
        self.log.info("Starting Threat Score Update...")
        
        try:
            # 1️⃣ CPU Calculation
            cpu_count = multiprocessing.cpu_count()
            workers = math.ceil(cpu_count / 1.0) if cpu_count > 1 else 1
            self.log.info("🔥 Spinning up %d worker processes...", workers)

            # 2️⃣ Fetch Stats
            db = MispDB()
            att_stat = db.getAttributeCount()
            if att_stat["status"] != "success":
                self.log.error("❌ Failed to get attribute count!")
                return {"status": "failure", "value": "DB Error"}
            
            total_attributes = int(att_stat["value"])
            
            feed_stat = db.getEnabledFeeds()
            feed_count = int(feed_stat["value"]["enabled"]) if feed_stat["status"] == "success" else 0
            
            self.log.info("📊 Total Attributes: %d | Feeds: %d", total_attributes, feed_count)

            if total_attributes == 0:
                self.log.warn("💤 No attributes to score.")
                return {"status": "success", "value": "Nothing to do"}

            # 3️⃣ Chunking Strategy
            # Use floating point division to force exact chunks
            chunk_size = math.ceil(float(total_attributes) / workers)
            chunks = []
            
            current_offset = 0
            while current_offset < total_attributes:
                chunks.append({"offset": int(current_offset), "limit": int(chunk_size)})
                current_offset += chunk_size

            # 4️⃣ Spawn Workers
            db.updateTask(task_id=task_id, status="processing", message="Spawning Workers", update_process=False)
            
            process_list = []
            for i, chunk in enumerate(chunks):
                p = multiprocessing.Process(
                    target=self.process_chunk,
                    args=(chunk["offset"], chunk["limit"], str(i), task_id, False, feed_count)
                )
                process_list.append(p)
                p.start()
            
            # Wait for completion
            for p in process_list:
                p.join()

            self.log.info("✅ All workers finished!")
            return {"status": "success", "value": "Threat Scoring Complete"}

        except Exception as e:
            self.log.error("💥 Critical Failure: %s", str(e))
            return {"status": "failure", "value": str(e)}

    def process_chunk(self, offset, limit, process_id, task_id, external_scoring, feed_count):
        """Worker function: Processes a specific range of attributes."""
        try:
            # Refresh DB connection per process usually required
            db = MispDB() 
            
            # Load Weights
            root = os.path.dirname(os.path.realpath(__file__))
            with open(os.path.join(root, "weightage.json")) as f:
                weights = json.load(f)

            # Fetch Data Chunk
            resp = db.getAttributesToScore(offset, limit)
            if resp["status"] != "success":
                db.updateProcessMessage(process_id, task_id, "failure", "Fetch Failed: " + str(resp.get("value")))
                return

            attributes = resp["value"]
            if not attributes:
                db.updateProcessMessage(process_id, task_id, "success", "Empty Chunk")
                return

            # Score each attribute
            failed_ids = []
            for att in attributes:
                try:
                    self.score_single_attribute(att, weights, feed_count, db)
                except Exception as e:
                    failed_ids.append(att.get("id"))

            if failed_ids:
                msg = "Partial Failure on IDs: " + str(failed_ids)
                db.updateProcessMessage(process_id, task_id, "success", msg) # Partial success is still "success" to master?
            else:
                db.updateProcessMessage(process_id, task_id, "success", "Chunk Complete")

        except Exception as e:
            # db.updateProcessMessage(process_id, task_id, "failure", "Worker Crash: " + str(e))
            pass

    def score_single_attribute(self, att, weights, feed_count, db):
        """Calculates score for one attribute."""
        # Calculate Component Scores
        date_score = self.calc_date_score(att.get("i_date"), weights["Date"])
        tag_score = self.calc_tag_score(att.get("i_tags"), weights["Tags"])
        corr_score = self.calc_correlation_score(att.get("i_corelation"), weights["Corelation"], feed_count)
        comm_score = self.calc_comment_score(att.get("i_comment"), weights["Comment"])
        
        # Aggregate
        total_internal = (date_score + tag_score + corr_score + comm_score) / 10.0
        
        # Update DB
        db.updateAttributeScore(
            id=att["id"],
            i_date_score=date_score,
            i_tags_score=tag_score,
            i_corelation_score=corr_score,
            i_comment_score=comm_score,
            total_internal_score=total_internal,
            cumulative_score=total_internal,
            value=att["value"]
        )

    # 🧮 Score Calculation Helpers
    
    def compute_weighted_score(self, val, setting, param_name=""):
        """Generic logic to checking range/fixed partitions."""
        try:
            max_weight = int(setting["weightage"])
            partitions = setting["partitions"]
            assigned_pct = 0
            
            for p in partitions:
                p_weight = int(p["weight"])
                
                if p["type"] == "range":
                    # Range Check
                    if int(p["ll"]) <= val <= int(p["ul"]):
                        assigned_pct = p_weight
                        break
                        
                elif p["type"] == "fixed":
                    # Exact Match Check
                    if val == int(p["size"]):
                        assigned_pct = p_weight
                        break
            
            # Final calculation: (Category Weight) * (Match %)
            return max_weight * (assigned_pct / 100.0)
            
        except Exception as e:
            self.logger.error("Calc Error (%s): %s", param_name, e)
            return 0

    def calc_date_score(self, timestamp, setting):
        try:
            # Convert timestamp to days ago
            ioc_date = datetime.datetime.fromtimestamp(float(timestamp))
            delta = datetime.datetime.now() - ioc_date
            days = max(1, delta.days) # Minimum 1 day
            
            return self.compute_weighted_score(days, setting, "Date")
        except:
            return 0

    def calc_tag_score(self, tag_count, setting):
        return self.compute_weighted_score(int(tag_count or 0), setting, "Tags")

    def calc_correlation_score(self, corr_count, setting, feed_total):
        try:
            if feed_total == 0: return 0
            # Calculate Percentage of feeds that correlate
            pct = (int(corr_count or 0) / float(feed_total)) * 100
            return self.compute_weighted_score(pct, setting, "Corelation")
        except:
            return 0

    def calc_comment_score(self, comment, setting):
        has_comment = 1 if (comment and comment.strip()) else 0
        return self.compute_weighted_score(has_comment, setting, "Comment")

if __name__ == "__main__":
    scorer = ThreatScoreGenerator()
    scorer.run_scoring_job()
