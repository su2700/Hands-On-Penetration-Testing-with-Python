#!/usr/bin/env python3
"""
📐 Area Finder Helper
This script uses the 'shapes' module to verify our area calculations.
Running this feels like a math test, but way easier! ✅
"""

from shapes import area_finder as AF

def find_area():
	"""
	Runs area calculations for different shapes.
	"""
	# 🟣 Circle
	print("\n--- 🟣 Circle ---")
	AF.compute_area("circle", radius=5)
	
	# 🟦 Rectangle
	print("\n--- 🟦 Rectangle ---")
	AF.compute_area("rect", length=10, width=5)
	
	# 🔺 Triangle
	print("\n--- 🔺 Triangle ---")
	AF.compute_area("triangle", base=10, altitude=5)
	
	# ⬛ Square
	print("\n--- ⬛ Square ---")
	AF.compute_area("square", side=4)

if __name__ == "__main__":
	print("🚀 Starting Area Calculations...")
	find_area()
	print("\n✅ All done!")
