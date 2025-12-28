#!/usr/bin/env python3
"""
👔 The Process Manager
Spawning workers, checking on them, and knowing when to let them go.
It's like being a boss! 💼
"""

import multiprocessing as mp
import time
import logging

# 📝 Setup Logging (So we can see what's happening!)
logging.basicConfig(
    level=logging.DEBUG,
    format='(%(processName)-10s) 👉 %(message)s',
)

class WorkerBot:
    """I am a simple bot. I do work and then I sleep. 🤖"""
    
    def do_work(self, worker_id):
        """Simulates doing a task."""
        # 💤 Sleeping to pretend we are busy
        time.sleep(1)
        logging.debug(f"✅ Finished Task ID: {worker_id}")

def main():
    print("\n--- 🏭 Factory Opening ---")
    
    bot = WorkerBot()
    process_list = []
    
    # 1️⃣ HIRE WORKERS (Spawn Processes)
    print("👷 Hiring 10 workers...")
    for i in range(10):
        # We create a Process object
        p = mp.Process(name=f"Worker_{i}", target=bot.do_work, args=(i,))
        process_list.append(p)
        p.start() # 🚀 Go!
    
    current_process = mp.current_process()
    print(f"🕴️  Main Boss: {current_process.name}")
    
    # 2️⃣ MONITOR WORKERS (Join or Terminate)
    print("\n⏳ Boss is waiting for 3 seconds...")
    
    # We will be patient effectively for the first few, then impatient!
    patience_limit = 1
    patience_counter = 0

    for p in process_list:
        if p.is_alive():
            if patience_counter < patience_limit:
                # 🤝 JOIN: Wait nicely for the process to finish
                logging.debug(f"🤝 Waiting nicely for {p.name}...")
                p.join(timeout=3)
                patience_counter += 1
            else:
                # ☠️ TERMINATE: You're taking too long! Fired!
                if p.is_alive():
                    logging.debug(f"😤 You're too slow, {p.name}! -- TERMINATING ☠️")
                    p.terminate()
                    p.join() # Clean up the zombie process
    
    print("\n--- 🏭 Factory Closing ---")

if __name__ == "__main__":
    main()
