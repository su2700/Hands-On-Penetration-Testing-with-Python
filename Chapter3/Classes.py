#!/usr/bin/env python3
"""
🏭 Classes & Objects
The Factory Floor! defining templates for Employees and Specialists. 👷
"""

# 🆔 Automatic ID Maker
class IdGenerator():
    def __init__(self):
        self.id = 0
    def generate(self):
        self.id += 1
        return self.id

# 👤 Base Employee
class Employee():
    def __init__(self, name, id_gen):
        self.id = id_gen.generate()
        self.name = name
        self.salary = None
    
    def print_details(self):
        print(f"\n👤 Employee: {self.name} (ID: {self.id})")
        print(f"   💰 Salary: {self.salary}")

# 💻 Programmer (Specialized Employee)
class Programmer(Employee):
    def __init__(self, name, id_gen, lang=None, db=None, projects=None, **skills):
        # Initialize Parent
        super().__init__(name, id_gen)
        
        # Specialist Attributes
        self.languages = lang if lang else []
        self.db = db if db else []
        self.projects = projects if projects else []
        self.extra_skills = skills # **kwargs for extra stuff
        
    def print_skill_details(self):
        print("\n" + "="*40)
        print(f"💻 PROGRAMMER PROFILE: {self.name}")
        print("="*40)
        print(f"   🔢 ID: {self.id}")
        print(f"   💰 Salary: {self.salary}")
        
        print("\n   🗣️  Languages:")
        for l in self.languages:
            print(f"      - {l}")
            
        print("\n   🗄️  Databases:")
        for d in self.db:
            print(f"      - {d}")
            
        print("\n   🚀 Projects:")
        for p in self.projects:
            print(f"      - {p}")
            
        print("\n   ✨ Extra Skills:")
        for category, items in self.extra_skills.items():
            print(f"      🔹 {category.replace('_', ' ').title()}:")
            for item in items:
                print(f"          • {item}")
        print("="*40 + "\n")

# 🏗️ Execution
if __name__ == "__main__":
    id_machine = IdGenerator()
    
    # Hiring a Super Coder
    coder = Programmer(
        "Neo", 
        id_machine,
        lang=["Python", "C++", "Java"],
        db=["MySQL", "PostgreSQL"],
        projects=["Matrix v1", "Defense Grid"],
        # Extra Skills (**kwargs)
        os=["Linux (Kali)", "Windows"],
        hacking=["Penetration Testing", "Reverse Engineering"]
    )
    
    coder.salary = 150000
    coder.print_skill_details()
