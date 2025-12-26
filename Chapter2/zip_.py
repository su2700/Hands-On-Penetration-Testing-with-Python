#!/usr/bin/env python3
"""
🤐 Zip Function
Zips two lists together like a jacket! 🧥
"""

list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]

# 🤐 Zipping
zipped = list(zip(list_a, list_b))
print(f"🤐 Zipped Lists: {zipped}")

# ➕ Adding elements from both lists
# Loop way
sum_loop = [x + y for x, y in zipped]
print(f"➕ Sum (Loop): {sum_loop}")

# Map way (One shot!)
# We use lambda to take a tuple 'x' and add x[0] + x[1]
sum_map = list(map(lambda pair: pair[0] + pair[1], zip(list_a, list_b)))
print(f"⚡ Sum (Map):  {sum_map}")

# List Comp way (One shot)
sum_comp = [x + y for x, y in zip(list_a, list_b)]
print(f"🚀 Sum (Comp): {sum_comp}")
