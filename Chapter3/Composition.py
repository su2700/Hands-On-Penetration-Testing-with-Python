#!/usr/bin/env python3
"""
🏎️ Composition
"Part-Of" Relationship.
A Ferrari IS A Car, but it HAS AN Engine. The Engine is arguably the most vital part! ❤️
"""

# 🚗 Base Car
class Car():
    def __init__(self, cat, mile, cap):
        self.category = cat
        self.mileage = mile
        self.capacity = cap

# ⚙️ The Engine (Part)
class Engine():
    def get_details(self):
        return (
            "   🐎 V8 Engine (Ferrari/Maserati F136)\n"
            "   ⚡ 562 hp @ 9,000 rpm\n"
            "   🔧 398 lb-ft Torque"
        )

# 🐎 Ferrari (Whole)
class Ferrari(Car):
    def __init__(self, cat, mile, cap, hp, top_speed, acc):
        super().__init__(cat, mile, cap)
        self.hp = hp
        self.top_speed = top_speed
        self.acc = acc
        self.engine = Engine() # Composition: Creating the part INSIDE the whole
        
    def print_specs(self):
        print("\n" + "🔴"*20)
        print("      FERRARI 458 SPECS      ")
        print("🔴"*20)
        print(f"   🏎️  Category:  {self.category}")
        print(f"   👥 Capacity:  {self.capacity}")
        print(f"   🚀 0-60 mph:  {self.acc}")
        print(f"   🏁 Top Speed: {self.top_speed}")
        print("\n   ⚙️  ENGINE SPECS:")
        print(self.engine.get_details())
        print("\n" + "🔴"*20)

# 🏁 Race Time!
if __name__ == "__main__":
    my_dream_car = Ferrari(
        "Sports", 
        "15 mpg", 
        "2 Seater", 
        "562 HP", 
        "202 mph", 
        "3.0 sec"
    )
    my_dream_car.print_specs()
