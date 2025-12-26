#!/usr/bin/env python3
"""
🔄 For Loops - Basics
Looping is doing the same thing over and over... but fast! 🏎️
"""

# 1️⃣ Standard Loop (0 to 4)
print("\n👉 Loop 1: Default range (0 to 4)")
for i in range(5):
    print(f"   Step {i}")

# 2️⃣ Range with Start and End (5 to 9)
print("\n👉 Loop 2: Start at 5, Stop before 10")
for i in range(5, 10):
    print(f"   Step {i}")

# 3️⃣ Range with Start, End, and Step (Skipping numbers)
print("\n👉 Loop 3: Start at 1, Stop before 10, Jump by 2")
step_size = 2
for i in range(1, 10, step_size):
    print(f"   Step {i} (Jumped by {step_size})")

print("\n🏁 Loops finished!")
