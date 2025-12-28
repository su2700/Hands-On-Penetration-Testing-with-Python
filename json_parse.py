#!/usr/bin/env python3
"""
📦 JSON Parser
Managing structured data like web apps do! 🌐
JSON = JavaScript Object Notation (But Python loves it too!) 🐍
"""

import json
import sys
import os

class JsonMaster:
    def __init__(self, filepath):
        self.json_path = filepath
        if not os.path.exists(filepath):
            print(f"⚠️ Warning: '{filepath}' not found.")

    def analyze_file(self):
        """Reads and displays JSON content. 🧐"""
        print("\n" + "="*40)
        print("       ANALYZING JSON       ")
        print("="*40)
        
        try:
            with open(self.json_path, "r") as json_file:
                data = json.load(json_file)
                
            print(f"   📦 Data Type: {type(data)}")
            
            # Navigate structure (Assumes 'employees' key exists)
            root = data.get("employees", {})
            
            if root:
                print(f"   🏢 Dept:     {root.get('department')}")
                print(f"   📍 Location: {root.get('location')}")
                print("\n   👥 Staff List:")
                
                for emp in root.get("data", []):
                    print("      " + "-"*20)
                    for k, v in emp.items():
                        print(f"      🔹 {k.capitalize()}: {v}")
            else:
                print("   ❓ 'employees' key not found.")
                
            return data # Return for processing
            
        except Exception as e:
            print(f"   ❌ Error Read: {e}")
            return None

    def process_slabs(self):
        """Updates 'Slab' based on Salary. 💰"""
        print("\n" + "="*40)
        print("       PROCESSING SLABS       ")
        print("="*40)
        
        data = self.analyze_file()
        if not data:
            return

        print("\n   ⚙️  Calculating Slabs...")
        
        emp_list = data["employees"]["data"]
        modified = False
        
        for i, emp in enumerate(emp_list):
            name = emp.get("name", "Unknown")
            salary = emp.get("salary", 0)
            
            old_slab = emp.get("slab", "N/A")
            new_slab = "A" if salary >= 30000 else "B"
            
            # Apply Change
            if old_slab != new_slab:
                print(f"      🔄 {name}: {old_slab} -> {new_slab}")
                data["employees"]["data"][i]["slab"] = new_slab
                modified = True
            
        if modified:
            print("\n   💾 Saving Changes...")
            with open(self.json_path, "w") as json_file:
                json.dump(data, json_file, indent=4, sort_keys=True)
            print("   ✅ Saved!")
            
            # Show result
            self.analyze_file()
        else:
            print("   💤 No changes needed.")

if __name__ == "__main__":
    target_file = "employees.json"
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
        
    print(f"🎯 Target File: {target_file}")
    
    master = JsonMaster(target_file)
    master.process_slabs()
