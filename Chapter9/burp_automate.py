#!/usr/bin/env python2
"""
🍩 Burp Suite Automator
Automates security scans using the Burp Suite REST API. 🤖
It's like having a robot drive your Burp Suite! 🚗💨
"""

import requests
import json
from urlparse import urljoin # Python 2
import socket
import time
import sys

class BurpBot:
    def __init__(self):
        # 🔑 Configuration
        self.api_key = "odTOmUX9mNTV3KRQ4La4J1pov6PEES72"
        self.api_url = "http://127.0.0.1:1337"
        print "\n🤖 BurpBot Initialized!"
        print "   🔑 API Key: " + self.api_key
        print "   🔗 Target API: " + self.api_url

    def start_scan(self):
        """Initiates the scan via API."""
        print "\n🚀 Starting Scan Sequence..."
        
        try:
            # 📝 Scan Configuration (JSON)
            scan_config = {
                "application_logins": [
                    {"username": "admin", "password": "password"}
                ],
                "scan_callback": {
                    "url": "http://127.0.0.1:8001" # Our listener!
                },
                "scope": {
                    "exclude": [{"rule": "http://192.168.250.1/dvwa/logout.php", "type": "SimpleScopeDef"}],
                    "include": [{"rule": "http://192.168.250.1/dvwa/", "type": "SimpleScopeDef"}]
                },
                "urls": ["http://192.168.250.1/dvwa/"]
            }

            # 🛠️ Construct URL
            # API URL structure: http://host:port/API_KEY/v0.1/scan
            full_url = urljoin(self.api_url, self.api_key) + "/v0.1/scan"
            
            print "   📡 Sending Scan Request to: " + full_url
            
            # 📨 Send Request
            resp = requests.post(full_url, json=scan_config)
            
            if resp.status_code == 201:
                print "   ✅ Scan request accepted!"
                self.listen_for_callback()
            else:
                print "   ❌ Start Failed! Status: " + str(resp.status_code)
                print "   ⚠️ Response: " + resp.text

        except Exception as ex:
            print "   💥 Exception in Start: " + str(ex)

    def listen_for_callback(self):
        """Listens for the Burp Suite callback to get the Task ID."""
        print "\n👂 Listening for Callback on port 8001..."
        
        try:
            # 1️⃣ Setup Socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(('127.0.0.1', 8001))
            s.listen(1) # Listen for 1 connection
            
            # 2️⃣ Wait for connection
            print "   ⏳ Waiting for Burp to call home..."
            conn, addr = s.accept()
            
            if conn:
                print "   📞 Connection received from " + str(addr)
                
                # 3️⃣ Read Data
                data = conn.recv(2048)
                if data:
                    print "   📨 Received Data payload."
                    # Parse Task ID manually from the raw HTTP/JSON dump
                    # Expecting something like ... "task_id": "123" ...
                    
                    try:
                        # Find "task_id" in string
                        idx = str(data).find("task_id")
                        if idx != -1:
                            # Extract roughly the number area
                            # This is a bit hacky but keeps the original logic intact
                            snippet = str(data)[idx:idx+25] 
                            # Clean it up to find the number
                            # Example snippet: task_id":"11"
                            clean_id = ''.join(filter(str.isdigit, snippet))
                            
                            task_id = int(clean_id)
                            print "   🆔 Task ID Found: " + str(task_id)
                            
                            conn.close()
                            s.close()
                            
                            # 🚀 Switch to Polling Mode
                            self.poll_results(task_id)
                            return
                            
                    except Exception as e:
                        print "   ❌ Error parsing ID: " + str(e)
                
                conn.close()
            s.close()
            
        except Exception as ex:
            print "   💥 Callback Exception: " + str(ex)

    def poll_results(self, task_id):
        """Polls the API for scan results."""
        print "\n🦅 Polling for Results (Task " + str(task_id) + ")..."
        
        try:
            while True:
                time.sleep(5) # Wait a bit 💤
                
                # 🛠️ Construct URL
                full_url = urljoin(self.api_url, self.api_key) + "/v0.1/scan/" + str(task_id)
                
                resp = requests.get(full_url)
                data = resp.json()
                
                status = data.get("scan_status", "unknown")
                print "   🔄 Status: " + status
                
                # 🧐 Check for Issues
                issue_events = data.get("issue_events", [])
                for idx, event in enumerate(issue_events):
                    issue = event.get("issue", {})
                    severity = issue.get("severity", "Info")
                    
                    if severity != "info" and severity != "Info":
                        print "\n   " + "!"*30
                        print "   🔥 ISSUE FOUND! 🔥"
                        print "      Severity:    " + severity
                        print "      Name:        " + issue.get("name", "Unknown")
                        print "      Path:        " + issue.get("path", "Unknown")
                        print "      Description: " + issue.get("description", "")[:50] + "..." # Truncate
                        
                if status == "succeeded" or status == "failed":
                    print "\n✅ Scan Finished with status: " + status
                    break
                    
        except Exception as ex:
            print "   💥 Polling Exception: " + str(ex)

if __name__ == "__main__":
    bot = BurpBot()
    bot.start_scan()
