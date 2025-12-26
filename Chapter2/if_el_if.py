#!/usr/bin/env python3
"""
🔗 If-Elif-Else Chain
Only ONE block will run. It's like a multiple-choice question where you pick the first right answer! 📝
"""

a = 22
b = 44
c = 55
d = None

print("🏃 Running the Chain Check...")

if a and b and c and d:
    print("1️⃣ All are valid.")
elif b and c and d:
    print("2️⃣ 'a' might be missing.")
elif a and c and d:
    print("3️⃣ 'b' might be missing.")
elif a and b and d:
    print("4️⃣ 'c' might be missing.")
elif a and b and c:
    print("5️⃣ 'd' (None) is missing! This is the one! ✅")
else:
    print("❓ Strange outcome.")

print("🏁 Done.")
