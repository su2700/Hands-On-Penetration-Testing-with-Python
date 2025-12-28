#!/usr/bin/env python3
"""
🔒 Thread Locking
Imagine a bathroom with one key. 🔑
Only one thread can go in at a time. Everyone else must wait in line!
This prevents 'Race Conditions' (messing up data).
"""

import threading
import time
import logging

# 📝 Pretty Logging
logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) 🗣️ %(message)s',
)

class SafeCounter:
    def __init__(self):
        self.counter = 0
        # 🔑 The Magic Lock
        self.lock = threading.Lock()

    def dangerous_increment(self):
        """Increments without a lock (Chaos!)"""
        # Logic would go here
        pass

    def safe_increment(self):
        """Increments WITH a lock (Safe!)"""
        
        # 1️⃣ Acquire Lock (Grab the Key)
        # Using 'with' is cleaner than acquire() / release()
        logging.debug("⏳ Waiting for lock...")
        with self.lock:
            logging.debug("🔐 Lock Acquired! Incrementing...")
            
            # Critical Section (Do the important stuff)
            current_val = self.counter
            time.sleep(0.1) # Pretend this is hard work
            self.counter = current_val + 1
            
            logging.debug(f"📈 Counter is now: {self.counter}")
        
        # 2️⃣ Lock Released automatically here!
        logging.debug("🔓 Lock Released.")

    def worker_task(self):
        """What every thread does."""
        self.safe_increment()

    def run_demo(self, num_threads):
        print("\n--- 🧵 Starting Locking Demo ---")
        threads = []
        
        # Spawn Threads
        for i in range(num_threads):
            t = threading.Thread(name=f"Worker_{i}", target=self.worker_task)
            threads.append(t)
            t.start()
        
        # Wait for all to finish
        for t in threads:
            t.join()
            
        print("-" * 30)
        print(f"✅ Final Counter Value: {self.counter}")
        print("(It should match the number of threads!)")

if __name__ == "__main__":
    demo = SafeCounter()
    demo.run_demo(5)
