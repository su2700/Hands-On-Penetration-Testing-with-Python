#!/usr/bin/env python3
"""
🧪 Relative Import Experiment
Testing how to import things from nearby folders. 📂
"""

# ⚠️ Note: Relative imports depend heavily on how you run the script!
# They usually require running as a module (python -m ...).

try:
    print("Attempting imports...")
    from . import area_finder as AF
    # import area_finder as AFF # This might be the absolute import fallback
    
    print("✅ Import successful!")
    AF.compute_area("circle", radius=4)

except ImportError as e:
    print(f"❌ Import failed: {e}")
    print("Tip: Run this as part of a package!")
