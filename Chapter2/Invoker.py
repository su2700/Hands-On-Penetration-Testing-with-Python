#!/usr/bin/env python3
"""
🧙‍♂️ The Invoker
This script demonstrates how to call functions from other modules.
It's like casting a spell from a spellbook! 📖
"""

# Importing the area_finder module as 'AF' (short alias)
from shapes import area_finder as AF

# Alternative import (unused here but good to know!):
# import shapes.area_finder as AFF

def find_area():
    """
    Calls compute_area for various shapes using the imported module.
    """
    print("✨ Invoking Shape spells...")

    # 1. Circle Calculation 🟣
    AF.compute_area("circle", radius=4)

    # 2. Triangle Calculation 🔺
    AF.compute_area("triangle", base=4, altitude=6)

    # 3. Rectangle Calculation 🟦
    AF.compute_area("rect", length=12, width=16)

    # 4. Square Calculation ⬛
    AF.compute_area("square", side=4)

# Execute!
find_area()
print("🎉 Invocation complete!")
