#!/usr/bin/env python3
"""
🏎️ Polymorphism (Functions)
Duck Typing: "If it looks like a duck and quacks like a duck..." 🦆
We don't care what Class it is, as long as it has a .speed() method!
"""

class Ferrari():
    def speed(self):
        print("   🐎 Ferrari: 349 km/h")

class McLaren():
    def speed(self):
        print("   🏎️  McLaren: 362 km/h")

def check_speed(car_obj):
    """
    I don't care what car_obj is, I just want to know its speed!
    """
    print(f"\n🔍 Checking {car_obj.__class__.__name__}...")
    car_obj.speed()

# 🏁 Race Day
print("\n--- 🏁 Speed Test ---")

f_car = Ferrari()
m_car = McLaren()

# The function handles both types easily!
check_speed(f_car)
check_speed(m_car)

print("\n✅ Done!")
