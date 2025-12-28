#!/usr/bin/env python2
"""
💥 The Fuzzer
Throwing stuff at the wall until it breaks! 🧱🔨
We increase the input size until the program crashes.
"""

import subprocess as sp
import time

def fuzz_target():
    print "\n🤖 Fuzzer Initialized..."
    print "   🎯 Target: ./buff"
    
    length = 1
    step_size = 10
    
    while True:
        # Create a string of 'a's with increasing length
        fuzz_input = 'a' * length
        
        # 🏃 Run the target program
        # We pipe our input into it using echo
        command = "echo " + fuzz_input + " | ./buff"
        
        try:
            p = sp.Popen(command, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
            out, err = p.communicate()
            output_lines = out.split("\n")
            
            # Check if it survived
            # We look for the "What is your name?" output or similar normal behavior
            if output_lines and len(output_lines) > 0 and "What" in output_lines[0]:
                print "   ✅ Pass: Length " + str(length) + " survived."
                length += step_size
            else:
                # If we don't see the expected output, it likely crashed!
                print "\n   💥 CRASH DETECTED! 💥"
                print "   💀 Input Length: " + str(length)
                print "   ⚠️ Output dump: " + str(output_lines)
                break
                
        except Exception as e:
            print "   ❌ Execution Error: " + str(e)
            break
            
        # Optional: Sleep to easier watch the progress
        # time.sleep(0.1) 

if __name__ == "__main__":
    fuzz_target()
