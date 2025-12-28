#!/usr/bin/env python
"""
🖱️ Clickjacking Detector
Checks if a site allows itself to be framed (which is bad!). 🚫
"""

import requests

class ClickJackingDetector:
    def __init__(self, target):
        self.target = target
        print "\n🕵️ Clickjacking Detector Initialized!"
        print "   🎯 Target: " + self.target

    def start_scan(self):
        """Starts the detection logic."""
        try:
            print "   📡 Sending request..."
            resp = requests.get(self.target)
            headers = resp.headers
            
            print "\n   📋 === HTTP HEADERS === "
            for k, v in headers.iteritems():
                print "   🔹 " + k + ": " + v
            print "   ======================="

            # 🧐 Check for X-Frame-Options
            if "X-Frame-Options" in headers:
                print "\n   ✅ SAFE: 'X-Frame-Options' header is present."
                print "      Value: " + headers["X-Frame-Options"]
            else:
                print "\n   ⚠️ VULNERABLE: 'X-Frame-Options' header is MISSING!"
                print "      (This site might be vulnerable to Clickjacking!)"

        except Exception as ex:
            print "   ❌ Exception: " + str(ex)

if __name__ == "__main__":
    # DVWA Example URL
    target_url = "http://192.168.250.1/dvwa" 
    detector = ClickJackingDetector(target_url)
    detector.start_scan()
