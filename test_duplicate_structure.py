#!/usr/bin/env python3
"""
TEST DUPLICATE STRUCTURE - Check if modules in duplicate paths are being used
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_duplicate_imports():
    """Test imports from duplicate structure"""
    print("🔍 TESTING DUPLICATE STRUCTURE IMPORTS")
    print("=" * 60)
    
    # Test standard import
    try:
        from versalaw2.international_law.international_treaties import InternationalTreatyAnalyzer
        print("✅ Standard import: SUCCESS")
        analyzer1 = InternationalTreatyAnalyzer()
        print(f"   Standard location: {analyzer1.__class__.__module__}")
    except Exception as e:
        print(f"❌ Standard import: {e}")
    
    # Test duplicate structure import
    try:
        # Coba import dari path duplikat
        from versalaw2.international_law.versalaw2.international_law.international_treaties import InternationalTreatyAnalyzer as DuplicateAnalyzer
        print("✅ Duplicate structure import: SUCCESS")
        analyzer2 = DuplicateAnalyzer()
        print(f"   Duplicate location: {analyzer2.__class__.__module__}")
        
        # Compare both
        if analyzer1.__class__.__module__ == analyzer2.__class__.__module__:
            print("⚠️  WARNING: Both imports point to SAME module!")
        else:
            print("✅ DIFFERENT modules detected")
            
    except Exception as e:
        print(f"❌ Duplicate structure import: {e}")
    
    # Check file paths
    print("\n📁 FILE PATH CHECK:")
    import versalaw2.international_law.international_treaties as standard_mod
    print(f"Standard module file: {standard_mod.__file__}")
    
    try:
        import versalaw2.international_law.versalaw2.international_law.international_treaties as duplicate_mod
        print(f"Duplicate module file: {duplicate_mod.__file__}")
    except Exception as e:
        print(f"Duplicate module file: NOT ACCESSIBLE - {e}")

def check_all_duplicate_files():
    """Check all files in duplicate structure"""
    print("\n📋 CHECKING ALL FILES IN DUPLICATE STRUCTURE:")
    print("=" * 60)
    
    duplicate_path = "versalaw2/international_law/versalaw2"
    if os.path.exists(duplicate_path):
        for root, dirs, files in os.walk(duplicate_path):
            for file in files:
                if file.endswith('.py'):
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, 'versalaw2/international_law/versalaw2')
                    print(f"📄 {rel_path}")
                    
                    # Check if file has content
                    try:
                        with open(full_path, 'r') as f:
                            content = f.read().strip()
                            if content:
                                print(f"   Size: {len(content)} chars")
                            else:
                                print("   ⚠️  EMPTY FILE")
                    except Exception as e:
                        print(f"   ❌ Error reading: {e}")
    else:
        print("❌ Duplicate path not found")

if __name__ == "__main__":
    test_duplicate_imports()
    check_all_duplicate_files()
