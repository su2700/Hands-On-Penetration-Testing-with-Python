#!/usr/bin/env python3
"""
🗺️ Map Usage
Mapping is like applying a sticker to every item in the list! 🏷️
"""

def square(num):
    """Returns the square of a number."""
    return num ** 2

my_list = [1, 2, 3, 4]

# Using map() apply 'square' to everything in 'my_list'
# map() returns an iterator, so we cast it to list() to see it.
sq_map = list(map(square, my_list))

print(f"📋 Original: {my_list}")
print(f"✨ Mapped:   {sq_map}")
