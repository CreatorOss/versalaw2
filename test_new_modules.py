#!/usr/bin/env python3
"""
TEST NEW MODULES - Comprehensive coverage expansion
"""

import sys
import os
import importlib.util

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_new_modules():
    print("🧪 TEST NEW COMPREHENSIVE MODULES")
    print("=" * 60)
    
    new_modules = [
        # Civil Law
        ("Contract Law", "versalaw2/indonesian_law/civil_law/contract_law_analyzer.py", "ContractLawAnalyzer"),
        
        # Commercial Law  
        ("Company Law", "versalaw2/indonesian_law/commercial_law/company_law_analyzer.py", "CompanyLawAnalyzer"),
        
        # Agrarian Law
        ("Land Law", "versalaw2/indonesian_law/agrarian_law/land_law_analyzer.py", "LandLawAnalyzer"),
    ]
    
    print("🔍 TESTING NEW MODULES:")
    print("=" * 60)
    
    successful = 0
    for name, file_path, expected_class in new_modules:
        if not os.path.exists(file_path):
            print(f"❌ {name}: FILE NOT FOUND")
            continue
            
        try:
            spec = importlib.util.spec_from_file_location("module.name", file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Find analyzer class
            analyzer_class = None
            for attr_name in dir(module):
                if 'Analyzer' in attr_name and not attr_name.startswith('_'):
                    analyzer_class = getattr(module, attr_name)
                    break
            
            if analyzer_class is None:
                print(f"❌ {name}: NO ANALYZER CLASS FOUND")
                continue
            
            # Test functionality
            analyzer = analyzer_class()
            
            if "Contract" in name:
                test_data = {"kesepakatan": True, "kecakapan": True, "objek_tentu": True, "sebab_halal": True}
            elif "Company" in name:
                test_data = {"min_two_shareholders": True, "min_capital_met": True, "akta_notaris": True}
            elif "Land" in name:
                test_data = {"double_certificate": True}
            else:
                test_data = {"test": True}
                
            result = analyzer.analyze(test_data)
            
            print(f"✅ {name}: WORKING")
            successful += 1
            
        except Exception as e:
            print(f"❌ {name}: ERROR - {e}")
    
    print(f"\n📊 RESULTS: {successful}/{len(new_modules)} new modules working")
    
    # Update total count
    total_modules = 23 + successful  # Previous 23 + new modules
    print(f"🇮🇩 TOTAL INDONESIAN LAW MODULES: {total_modules}")
    
    return successful == len(new_modules)

if __name__ == "__main__":
    success = test_new_modules()
    if success:
        print("\n🎉 ALL NEW MODULES ADDED SUCCESSFULLY!")
        print("🚀 VERSALAW2 COVERAGE SIGNIFICANTLY EXPANDED!")
    else:
        print("\n⚠️  SOME NEW MODULES NEED ATTENTION!")
