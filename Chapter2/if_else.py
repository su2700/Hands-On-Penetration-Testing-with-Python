#!/usr/bin/env python3
"""
🚦 If-Else & Bitwise Operators
Decisions, decisions... and some binary magic! 🪄
"""

a = 22
b = 44
c = 55
d = None

# Basic Check
print("\n--- 🤔 Basic Check ---")
if a and b and c and d:
    print("❌ All True")
else:
    print("✅ Condition failed (one was False/None).")

if a == b:
    print("❌ They are equal.")
else:
    print(f"✅ {a} is NOT equal to {b}.")

# Bitwise Magic
print("\n--- 🧙‍♂️ Bitwise Magic ---")
val_a = 2
val_b = 2
val_c = 0

# AND operator
print("\n👉 Bitwise AND (&)")
result = val_a & val_b & val_c
if result:
    print(f"   Result: {result} (Non-Zero)")
else:
    print(f"   Result: {result} (Zero)")

result_ab = val_a & val_b
if result_ab:
    print(f"   {val_a} & {val_b} = {result_ab} (Non-Zero) ✅")

# OR operator
print("\n👉 Bitwise OR (|)")
res_or = val_a | val_c
if res_or:
    print(f"   {val_a} | {val_c} = {res_or} (Should be 2)")

# Shifts
print("\n👉 Bit Shifts (<< >>)")
left_shift = val_a << val_b
if left_shift:
    print(f"   {val_a} << {val_b} = {left_shift} (Multiplication!)")

right_shift = val_a >> val_b
if right_shift:
    print(f"   {val_a} >> {val_b} = {right_shift}")
else:
    print(f"   {val_a} >> {val_b} = {right_shift} (Zero - Division effect)")

# Negation
print("\n👉 Bitwise NOT (~)")
neg_val = ~val_a
print(f"   ~{val_a} = {neg_val} (It flips bits! Usually -x-1)")
