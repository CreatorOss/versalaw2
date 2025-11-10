#!/usr/bin/env python3
"""
TEST HAM AND CHILD PROTECTION MODULES
"""

import sys
import os
import importlib.util

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_ham_modules():
    print("🧪 TEST HAM AND CHILD PROTECTION MODULES")
    print("=" * 60)
    
    ham_modules = [
        # HAM Modules
        ("Human Rights Analyzer", "versalaw2/indonesian_law/human_rights/human_rights_analyzer.py", "HumanRightsAnalyzer"),
        ("Child Protection Analyzer", "versalaw2/indonesian_law/human_rights/child_protection.py", "ChildProtectionAnalyzer"),
        ("Anti-Corruption Comprehensive", "versalaw2/indonesian_law/specialized_law/anti_corruption_comprehensive.py", "AntiCorruptionComprehensiveAnalyzer"),
    ]
    
    print("🔍 TESTING HAM MODULES:")
    print("=" * 60)
    
    successful = 0
    for name, file_path, expected_class in ham_modules:
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
            
            # Test with appropriate data
            if "Human Rights" in name:
                test_data = {"extrajudicial_killing": True}
            elif "Child Protection" in name:
                test_data = {"violation_type": "child_abuse", "child_age": 10}
            elif "Anti-Corruption" in name:
                test_data = {"corruption_type": "budget_corruption", "stolen_amount": 50000000000}
            else:
                test_data = {"test": True}
                
            result = analyzer.analyze(test_data)
            
            print(f"✅ {name}: WORKING")
            successful += 1
            
        except Exception as e:
            print(f"❌ {name}: ERROR - {e}")
    
    print(f"\n📊 RESULTS: {successful}/{len(ham_modules)} HAM modules working")
    
    # Update total count
    total_indonesian = 17 + successful  # Previous 17 + new HAM modules
    print(f"🇮🇩 TOTAL INDONESIAN LAW MODULES: {total_indonesian}")
    
    return successful == len(ham_modules)

if __name__ == "__main__":
    success = test_ham_modules()
    if success:
        print("\n🎉 ALL HAM MODULES ADDED SUCCESSFULLY!")
        print("🚀 VERSALAW2 NOW HAS COMPREHENSIVE HUMAN RIGHTS COVERAGE!")
    else:
        print("\n⚠️  SOME HAM MODULES NEED ATTENTION!")
