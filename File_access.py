#!/usr/bin/env python3
"""
📂 File Access 101
Reading, Writing, and Appending files like a pro! ✍️
"""

class FileMaster:
    def __init__(self, filepath):
        self.path = filepath
        print(f"   📂 Selected File: {self.path}")

    def read_file(self):
        """Reads file in various ways! 🧐"""
        print("\n📖 --- Reading File ---")
        
        try:
            with open(self.path, "r+") as f:
                # 1. Read EVERYTHING 🌍
                print("   🌍 Reading ALL data...")
                all_data = f.read()
                print(f"      Size: {len(all_data)} chars")

                # 2. Read Lines (List) 📜
                f.seek(0) # Rewind to start ⏪
                all_lines = f.readlines()
                
                print("\n   📜 Line by Line:")
                for i, line in enumerate(all_lines):
                    print(f"      #{i}: {line.strip()}")

                # 3. Buffered Read (Chunks) 🍪
                f.seek(0) # Rewind ⏪
                chunk = f.read(20) # Read first 20 chars
                print(f"\n   🍪 First 20 chars (Buffer): '{chunk}'")

        except FileNotFoundError:
            print("   ❌ File not found! Did you create it first?")

    def write_data(self, content, mode="w+", use_newlines=False):
        """Writes data to the file. ✍️"""
        action = "Overwriting" if "w" in mode else "Appending"
        print(f"\n✍️ --- {action} Data ---")
        
        with open(self.path, mode) as outfile:
            if isinstance(content, list):
                print(f"   📋 Writing List of {len(content)} items...")
                if use_newlines:
                    for line in content:
                        outfile.write(line + "\n")
                else:
                    outfile.writelines(content)
            elif isinstance(content, str):
                print("   📝 Writing String...")
                outfile.write(content)
            else:
                print("   ❌ Invalid Content Type!")
        
        print("   ✅ Done!")

class Driver:
    def main(self):
        print("\n--- 🏁 Start File Demo ---")
        
        # 1. Create Object
        my_file = FileMaster("python.txt")
        
        # 2. Write (Overwrite)
        write_list = ["Learning Python is fun! 🐍", " Just started it."]
        my_file.write_data(write_list)
        
        # 3. Append
        append_list = ["I want to explore all of it! 🚀", "It's awesome! ✨"]
        my_file.write_data(append_list, mode="a+", use_newlines=True)
        
        # 4. Read Verification
        my_file.read_file()
        
        print("\n--- 🏁 End Demo ---")

if __name__ == "__main__":
    app = Driver()
    app.main()
