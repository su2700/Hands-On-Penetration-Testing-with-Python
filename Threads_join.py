#!/usr/bin/env python3
"""
🤝 Thread Joining
Demonstrates waiting for threads to finish (Joining).
"We finish together!" 🏃‍♂️🏃‍♀️
"""

import threading
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

class TaskRunner:
    def execute(self):
        t = threading.currentThread()
        logging.debug("✅ Started")
        time.sleep(2)
        logging.debug("🏁 Finished")

class ThreadManager:
    def __init__(self):
        self.counter = 0
        self.max_threads = 6
        self.active_limit = 3 # Only run 3 at a time

    def start_workflow(self):
        runner = TaskRunner()
        my_threads = []
        
        logging.debug("🚀 Workflow Started. Aiming to run %d threads total.", self.max_threads)

        while True:
            # Check active threads (excluding MainThread)
            current_active = threading.active_count() - 1 
            
            if current_active < self.active_limit and self.counter < self.max_threads:
                # 🆕 Spawn new thread
                t_name = "Worker-" + str(self.counter)
                t = threading.Thread(name=t_name, target=runner.execute)
                my_threads.append(t)
                t.start()
                self.counter += 1
                logging.debug("➕ Spawned %s (Total spawned: %d)", t_name, self.counter)
            
            # Exit loop if we launched everything
            if self.counter >= self.max_threads:
                logging.debug("🛑 All threads launched. Waiting for completion...")
                break
                
            time.sleep(0.5) # Breath

        # 🤝 Join all threads (Wait for them)
        for t in my_threads:
            if t.is_alive():
                logging.debug("⏳ Waiting for %s...", t.name)
                t.join()
                logging.debug("👋 %s joined.", t.name)
        
        print("\n🎉 Exiting Main. All work done!")

if __name__ == "__main__":
    manager = ThreadManager()
    manager.start_workflow()
