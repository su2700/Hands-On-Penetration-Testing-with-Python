#!/usr/bin/env python3
"""
🧵 Daemon Threads
Demonstrates a background thread that gets killed when main exits. 💀
"""

import threading
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

class Worker:
    def execute(self, task_name):
        logging.debug("🧵 Starting Task: %s", task_name)
        time.sleep(4)
        logging.debug("🧵 Finished Task: %s", task_name)

if __name__ == "__main__":
    worker = Worker()
    
    # 👹 Daemon Thread
    t = threading.Thread(name="DaemonThread", target=worker.execute, args=("Background Job",))
    t.setDaemon(True) # Legacy method, modern is 'daemon=True' in constructor
    
    logging.debug("🚀 Main Thread Started")
    t.start()
    
    # time.sleep(1) # Uncomment to let daemon finish
    logging.debug("🏁 Main Thread Ended (Daemon dies now!)")
