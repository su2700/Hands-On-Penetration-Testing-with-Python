#!/usr/bin/env python
"""
🔒 HSTS Detector
Checks if Strict-Transport-Security is enabled.
(Forces browsers to use HTTPS only!) 🛡️
"""

import requests

class HSTSDetector:
    def __init__(self, target):
        self.target = target
        print "\n🛡️ HSTS Detector Initialized!"
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

            # 🧐 Check for HSTS
            if "Strict-Transport-Security" in headers:
                print "\n   ✅ SAFE: 'Strict-Transport-Security' header is present."
                print "      Value: " + headers["Strict-Transport-Security"]
            else:
                print "\n   ⚠️ VULNERABLE: 'Strict-Transport-Security' header is MISSING!"
                print "      (This site does not enforce HTTPS via HSTS!)"

        except Exception as ex:
            print "   ❌ Exception: " + str(ex)

if __name__ == "__main__":
    # DVWA Example URL
    target_url = "http://192.168.250.1/dvwa" 
    detector = HSTSDetector(target_url)
    detector.start_scan()
