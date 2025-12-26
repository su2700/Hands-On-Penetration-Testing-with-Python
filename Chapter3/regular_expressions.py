#!/usr/bin/env python3
"""
🕵️ Regular Expressions (Regex)
Pattern Matching on steroids! 💪
We search for needles in haystacks. 🪡🌾
"""

import re

class RegexHunter:
    def __init__(self, text):
        self.text = text
        print(f"📄 INPUT TEXT: \"{self.text}\"")

    def hunt(self, pattern, replace_with="@", do_replace=False):
        print(f"\n🔍 Pattern: '{pattern}'")
        
        # 1. MATCH (Checks ONLY the beginning of the string)
        match_res = re.match(pattern, self.text, re.M | re.I | re.DOTALL)
        if match_res:
            print(f"   ✅ MATCH (Start): '{match_res.group()}'")
        else:
            print("   ❌ MATCH (Start): None")

        # 2. SEARCH (Checks ANYWHERE in the string)
        search_res = re.search(pattern, self.text)
        if search_res:
            print(f"   ✅ SEARCH (Anywhere): '{search_res.group()}' at index {search_res.start()}-{search_res.end()}")
        else:
            print("   ❌ SEARCH (Anywhere): None")

        # 3. FINDALL (Finds ALL occurrences)
        find_res = re.findall(pattern, self.text)
        if find_res:
            print(f"   ✅ FINDALL (List): {find_res}")
        else:
            print("   ❌ FINDALL (List): []")

        # 4. SUB (Replace)
        if do_replace:
            sub_res = re.sub(pattern, replace_with, self.text)
            print(f"   🔄 SUB (Replace): \"{sub_res}\"")

# 🧪 The Lab
print("\n" + "="*40)
print("       REGEX LABORATORY       ")
print("="*40)

text1 = "Hello => (1) Python Regular Expressions. "
text2 = "(2) Enjoying Python to the fullest !"
full_text = text1 + text2

hunter = RegexHunter(full_text)

# 🐢 Basic Words
hunter.hunt("Hello")

# 🔢 Digits (\d)
hunter.hunt(r'\d') # Matches first digit found

# 🔢 Groups of Non-Digits & Digits
hunter.hunt(r'(\D\d)+')

# 💲 End of String ($)
hunter.hunt(r'!$')

# 🎩 Start of String (^)
hunter.hunt(r'^Hello')

# 🚫 NOT Numbers ([^0-9])
hunter.hunt(r'[^0-9]+')

# 🔄 Replacements
hunter.hunt("Python", "🐍 SnakeLang 🐍", do_replace=True)
hunter.hunt(r'\D+', "#", do_replace=True) # Replace all non-digits with #

print("\n🎉 Regex Hunt Complete!")
