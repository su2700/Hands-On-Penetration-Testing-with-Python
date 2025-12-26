#!/usr/bin/env python3
"""
⚡ Generators
Generators are lazy... in a good way! 🛌
They give you one value at a time instead of everything at once.
This saves memory! 🧠
"""

def gen_method():
    """
    A simple generator function.
    Notice the 'yield' keyword instead of 'return'.
    """
    a = 100
    for i in range(3):
        print(f"   [Inside Gen] 'a' is {a}, getting ready to yield...")
        a = a + 1
        yield a  # ⏸️ PAUSE HERE and give value
        print(f"   [Inside Gen] Resumed! 'a' is now {a}")

def driver_loop():
    """
    Drives the generator using a loop.
    """
    print("🚗 Starting Loop Driver...")
    for value in gen_method():
        print(f"👉 Received value: {value}")
        print("   --------------")

def driver_manual():
    """
    Drives the generator manually using next().
    """
    print("\n🚜 Starting Manual Driver...")
    v = gen_method()
    
    print("1️⃣ Calling next()...")
    print(f"   Got: {next(v)}")
    
    print("2️⃣ Calling next()...")
    print(f"   Got: {next(v)}")
    
    print("3️⃣ Calling next()...")
    print(f"   Got: {next(v)}")

# Uncomment the one you want to run!
# driver_manual() 
driver_loop()
print("\n🏁 Generator demo finished!")
