#!/usr/bin/env python3
"""
🐑 Lambda & Map
Lambda: A tiny, anonymous function. 🤏
Map: Applying that tiny function to a whole list. 🗺️
"""

numbers = [1, 2, 3, 4]

# 📝 The Logic: lambda x: x**2 (Take x, return x squared)
# 🗺️ The Map: Apply logic to 'numbers'
sq_list = list(map(lambda x: x**2, numbers))

print(f"📋 Original: {numbers}")
print(f"✨ Squared:  {sq_list}")
