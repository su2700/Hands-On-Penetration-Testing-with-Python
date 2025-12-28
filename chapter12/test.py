#!/usr/bin/env python
"""
🧪 Test Caller
Simply calls the 'buff' program with valid arguments to see it work normal.
This is the Control Group. 🧪
"""

import subprocess

def run_test():
    # 📝 Construct normal parameter
    # A sequence of readable characters
    param = "buff "
    
    # 0xa1 to 0xff are extended ASCII, should handle it fine?
    for i in range(0xa1, 0xff):
        param += chr(i)
        
    print "\n🧪 Running 'buff' with safe(ish) parameters..."
    print "   📝 Params length: " + str(len(param))
    
    try:
        # Note: 'buff' expects args, so we split the string into a list for call
        # Or we call it as a single string if it's shell=True
        # Original was: subprocess.call(param) which implies shell behavior or list issue
        
        # Let's clean it up to work as standard shell exec
        # Assuming param is the full command line "buff <args>"
        # But subprocess.call needs a list if shell=False
        
        cmd_list = param.split()
        # Ensure binary exists (using ./buff for local)
        cmd_list[0] = "./buff" 
        
        subprocess.call(cmd_list)
        print "\n✅ Execution finished."
        
    except Exception as e:
        print "   ❌ Error: " + str(e)

if __name__ == "__main__":
    run_test()