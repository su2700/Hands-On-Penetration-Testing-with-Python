#!/usr/bin/env python3
"""
⌨️ User Input
Talking to the script! 🗣️
"""

def main():
    print("\n--- ➕ Adder Bot 3000 ---")
    
    # ⚠️ input() ALWAYS returns a String!
    str_1 = input("   👉 Enter First Number: ")
    str_2 = input("   👉 Enter Second Number: ")
    
    # String Concatenation 🧵
    str_sum = str_1 + str_2
    print(f"\n   🧵 String Concatenation: '{str_sum}' (Wait, that's not math!)")
    
    # Integer Addition 🧮
    try:
        real_sum = int(str_1) + int(str_2)
        print(f"   ✅ Real Math Sum:        {real_sum}")
    except ValueError:
        print("   ❌ Oops! Those weren't valid numbers.")

if __name__ == "__main__":
    main()
