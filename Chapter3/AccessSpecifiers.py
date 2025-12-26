#!/usr/bin/env python3
"""
🔐 Access Specifiers
Who is allowed to touch my stuff? 🛑
- Public: Everyone can see it! 🌍
- Protected (_): Family only (subclasses)! 👨‍👩‍👧
- Private (__): ME ONLY! 🕵️‍♂️
"""

class Parent():
    def __init__(self, pub, prot, priv):
        self.public = pub           # 🟢
        self._protected = prot      # 🟡
        self.__private = priv       # 🔴

class Child(Parent):
    def __init__(self, pub, prot, priv):
        super().__init__(pub, prot, priv)
    
    def print_members(self):
        print("\n👶 Child trying to access variables...")
        
        # 1. Public
        print(f"   ✅ Public:    {self.public}")
        
        # 2. Protected (Technically accessible, but polite conventions say 'don't')
        print(f"   ⚠️ Protected: {self._protected}")
        
        # 3. Private (Will Fail!)
        try:
            print(f"   ❌ Private:   {self.__private}")
        except AttributeError as ex:
            print(f"   🚫 Access Denied! (Exception: {ex})")
            
            # 🕵️‍♂️ The Secret Backdoor (Name Mangling)
            # Python renames private vars to _ClassName__variable
            print(f"   🕵️ Psst... Hacky Access: {self._Parent__private}")

# 🏃 Execution
print("\n--- 🔐 Access Level Demo ---")
ch = Child("Everyone", "Family", "Secret")
ch.print_members()

print("\n🌍 Outside World Access:")
print(f"   ✅ Public: {ch.public}")
print(f"   ⚠️ Protected: {ch._protected} (You shouldn't be doing this!)")

try:
    print(f"   ❌ Private: {ch.__private}")
except AttributeError:
    print("   🚫 Private is hidden from the world!")

print("\n🏁 Demo Done!")
