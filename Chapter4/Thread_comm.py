#!/usr/bin/env python3
"""
🏃💨 The Relay Race (Thread Communication)
Threads talking to each other using 'Events'. 🚦
One thread runs, signals "READY!", and the other reacts.
"""

import threading
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) 👉 %(message)s',
)

class BatonPass:
    def __init__(self):
        self.counter = 0
        
    def runner_waiter(self, event):
        """
        I wait for the signal to sprint! 🏃
        """
        logging.debug("💤 Waiting for the signal (Event)...")
        
        # This blocks untill event.set() is called
        event.wait()
        
        logging.debug(f"⚡ SIGNAL RECEIVED! Counter reached target: {self.counter}")
        logging.debug("🏁 I finished my part!")

    def runner_starter(self, event, target_val=5):
        """
        I run the first leg of the race. 👟
        """
        while self.counter < 10:
            logging.debug(f"🏃 Running... Step {self.counter}")
            
            # Simulate effort
            time.sleep(0.5)
            self.counter += 1
            
            # Check if we should signal
            if self.counter == target_val:
                logging.debug("🚨 REACHED TARGET! Signaling Event!")
                event.set() # Wake up the other thread!

if __name__ == "__main__":
    print("\n--- 🏁 Relay Race Start ---")
    
    race = BatonPass()
    
    # 🚦 The Event Object (Flag)
    start_signal = threading.Event()
    
    # Create Threads
    t_waiter = threading.Thread(name="Waiter", target=race.runner_waiter, args=(start_signal,))
    t_starter = threading.Thread(name="Starter", target=race.runner_starter, args=(start_signal, 5))
    
    t_waiter.start()
    t_starter.start()
    
    t_waiter.join()
    t_starter.join()
    
    print("\n✅ Race Complete!")
