#!/usr/bin/env python3
"""
TEST EXTENDED MODULES - Module hukum Indonesia yang diperluas
"""

import sys
import os
import importlib.util

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_extended_modules():
    print("🧪 TEST EXTENDED INDONESIAN LAW MODULES")
    print("=" * 60)
    
    new_modules = [
        # Hierarchical Law
        ("Legislative Hierarchy", "versalaw2/indonesian_law/hierarchical_law/legislative_hierarchy.py", "LegislativeHierarchyAnalyzer"),
        
        # Professional Ethics - Extended
        ("Police Ethics", "versalaw2/indonesian_law/professional_ethics/police_ethics.py", "PoliceEthicsAnalyzer"),
        ("Judicial Ethics", "versalaw2/indonesian_law/professional_ethics/judicial_ethics.py", "JudicialEthicsAnalyzer"),
        ("Prosecutor Ethics", "versalaw2/indonesian_law/professional_ethics/prosecutor_ethics.py", "ProsecutorEthicsAnalyzer"),
        
        # Supreme Court Regulations
        ("PERMA Analyzer", "versalaw2/indonesian_law/supreme_court/perma_analyzer.py", "PERMAAnalyzer"),
        ("SEMA Analyzer", "versalaw2/indonesian_law/supreme_court/sema_analyzer.py", "SEMAAnalyzer"),
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
            test_data = {"test": True}
            result = analyzer.analyze(test_data)
            
            print(f"✅ {name}: WORKING")
            successful += 1
            
        except Exception as e:
            print(f"❌ {name}: ERROR - {e}")
    
    print(f"\n📊 RESULTS: {successful}/{len(new_modules)} new modules working")
    
    # Total modules count
    total_indonesian = 11 + successful  # Original 11 + new modules
    print(f"🇮🇩 TOTAL INDONESIAN LAW MODULES: {total_indonesian}")
    
    return successful == len(new_modules)

if __name__ == "__main__":
    success = test_extended_modules()
    if success:
        print("\n🎉 ALL NEW MODULES ADDED SUCCESSFULLY!")
    else:
        print("\n⚠️  SOME NEW MODULES NEED ATTENTION!")
