#!/usr/bin/env python3
"""
🏆 Python Best Practices Demo
This file demonstrates the proper habits for declaring classes and functions.
"""

# 1. Constants goes at the top, in UPPER_CASE
MAX_LEVEL = 100
DEFAULT_Element = "Fire"

class HeroCharacter:
    """
    🛡️ A class representing a Hero.
    Note the 'PascalCase' naming for classes!
    """

    def __init__(self, name: str, level: int = 1):
        """
        The constructor.
        :param name: The hero's name (String)
        :param level: The hero's starting level (Integer)
        """
        self.name = name
        self.level = level
        print(f"✨ Hero {self.name} summoned at level {self.level}!")

    def attack_enemy(self, damage: int) -> bool:
        """
        Performs an attack.
        Note the 'snake_case' for function names!
        
        :param damage: How much damage to deal
        :return: True if attack is successful
        """
        print(f"⚔️ {self.name} attacks for {damage} damage!")
        
        if damage > 0:
            return True
        return False

    def _internal_heal(self):
        """
        Stats with '_', meaning it's intended for internal use only (private-ish).
        """
        print("❤️ Healing...")

def quick_math(a: int, b: int) -> int:
    """
    A standalone function demonstration.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: The sum
    """
    return a + b

# 🛡️ Main Guard: Always use this!
if __name__ == "__main__":
    # Create an instance of the class
    my_hero = HeroCharacter("Noah", level=50)
    
    # Call a method
    success = my_hero.attack_enemy(999)
    print(f"   Attack Success: {success}")
    
    # Call a regular function
    result = quick_math(10, 20)
    print(f"   Math Result: {result}")
