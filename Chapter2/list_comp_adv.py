#!/usr/bin/env python3
"""
🚀 Advanced List Comprehensions! 
We'll do some cool math tricks with lists in a single line! ✨
"""

# 📋 Our starting lists
main_numbers = [1, 2, 3, 4]
extra_numbers = [5, 6]

# 1️⃣ Square ONLY the even numbers ⬛ -> 🟦
# Logic: If x is even (x%2==0), square it (x**2).
even_squares = [x**2 for x in main_numbers if x % 2 == 0]

# 2️⃣ Add every number to every other number (Nested Loop) 🔄
# Logic: Take 'x' from main, 'y' from extra, and add them.
sum_combinations = [x + y for x in main_numbers for y in extra_numbers]

# 3️⃣ Create a Dictionary of Squares 📖
# Logic: Key is the number, Value is its square.
square_dictionary_list = [{x: x**2} for x in main_numbers]

# 📢 Print the results!
print(f"🎲 Squares of evens: {even_squares}")
print(f"➕ Sum of nested loops: {sum_combinations}")
print(f"📚 Squares Dictionary: {square_dictionary_list}")
