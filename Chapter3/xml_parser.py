#!/usr/bin/env python3
"""
📑 XML Parser
Reading structured data like a pro! 👓
"""

import xml.etree.ElementTree as ET
import sys
import os

class XMLParser:
    def __init__(self, xml_source, is_file=True):
        self.xml_source = xml_source
        self.is_file = is_file
        
    def parse(self):
        print(f"\n📂 Parsing {'File' if self.is_file else 'String'}...")
        
        # 🌳 Build the Tree
        if self.is_file:
            if not os.path.exists(self.xml_source):
                print(f"   ❌ File not found: {self.xml_source}")
                return
            root = ET.parse(self.xml_source).getroot()
        else:
            root = ET.fromstring(self.xml_source)

        # 🌱 Root Info
        print(f"   🌱 Root Tag: <{root.tag}>")
        print("   🏷️  Root Attributes:")
        for k, v in root.attrib.items():
            print(f"      - {k}: {v}")

        # 🍂 Leaves (Nodes)
        print("\n🔍 Scanning Employees...")
        
        # Iterate over all children (Employees)
        for employee in root:
            print(f"\n   👤 Employee Found:")
            
            # Auto-discover child tags (Name, Salary, etc)
            for element in employee:
                print(f"      🔹 {element.tag.capitalize()}: {element.text}")
                
        print("\n✅ Parsing Complete!")

# 🧪 Test Data (Embedded Backup)
test_xml = """<employees department="IT" location="Dubai">
    <employee id="1">
        <name>Emp1</name>
        <age>32</age>
        <salary>30000</salary>
        <doj>06/06/2016</doj>
        <manager_id>33</manager_id>
    </employee>
    <employee id="2">
        <name>Emp2</name>
        <age>28</age>
        <salary>27000</salary>
        <doj>18/02/2017</doj>
        <manager_id>33</manager_id>
    </employee>
</employees>"""

if __name__ == "__main__":
    # Check if user provided a file argument
    if len(sys.argv) > 1:
        parser = XMLParser(sys.argv[1], is_file=True)
        parser.parse()
    else:
        print("⚠️ No file provided. Using Demo String data.")
        parser = XMLParser(test_xml, is_file=False)
        parser.parse()
