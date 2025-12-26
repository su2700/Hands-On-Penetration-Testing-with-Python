#!/usr/bin/env python3
"""
🧹 Filter Usage
Showcasing how to 'filter' out unwanted items from a list.
It's like panning for gold! 🌟
"""

# The raw list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# 🔍 The Filter
# We use a 'lambda' (anonymous function) to check if a number is even.
# lambda x : x % 2 == 0  --> Returns True if Even, False if Odd.
even_filter = filter(lambda x: x % 2 == 0, numbers)

# 📦 The Result (It's an iterator first!)
print(f"📦 Filter Object: {even_filter}")

# 📝 Convert to List to see contents
even_list = list(even_filter)
print(f"✨ Filtered List (Evens): {even_list}")
