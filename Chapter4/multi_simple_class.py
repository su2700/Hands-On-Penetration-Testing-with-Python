#!/usr/bin/env python3
"""
🐣 Process Basics
Two ways to make a process:
1. Functional Way (Easy & Quick) 🏃
2. Class Way (Organized & Powerful) 🏛️
"""

import multiprocessing as mp
import time

# --- Way 1: The Function ---
def functional_worker(worker_id):
    """Just a simple function doing work."""
    print(f"   🏃 Function Worker {worker_id}: Running!")

# --- Way 2: The Class ---
class ClassWorker(mp.Process):
    """A dedicated worker class."""
    def __init__(self, name):
        super().__init__() # Init parent
        self.name = name
        
    def run(self):
        """This method runs when you call .start()"""
        print(f"   🏛️  Class Worker '{self.name}': Initialized & Running!")

if __name__ == "__main__":
    print("\n--- 1️⃣ Functional Approach ---")
    procs = []
    for i in range(3):
        p = mp.Process(target=functional_worker, args=(i,))
        procs.append(p)
        p.start()
    
    # Wait for them
    for p in procs:
        p.join()

    print("\n--- 2️⃣ Class Approach ---")
    obj = ClassWorker("Robo-1")
    obj.start()
    obj.join()

    print("\n✅ All Done!")
