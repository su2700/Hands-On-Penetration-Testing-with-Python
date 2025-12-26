#!/usr/bin/env python3
"""
🧠 Class Methods vs Static Methods vs Instance Methods
- Instance Method: Needs 'self'. Can touch the object. 👤
- Class Method (@): Needs 'cls'. Can touch the Class (shared). 🏢
- Static Method (@): Needs nothing. Isolated helper. 🏝️
"""

class MethodDemo():
    class_var = 200 # 🌍 Shared by everyone

    def __init__(self):
        self.variable = 0 # 👤 Unique to me

    # 👤 Instance Method
    def instance_method(self):
        self.variable = 100
        print("\n" + "-"*30)
        print("👤 INSIDE INSTANCE METHOD")
        print(f"   My Value: {self.variable}")
        print(f"   Shared Class Var: {self.class_var}")
        print("-" * 30)

    # 🏢 Class Method
    @classmethod
    def class_method(cls):
        print("\n" + "-"*30)
        print("🏢 INSIDE CLASS METHOD")
        
        # We can't see 'self' (specific instance) here!
        # But we CAN see 'cls' (The Blueprint)
        print(f"   Shared Class Var: {cls.class_var}")
        
        # Let's change the shared variable for EVERYONE
        print("   🛠️ Changing Shared Class Var to 33...")
        cls.class_var = 33
        print("-" * 30)

    # 🏝️ Static Method
    @staticmethod
    def static_method():
        print("\n" + "-"*30)
        print("🏝️ INSIDE STATIC METHOD")
        print("   I am isolated. I can't easily see self or cls.")
        print("   I'm just a helper function living in the class.")
        print("-" * 30)

class Driver():
    def main(self):
        print("\n🎬 --- Method Types Demo ---")
        
        obj = MethodDemo()
        
        # 1. Instance Call
        obj.instance_method()
        
        # 2. Class Method Call (Can be called by obj OR Class)
        obj.class_method()      # Calling via Object
        MethodDemo.class_method() # Calling via Class
        
        # 3. Static Method Call
        obj.static_method()
        MethodDemo.static_method()
        
        print("\n🔍 --- Variable Scope Check ---")
        
        # Check current state
        print(f"   Instance 'o' asks for Class Var: {obj.class_var}")
        
        print("\n   🖍️  Overriding Class Var on Instance 'o' (Shadowing)...")
        obj.class_var = 999 
        # This creates a NEW local 'class_var' on 'obj' that hides the real shared one!
        
        print(f"   Instance 'o' Class Var: {obj.class_var} (Modified local copy)")
        print(f"   Original Class Var:     {MethodDemo.class_var} (Unchanged!)")
        
        print("\n🏁 Demo Complete!")

if __name__ == "__main__":
    d = Driver()
    d.main()
