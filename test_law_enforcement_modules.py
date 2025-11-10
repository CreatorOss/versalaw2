#!/usr/bin/env python3
"""
TEST LAW ENFORCEMENT INSTITUTIONS MODULES
"""

import sys
import os
import importlib.util

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_law_enforcement_modules():
    print("🧪 TEST LAW ENFORCEMENT INSTITUTIONS MODULES")
    print("=" * 60)
    
    enforcement_modules = [
        # Judicial System
        ("Judicial Law Analyzer", "versalaw2/indonesian_law/judicial_system/judicial_law_analyzer.py", "JudicialLawAnalyzer"),
        
        # Prosecution System  
        ("Prosecution Law Analyzer", "versalaw2/indonesian_law/prosecution_system/prosecution_law_analyzer.py", "ProsecutionLawAnalyzer"),
        
        # Police System
        ("Police Regulations Analyzer", "versalaw2/indonesian_law/police_system/police_regulations_analyzer.py", "PoliceRegulationsAnalyzer"),
    ]
    
    print("🔍 TESTING LAW ENFORCEMENT MODULES:")
    print("=" * 60)
    
    successful = 0
    for name, file_path, expected_class in enforcement_modules:
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
            
            # Test functionality with appropriate data
            analyzer = analyzer_class()
            
            if "Judicial" in name:
                test_data = {"executive_interference": True}
            elif "Prosecution" in name:
                test_data = {"case_strength": "weak", "public_interest": "low"}
            elif "Police" in name:
                test_data = {"arrest_without_procedure": True}
            else:
                test_data = {"test": True}
                
            result = analyzer.analyze(test_data)
            
            print(f"✅ {name}: WORKING")
            successful += 1
            
        except Exception as e:
            print(f"❌ {name}: ERROR - {e}")
    
    print(f"\n📊 RESULTS: {successful}/{len(enforcement_modules)} law enforcement modules working")
    
    # Update total count - previous 20 + 3 new modules
    total_indonesian = 20 + successful
    print(f"🇮🇩 TOTAL INDONESIAN LAW MODULES: {total_indonesian}")
    
    return successful == len(enforcement_modules)

if __name__ == "__main__":
    success = test_law_enforcement_modules()
    if success:
        print("\n🎉 ALL LAW ENFORCEMENT MODULES ADDED SUCCESSFULLY!")
        print("🚀 VERSALAW2 NOW HAS COMPREHENSIVE LAW ENFORCEMENT COVERAGE!")
        print("📋 COVERING: Judiciary, Prosecution, and Police Systems")
    else:
        print("\n⚠️  SOME LAW ENFORCEMENT MODULES NEED ATTENTION!")
