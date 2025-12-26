#!/usr/bin/env python3
"""
🔄 Advanced For Loops
Looping over different data types! 📦
"""

# 🧵 Iterate over Strings
print("\n🔤 --- Strings ---")
my_string = "Hello"
for char in my_string:
    print(f"  '{char}'")

# 📋 Iterate over Lists
print("\n📜 --- Lists ---")
my_list = [1, 2, 3, 4, 5, 6]
for item in my_list:
    print(f"  Item: {item}")

# 🔢 Iterate over Lists (with Index)
print("\n📍 --- Lists with Index (enumerate) ---")
for index, value in enumerate(my_list):
    print(f"  Index: {index} -> Value: {value}")

# 🔑 Iterate over Dictionary Keys
print("\n🔑 --- Dictionary Keys ---")
my_dict = {"k1": "v1", "k2": "v2", "k3": "v3"}
for key in my_dict:
    print(f"  Key: {key} -> Value: {my_dict[key]}")

# 🗝️ Iterate over Dictionary Items (Key & Value)
print("\n🗝️ --- Dictionary .items() ---")
for key, value in my_dict.items():
    print(f"  Key: {key} -> Value: {value}")

# 📦 Iterate over Tuples
print("\n📦 --- Tuples ---")
my_tuple = (1, 2, 3, 4, 5)
for value in my_tuple:
    print(f"  Value: {value}")

# 🧩 Iterate over Sets
print("\n🧩 --- Sets (Unique items only!) ---")
my_set = {2, 2, 3, 3, 5, 5}
for value in my_set:
    print(f"  Value: {value}")

print("\n🏁 All loops done!")
