#!/usr/bin/env python3
"""
COMPARE: VersaLaw2 vs Legalmind-AI
"""

import os

def main():
    print("🔍 COMPARISON: VERSALAW2 vs LEGALMIND-AI")
    print("=" * 50)
    
    # Current directory
    current_dir = os.getcwd()
    print(f"📍 Current directory: {current_dir}")
    
    # Paths
    versalaw2_path = "src/versalaw2"
    legalmind_path = "../legalmind-project/legalmind-ai"
    
    print(f"📦 VersaLaw2 path: {versalaw2_path}")
    print(f"🧠 Legalmind-AI path: {legalmind_path}")
    
    # Check paths
    if not os.path.exists(versalaw2_path):
        print("❌ VersaLaw2 path not found!")
        return
        
    if not os.path.exists(legalmind_path):
        print("❌ Legalmind-AI path not found!")
        return
    
    # Get VersaLaw2 modules
    versalaw2_modules = set()
    for root, dirs, files in os.walk(versalaw2_path):
        for file in files:
            if file.endswith('.py') and file != '__init__.py':
                versalaw2_modules.add(file)
                print(f"📦 VersaLaw2: {file}")
    
    # Get Legalmind-AI modules
    legalmind_modules = set()
    for file in os.listdir(legalmind_path):
        if file.endswith('.py') and file != '__init__.py':
            legalmind_modules.add(file)
            print(f"🧠 Legalmind: {file}")
    
    print(f"\n🎯 UNIQUE MODULES IN LEGALMIND-AI:")
    unique_modules = legalmind_modules - versalaw2_modules
    for mod in sorted(unique_modules):
        print(f"   🚀 {mod}")
    
    print(f"\n📊 SUMMARY:")
    print(f"   VersaLaw2 modules: {len(versalaw2_modules)}")
    print(f"   Legalmind-AI modules: {len(legalmind_modules)}")
    print(f"   Unique to integrate: {len(unique_modules)}")

if __name__ == "__main__":
    main()
