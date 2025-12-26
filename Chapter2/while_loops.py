#!/usr/bin/env python3
"""
⏳ While Loops
Keep doing it until I say STOP! 🛑
"""

# 1️⃣ Basic While
print("\n--- ⏳ Basic While Loop ---")
i = 0
while i < 3:
    print(f"   Count: {i}")
    i += 1

# 2️⃣ While over a List (Polymorphism intro!)
print("\n--- 🔄 Mixed List Iteration ---")
my_list = [1, "Hello", [10, 20], 33.33]

idx = 0
while idx < len(my_list):
    item = my_list[idx]
    
    # Check Type
    if isinstance(item, int):
        print(f"🔢 Integer found: {item}")
    elif isinstance(item, str):
        print(f"🔤 String found: {item}")
    elif isinstance(item, list):
        print("📦 Inner List found! Unpacking...")
        j = 0
        while j < len(item):
            print(f"   👉 Inner Item: {item[j]}")
            j += 1
    else:
        print(f"❓ Other Type ({type(item)}): {item}")
    
    idx += 1

print("\n🏁 Loop finished!")
