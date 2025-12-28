#!/usr/bin/env python3
"""
🧭 OS Directory Navigator
Exploring the file system with Python! 🗺️
Create, Delete, Rename, and Travel! 🚶‍♂️
"""

import os
import shutil

class DirectoryExplorer:
    def __init__(self):
        self.script_path = os.path.realpath(__file__)
        self.root_dir = os.path.dirname(self.script_path)
        print(f"📍 Start Point: {self.root_dir}")

    def scan_directory(self, path, scan_subdirs=False):
        """Lists files in a directory. 📋"""
        print(f"\n🔎 Scanning: '{os.path.basename(path)}'")
        
        if not os.path.exists(path):
            print("   ❌ Path does not exist!")
            return

        if not scan_subdirs:
            # Simple List
            items = os.listdir(path)
            for item in items:
                full_path = os.path.join(path, item)
                if os.path.isdir(full_path):
                    print(f"   📁 [DIR]  {item}")
                else:
                    print(f"   📄 [FILE] {item}")
        else:
            # Recursive Walk 🚶‍♂️
            print("   🚶 Walking through subdirectories...")
            for root, dirs, files in os.walk(path):
                level = root.replace(path, '').count(os.sep)
                indent = ' ' * 4 * (level)
                print(f"{indent}📁 {os.path.basename(root)}/")
                subindent = ' ' * 4 * (level + 1)
                for f in files:
                    print(f"{subindent}📄 {f}")

    def manage_directory(self, dir_name, action="create"):
        """Creates or Changes directory. 🛠️"""
        target_path = os.path.join(self.root_dir, dir_name)
        
        if action == "create":
            print(f"\n🆕 ACTION: Create Folder '{dir_name}'")
            if not os.path.exists(target_path):
                os.mkdir(target_path)
                print("   ✅ Created!")
            else:
                print("   ⚠️ Already exists.")
            self.scan_directory(self.root_dir)

        elif action == "change":
            print(f"\n🚪 ACTION: Enter Folder '{dir_name}'")
            print(f"   🏠 Before: {os.getcwd()}")
            try:
                os.chdir(target_path)
                print(f"   🏘️ After:  {os.getcwd()}")
                # Go back home 🏠
                os.chdir(self.root_dir)
            except FileNotFoundError:
                print("   ❌ Cannot find it!")

    def file_operations(self, relative_path, operation="delete", new_name="renamed.txt"):
        """Delete or Rename files. 🗑️/🏷️"""
        target_path = os.path.join(self.root_dir, relative_path)
        parent = os.path.dirname(target_path)
        
        print(f"\n🔧 ACTION: {operation.upper()} on '{os.path.basename(target_path)}'")
        
        if not os.path.exists(target_path):
            print("   ❌ File missing! Creating dummy for demo...")
            # Create dummy file to ensure demo works
            with open(target_path, 'w') as f: f.write("dummy")
        
        if operation == "delete":
            os.remove(target_path)
            print("   🗑️  Deleted!")
            
        elif operation == "rename":
            new_path = os.path.join(parent, new_name)
            os.rename(target_path, new_path)
            print(f"   🏷️  Renamed to '{new_name}'")
            
        self.scan_directory(parent)

if __name__ == "__main__":
    explorer = DirectoryExplorer()
    
    # 1. Create a Test Folder 📁
    explorer.manage_directory("Test_folder", "create")
    
    # 2. Enter it 🚪
    explorer.manage_directory("Test_folder", "change")
    
    # 3. Setup for file ops
    demo_folder = os.path.join(explorer.root_dir, "remove_folder")
    if not os.path.exists(demo_folder):
        os.mkdir(demo_folder)
        
    # 4. Delete Demo 🗑️
    explorer.file_operations("remove_folder/remove_file1.txt", "delete")
    
    # 5. Rename Demo 🏷️
    explorer.file_operations("remove_folder/remove_file2.txt", "rename", "updated.txt")
