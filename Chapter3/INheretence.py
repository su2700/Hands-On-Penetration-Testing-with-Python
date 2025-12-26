#!/usr/bin/env python3
"""
🧬 Inheritance
The Family Tree! 🌳
Employees inherit traits from... well, nobody in real life, 
but here they are composed of Departments, Managers, and Addresses!
"""

# 🆔 ID Maker
class IdGenerator():
    def __init__(self):
        self.curr = 0
    def generate(self):
        self.curr += 1
        return self.curr

# 🏢 Department
class Department():
    def __init__(self, name, loc):
        self.name = name
        self.loc = loc
    def get_info(self):
        return f"{self.name} ({self.loc})"

# 👔 Manager
class Manager():
    def __init__(self, m_id, name):
        self.m_id = m_id
        self.name = name
    def get_info(self):
        return f"{self.name} (ID: {self.m_id})"

# 📍 Address
class Address():
    def __init__(self, country, city, street):
        self.country = country
        self.city = city
        self.street = street
    def get_info(self):
        return f"{self.street}, {self.city}, {self.country}"

# 👷 Employee (The central hub)
class Employee():
    def __init__(self, name, id_gen, dept, manager, address):
        self.id = id_gen.generate()
        self.name = name
        self.dept = dept
        self.mgr = manager
        self.addr = address
        self.salary = 0 # Default
        
    def print_details(self):
        print("\n" + "-"*30)
        print(f"📄 RECORD: {self.name}")
        print("-"*30)
        print(f"   🆔 System ID: {self.id}")
        print(f"   💰 Salary:    ${self.salary}")
        print(f"   🏢 Dept:      {self.dept.get_info()}")
        print(f"   👔 Manager:   {self.mgr.get_info()}")
        print(f"   📍 Address:   {self.addr.get_info()}")
        print("-"*30 + "\n")

# 🌍 World Building
if __name__ == "__main__":
    gen = IdGenerator()
    
    # 🏗️ Create Components
    dept_it = Department("Cyber Security", "Bunker 1")
    boss = Manager(101, "Agent Smith")
    home = Address("Matrix", "Zion", "Sector 7")
    
    # 👶 Create Employee
    neo = Employee("Neo", gen, dept_it, boss, home)
    neo.salary = 500000
    
    # 🖨️ Print
    neo.print_details()
    
    print("✅ Employee Database Updated.")
