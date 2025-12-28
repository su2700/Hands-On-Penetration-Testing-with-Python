#!/usr/bin/env python3
"""
⌨️ The Command Center (Subprocess)
Run terminal commands right from your Python script! 
Hacker Mode: ON 🕶️
"""

import subprocess
import chardet # Helps guess text encoding

class CommandRunner:
    
    def run_command(self, command_list):
        """
        Executes a shell command safely.
        """
        print(f"\n🚀 Executing: {' '.join(command_list)}")
        print("-" * 30)
        
        try:
            # 1️⃣ Spawn the Process
            # Popen is powerful! It opens a pipe to the system.
            process = subprocess.Popen(
                command_list,
                shell=False,           # False is safer! (Avoids shell injection)
                stdout=subprocess.PIPE, # Capture Output
                stderr=subprocess.PIPE  # Capture Errors
            )
            
            print(f"   🆔 Process ID: {process.pid}")
            
            # 2️⃣ Communicate (Wait for finish & get data)
            # This blocks until the command finishes
            raw_out, raw_err = process.communicate()
            
            # 3️⃣ Decode & Print Output
            if raw_out:
                print("\n   ✅ OUTPUT:")
                # Auto-detect encoding or fallback to utf-8
                encoding = chardet.detect(raw_out)['encoding'] or 'utf-8'
                decoded_out = raw_out.decode(encoding)
                
                # Print line by line for neatness
                for line in decoded_out.splitlines():
                    print(f"      {line}")
            
            # 4️⃣ Decode & Print Errors
            if raw_err:
                print("\n   ⚠️ ERRORS:")
                decoded_err = raw_err.decode('utf-8')
                for line in decoded_err.splitlines():
                    print(f"      {line}")

        except Exception as ex:
            print(f"   ❌ OOPS: {ex}")

if __name__ == "__main__":
    runner = CommandRunner()
    
    # Try listing files (Linux/Mac: ls -l, Windows: dir)
    # Since we are on Linux:
    runner.run_command(["ls", "-l", "/home/noah/Documents"])
