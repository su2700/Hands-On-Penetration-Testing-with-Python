#!/usr/bin/env python3
"""
⚡ List Comprehension Basics
Making lists fast! 🐆
"""

# The setup
my_list = [1, 2, 3, 4]
print(f"📋 Original: {my_list}")

# 1️⃣ The Fast Way (List Comprehension)
sq_list_fast = [x**2 for x in my_list]
print(f"🚀 Fast Squares: {sq_list_fast}")

# 2️⃣ The Old Way (Loop)
print("\n🐢 The Old Way...")
def square(num):
    return num ** 2

sq_list_slow = []
for num in my_list:
    sq_list_slow.append(square(num))

print(f"🐢 Slow Squares: {sq_list_slow}")
