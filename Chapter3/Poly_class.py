#!/usr/bin/env python3
"""
🎨 Polymorphism (Classes)
Different Shapes, Same Method Name! 
The 'area()' method does different things depending on who calls it. 🎭
"""

import math

# 🟦 Base Shape
class Shape:
    def __init__(self, length=None, breadth=None, height=None, radius=None):    
        self.length = length
        self.breadth = breadth
        self.height = height
        self.radius = radius

    def area(self):             
        raise NotImplementedError("❌ Stop! use a specific shape, not the generic one!")

# ⬛ Square
class Square(Shape):
    def __init__(self, l, b):
        super().__init__(length=l, breadth=b)

    def area(self):
        result = self.length * self.breadth
        print(f"   ⬛ Square Area ({self.length}x{self.breadth}): {result}")

# 🟣 Circle
class Circle(Shape):
    def __init__(self, r):
        # We only need 'radius' here
        super().__init__(radius=r)

    def area(self):
        result = math.pi * (self.radius ** 2)
        print(f"   🟣 Circle Area (r={self.radius}): {result:.2f}")

# 🏗️ Execution
print("\n--- 🎨 Polymorphism Demo ---")

s = Square(3, 4)
s.area()

c = Circle(2)
c.area()

print("\n✅ Same method name .area(), different behavior!")
