#!/usr/bin/env python3
"""
👻 Process Daemons
Demonstrates creating a Daemon process (background ghost). 👻
Daemon processes die when the main program exits!
"""

import multiprocessing as mp
import time
import logging

# 📝 Logging Setup
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - (%(processName)-10s) %(message)s'
)

class GhostProcess:
    def work(self, label):
        logging.debug("👻 Enter: %s", label)
        time.sleep(4)
        logging.debug("👻 Exit:  %s", label)

if __name__ == "__main__":
    ghost = GhostProcess()
    
    # 🧟 Spawning a Daemon Process
    p = mp.Process(name="GhostDaemon", target=ghost.work, args=("Haunting...",))
    p.daemon = True # This makes it a daemon
    
    logging.debug("🚀 Main Program Started")
    p.start()
    
    # Optional: Wait a bit to see the daemon work, or exit immediately to see it die
    time.sleep(1) 
    logging.debug("🏁 Main Program Ended (Daemon should die now)")
