#!/usr/bin/env python3
"""
🧱 Method Basics
Building blocks of Python! 🏗️
"""

def print_simple():
    print("📢 Simple Message!")

def print_custom(message):
    print(f"📢 Custom: {message}")

def print_result(message, do_return):
    print(f"📢 Result: {message}")
    if do_return:
        return "✅ Returned Success"
    return "❌ Returned Nothing"

def print_options(main, op1="Default1", op2=False):
    print("\n--- ⚙️ Options ---")
    print(f"   Main: {main}")
    print(f"   Op1:  {op1}")
    print(f"   Op2:  {op2}")

def math_magic(a, b, c):
    # Returning multiple values creates a Tuple!
    return a*2, b*2, c*2

if __name__ == "__main__":
    print_simple()
    print_custom("Hello User!")
    
    print("\n--- 🔄 Return Values ---")
    res = print_result("Please return!", True)
    print(f"   Got: {res}")
    
    print_options("MandatoryOnly")
    print_options("Overriding", op1="Custom!", op2=True)
    
    print("\n--- 🔢 Multiple Returns ---")
    vals = math_magic(1, 2, 3)
    print(f"   Output: {vals} (Type: {type(vals)})")
