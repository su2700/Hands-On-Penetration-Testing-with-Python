#!/usr/bin/env python3
"""
⚡ Generator Expressions
Like List Comprehensions, but lazier (memory efficient)! 😴
It doesn't create the list until you ask for it.
"""

def expression_demo():
    print("🚀 creating generator...")
    
    # Notice the parentheses () instead of brackets []
    # This creates a generator object, not a list!
    gen_obj = (x * x for x in range(3))
    
    print(f"   📦 Object: {gen_obj}")
    print("   (It hasn't calculated anything yet!)")
    
    print("\n🏃 iterating through generator:")
    for val in gen_obj:
        print(f"   👉 {val}")

if __name__ == "__main__":
    expression_demo()
