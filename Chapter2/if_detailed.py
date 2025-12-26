#!/usr/bin/env python3
"""
🧐 Detailed If Statements
Python figures out if something is True or False (Truthiness).
"""

a = 22
b = 44
c = 55
d = None  # ⛔ None is essentially "Nothing"
e = True
f = False

print("\n--- 🕵️ Truthiness Check ---")
if 22:
    print("✅ 22 is True-ish!")
if "hello":
    print("✅ 'hello' is True-ish!")
if -1:
    print("✅ -1 is True-ish!")
if 0:
    print("❌ 0 is False-ish (Won't print)")
if d:
    print("❌ None is False-ish (Won't print)")
if e:
    print("✅ True is... True!")
if f:
    print("❌ False is... False!")

print("\n--- 🧠 Logical Operators ---")

if a and b and c:
    print(f"✅ All are set: {a}, {b}, {c}")

if a and b and c and d:
    print("❌ Won't print because 'd' is None")

if a < b and a < c:
    print(f"✅ {a} is the smallest!")

if (a < b) and (a < c):
    print(f"✅ {a} is still the smallest (with braces)")

if a or b or c or d:
    print("✅ At least ONE of them is valid!")

if not d:
    print("✅ 'not None' becomes True!")
