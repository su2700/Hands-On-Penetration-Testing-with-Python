#!/usr/bin/env python3
"""
🤝 Aggregation
"Has-A" Relationship. 
The Departments and Employees exist independently, but they work together! 🏢
"""

# 📍 Address Class
class Address():
    def __init__(self, country, state, street, zip_code):
        self.country = country
        self.state = state
        self.street = street
        self.zip_code = zip_code
        
    def get_info(self):
        return f"{self.street}, {self.state}, {self.country} ({self.zip_code})"

# 👔 Manager Class
class Manager():
    def __init__(self, m_id, name):
        self.m_id = m_id
        self.name = name
        
    def get_info(self):
        return f"Manager: {self.name} (ID: {self.m_id})"

# 🏷️ Department Class
class Department():
    def __init__(self, name, loc):
        self.name = name
        self.loc = loc
        
    def get_info(self):
        return f"Dept: {self.name} @ {self.loc}"

# 🆔 Helper for IDs
class IdGenerator():
    def __init__(self):
        self.current_id = 0
    def generate(self):
        self.current_id += 1
        return self.current_id

# 👷 Employee Class
class Employee():
    def __init__(self, name, id_gen, dept=None, manager=None):
        self.id = id_gen.generate()
        self.name = name
        self.dept = dept        # "Has-A" Department
        self.manager = manager  # "Has-A" Manager
        
    def print_details(self):
        print("\n📋 --- Employee Profile ---")
        print(f"   👤 Name: {self.name}")
        print(f"   🔢 ID:   {self.id}")
        
        if self.dept:
            print(f"   🏢 {self.dept.get_info()}")
        else:
            print("   🏢 Dept: N/A")
            
        if self.manager:
            print(f"   👔 {self.manager.get_info()}")
        else:
            print("   👔 Manager: N/A")
            
        print("---------------------------")

# 🧪 Test Drive
if __name__ == "__main__":
    print("\n--- 🏗️ Building Org Chart ---")
    
    # Tools
    id_gen = IdGenerator()
    
    # Independent Entities
    dept_it = Department("IT Squad", "Floor 42")
    boss_man = Manager(99, "Mr. Stark")
    
    # Employee (Aggregating them)
    emp = Employee("Peter Parker", id_gen, dept=dept_it, manager=boss_man)
    
    emp.print_details()
    
    print("\n✅ Done!")
