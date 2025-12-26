#!/usr/bin/env python3
"""
👻 Abstract Classes
Think of an 'Abstract Class' as a BLUEPRINT 📐.
You can't live in a blueprint, but you use it to build actual houses (Subclasses)! 🏠
"""

from abc import ABC, abstractmethod

# 📐 The Blueprint
class QueueAbs(ABC):
    """
    I am just an idea of a Queue. You can't use me directly!
    """
    def __init__(self):
        self.buffer = []

    def print_items(self):
        """Prints all items currently in the buffer."""
        for item in self.buffer:
            print(f"   🔹 {item}")

    @abstractmethod
    def enqueue(self, item):
        """You MUST implement this to add items!"""
        pass

    @abstractmethod
    def dequeue(self):
        """You MUST implement this to remove items!"""
        pass

# 🏗️ The Real Construction
class Queue(QueueAbs):
    """
    I am a REAL Queue. I follow the blueprint!
    """

    def __init__(self, length):
        super().__init__() # Call parent's setup
        self.length = length

    def enqueue(self, item):
        # Check if full 🚫
        if self.length <= len(self.buffer):
            print("   ⚠️ Queue is full!")
            return
        
        self.buffer.append(item)
        print(f"   ✅ Added: {item}")

    def dequeue(self):
        # Check if empty 🕳️
        if len(self.buffer) == 0:
            print("   ⚠️ Empty Queue!")
            return 
        
        item = self.buffer[0]
        del self.buffer[0]
        return item

# 🚗 The Driver Code
class Driver():
    def main(self):
        print("\n--- 🏁 Starting Queue Demo ---")
        q = Queue(10)
        
        print("\n📥 Enqueuing items...")
        for item in range(0, 10):
            q.enqueue(item)
        
        print("\n📜 Current List:")
        q.print_items()
        
        print("\n📤 Dequeuing items...")
        for _ in range(0, 10):
            removed = q.dequeue()
            print(f"   👋 Removed: {removed}")
        
        print("\n🏁 Demo Complete!")

if __name__ == "__main__":
    d = Driver()
    d.main()
