#!/usr/bin/env python3
"""
🧩 Methods Advanced (Args & Kwargs)
Handling ANY number of inputs! Like a magic bag! 🎒
"""

# *args = List of arguments (Tuple)
def method_args(*args):
    print("\n📦 --- *ARGS (Tuple) ---")
    print(f"   Received: {args}")
    
    total = sum(args)  # Python includes a handy sum() function!
    print(f"   Total Sum: {total}")

# **kwargs = Dictionary of arguments
def method_kwargs(**kwargs):
    print("\n🔑 --- **KWARGS (Dictionary) ---")
    print(f"   Received: {kwargs}")
    
    for k, v in kwargs.items():
        print(f"   Key: {k} -> Value: {v}")

# Unpacking Examples
def unpack_demo():
    print("💥 Unpacking Demo!")
    
    # 1. Unpacking a List with *
    my_list = [1, 2, 3, 4, 5, 8]
    method_args(*my_list)
    
    # 2. Unpacking a Dict with **
    my_dict = {"k1": 22, "k2": 33}
    method_kwargs(**my_dict)

if __name__ == "__main__":
    unpack_demo()
