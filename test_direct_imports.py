#!/usr/bin/env python3
"""
TEST DIRECT IMPORTS - Avoid __init__.py circular imports
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_direct_imports():
    print("🧪 TEST DIRECT IMPORTS (No __init__.py dependency)")
    print("=" * 60)
    
    tests = [
        # Indonesian Law - import langsung dari submodule
        ("Anti-Corruption", "versalaw2.indonesian_law.specialized_law.anti_corruption", "AntiCorruptionAnalyzer"),
        ("Terrorism Law", "versalaw2.indonesian_law.specialized_law.terrorism_law", "TerrorismLawAnalyzer"),
        
        # International Law - import langsung dari file
        ("International Treaties", "versalaw2.international_law.international_treaties", "InternationalTreatyAnalyzer"),
        ("Diplomatic Law", "versalaw2.international_law.diplomatic_law", "DiplomaticLawAnalyzer"),
        ("Extradition MLAT", "versalaw2.international_law.extradition_mutual_legal", "ExtraditionMLATAnalyzer"),
        ("International Humanitarian", "versalaw2.international_law.international_humanitarian", "InternationalHumanitarianAnalyzer"),
        ("International Trade", "versalaw2.international_law.international_trade", "InternationalTradeAnalyzer"),
        ("Law of the Sea", "versalaw2.international_law.law_of_the_sea", "LawOfTheSeaAnalyzer"),
    ]
    
    successful = 0
    for name, module_path, class_name in tests:
        try:
            module = __import__(module_path, fromlist=[class_name])
            analyzer_class = getattr(module, class_name)
            analyzer = analyzer_class()
            
            # Test basic functionality
            test_data = {}
            result = analyzer.analyze_case(test_data) if hasattr(analyzer, 'analyze_case') else analyzer.analyze(test_data)
            
            print(f"✅ {name}: SUCCESS")
            successful += 1
            
        except Exception as e:
            print(f"❌ {name}: FAILED - {e}")
    
    print(f"\n📊 RESULTS: {successful}/{len(tests)} analyzers working")
    return successful == len(tests)

if __name__ == "__main__":
    success = test_direct_imports()
    if success:
        print("🎉 ALL DIRECT IMPORTS WORKING!")
    else:
        print("⚠️  SOME DIRECT IMPORTS FAILED")
