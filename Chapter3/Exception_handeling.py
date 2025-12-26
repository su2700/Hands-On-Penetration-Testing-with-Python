#!/usr/bin/env python3
"""
🛡️ Exception Handling
Coding without a safety net is dangerous! 🤸‍♂️
Catch those errors before they crash your program! 💥
"""

class MathWizard():
    
    # 1️⃣ Basic Try-Except
    def div_basic(self, num1, num2):
        print(f"\n1️⃣ Attempting: {num1} / {num2}")
        try:
            res = num1 / num2
            print(f"   ✅ Result: {res}")
        except Exception as ex:
            print(f"   ❌ OOPS! Error: {ex}")

    # 2️⃣ Try-Except-Finally (Cleanup always happens!)
    def div_cleanup(self, num1, num2):
        print(f"\n2️⃣ Attempting (with Cleanup): {num1} / {num2}")
        try:
            res = num1 / num2
            print(f"   ✅ Result: {res}")
        except Exception as ex:
            print(f"   ❌ OOPS! Error: {ex}")
        finally:
            print("   🧹 Cleaning up resources... (This always runs!)")

    # 3️⃣ Custom Errors (Raising the flag!) 🚩
    def div_strict(self, num1, num2):
        print(f"\n3️⃣ Strict Division: {num1} / {num2}")
        try:
            if num2 == 0:
                raise ValueError("⛔ We do NOT allow dividing by zero here!")
            
            res = num1 / num2
            print(f"   ✅ Result: {res}")
            
        except Exception as exc:
            print(f"   🚩 Caught Raised Error: {exc}")

# 🪄 Magic Time
wiz = MathWizard()

# Scenario 1: Success
wiz.div_basic(10, 2)
# Scenario 2: Fail
wiz.div_basic(10, 0)

# Scenario 3: Cleanup
wiz.div_cleanup(10, 0)

# Scenario 4: Manual Raise
wiz.div_strict(10, 0)

print("\n🎉 Program survived all errors!")
