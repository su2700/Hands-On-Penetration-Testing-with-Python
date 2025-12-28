#!/usr/bin/env python3
"""
🧙‍♂️ The Invoker

This script demonstrates how to call functions from other modules.
It's like casting a spell from a spellbook! 📖
"""

# 📚 Import Module (The Spellbook)
# Import 'area_finder' from the 'shapes' package.
# We alias it as 'AF' to keep things short and sweet!
from shapes import area_finder as AF

# Alternative import (not used here, but good to know):
# import shapes.area_finder as AFF

def find_area():
    """
    🔮 Casting Spells
    Calls the compute_area function to calculate areas for various shapes.
    """
    print("✨ Invoking Shape spells...")

    # 1. 🟣 Circle
    # Pass radius
    AF.compute_area("circle", radius=4)

    # 2. 🔺 Triangle
    # Pass base and altitude
    AF.compute_area("triangle", base=4, altitude=6)

    # 3. 🟦 Rectangle
    # Pass length and width
    AF.compute_area("rect", length=12, width=16)

    # 4. ⬛ Square
    # Pass side length
    AF.compute_area("square", side=4)

# 🚀 Execution (Done!)
if __name__ == "__main__":
    find_area()
    print("🎉 Invocation complete!")
