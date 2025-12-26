#!/usr/bin/env python3
"""
📐 Area Finder Module
This is the BRAINS of the operation! 🧠
It calculates the area based on the shape you ask for.
"""

def compute_area(shape, **kwargs):
    """
    Computes area for various shapes.
    
    **kwargs (The Magic Dictionary 🎩):
    We use **kwargs to accept ANY named arguments (like radius=5, width=10).
    It packs them into a dictionary so we can pick out what we need!
    """
    
    # Normalize input to lowercase
    shape_type = shape.lower()
    
    # 🟣 Circle
    if shape_type == "circle":
        radius = kwargs.get("radius", 0)
        area = 3.14 * (radius ** 2)
        print(f"   🟣 Area of Circle (r={radius}): {area}")
        
    # 🟦 Rectangle
    elif shape_type in ["rect", "rectangle"]:
        length = kwargs.get("length", 0)
        width = kwargs.get("width", 0)
        area = length * width
        print(f"   🟦 Area of Rectangle ({length}x{width}): {area}")
        
    # 🔺 Triangle
    elif shape_type == "triangle":
        base = kwargs.get("base", 0)
        altitude = kwargs.get("altitude", 0)
        area = (base * altitude) / 2
        print(f"   🔺 Area of Triangle (b={base}, h={altitude}): {area}")
        
    # ⬛ Square
    elif shape_type == "square":
        side = kwargs.get("side", 0)
        area = side ** 2
        print(f"   ⬛ Area of Square (side={side}): {area}")
        
    # ❓ Unknown
    else:
        print(f"   ❌ Shape '{shape}' not supported yet!")
