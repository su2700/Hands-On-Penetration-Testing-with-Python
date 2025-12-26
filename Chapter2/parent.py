#!/usr/bin/env python3
"""
👨‍👦 Parent Script
I am the Parent. I check on the Child.
"""

import child as c

def parent_method():
    print("\n👨 Parent: Checking on child...")
    print("--------------------")
    c.child_method()
    print("--------------------")
    print("👨 Parent: Good job child.\n")

parent_method()
