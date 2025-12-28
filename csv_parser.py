#!/usr/bin/env python3
"""
📊 CSV Parser
Crunching spreadsheet data! 🔢
We read, we filter, we write back! ♻️
"""

import csv
import sys
import os

class CSVParser:
    def __init__(self, filepath):
        self.csv_path = filepath
        self.employees = []
        
        if not os.path.exists(filepath):
            print(f"❌ Error: File '{filepath}' not found!")
            # Create a dummy file if needed for demo?
            # For now, we will handle it gracefully.

    def parse_basic(self):
        """Reads CSV using standard Reader and DictReader 📖"""
        print("\n" + "="*40)
        print("       READING CSV DATA       ")
        print("="*40)

        # Method 1: Standard Reader (Returns Lists) 📋
        print("\n1️⃣  Standard Reader (Lists):")
        try:
            with open(self.csv_path, 'r') as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader) # Skip Header
                
                print(f"   🏷️  Header: {header}")
                print("   👇 User Data:")
                
                for row in reader:
                    print(f"      🔹 {row}")
                    
                    # Store as dictionary for processing later
                    # Note: This relies on specific column indexes!
                    if len(row) >= 5:
                        emp = {
                            "Name": row[0],
                            "Age": row[1],
                            "Salary": row[2],
                            "M_id": row[3],
                            "Slab": row[4] # Assuming Slab is column 4
                        }
                        self.employees.append(emp)
                        
        except Exception as e:
            print(f"   ❌ Read Error: {e}")

        # Method 2: DictReader (Returns Dictionaries) 📕
        print("\n2️⃣  DictReader (Dictionaries):")
        try:
            with open(self.csv_path, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                print(f"   🏷️  Fields: {reader.fieldnames}")
                
                for row in reader:
                    # Clean output
                    print(f"      🔸 {row['Name']} | ${row['Salary']}")
                    
        except Exception as e:
            print(f"   ❌ DictReader Error: {e}")

    def process_data(self):
        """Filters data and updates the file! ⚙️"""
        print("\n" + "="*40)
        print("       PROCESSING DATA       ")
        print("="*40)
        
        if not self.employees:
            print("   ⚠️ No data to process! Run parse_basic() first?")
            return

        print("   ⚙️  Calculating Slabs (A for Salary >= 30,000)...")
        for emp in self.employees:
            try:
                salary = int(emp.get("Salary", 0))
                if salary >= 30000:
                    emp["Slab"] = "A 🌟"
                else:
                    emp["Slab"] = "B"
            except ValueError:
                 print(f"      ⚠️ Invalid Salary for {emp.get('Name')}")

        print("   💾 Saving Updated Data...")
        
        # Write back to file
        try:
            header = self.employees[0].keys()
            with open(self.csv_path, "w", newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=header)
                writer.writeheader()
                writer.writerows(self.employees)
            print("   ✅ Data Saved Successfully!")
            
        except Exception as e:
            print(f"   ❌ Write Error: {e}")

        # Reprint to show changes
        self.parse_basic()

if __name__ == "__main__":
    # Default to 'employees.csv' if no arg provided
    target_file = "employees.csv"
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
    
    print(f"🎯 Target File: {target_file}")
    
    parser = CSVParser(target_file)
    parser.parse_basic()
    parser.process_data()
