#!/usr/bin/env python3
"""
TEST CURRENT FUNCTIONALITY - Ensure everything works with current structure
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_all_analyzers():
    """Test all analyzer classes with current structure"""
    print("🧪 TEST ALL ANALYZERS WITH CURRENT STRUCTURE")
    print("=" * 60)
    
    tests = [
        # Indonesian Law
        ("Anti-Corruption", "versalaw2.indonesian_law.specialized_law.anti_corruption", "AntiCorruptionAnalyzer"),
        ("Terrorism Law", "versalaw2.indonesian_law.specialized_law.terrorism_law", "TerrorismLawAnalyzer"),
        
        # International Law 
        ("International Treaties", "versalaw2.international_law.international_treaties", "InternationalTreatyAnalyzer"),
        ("Diplomatic Law", "versalaw2.international_law.diplomatic_law", "DiplomaticLawAnalyzer"),
        ("Extradition MLAT", "versalaw2.international_law.extradition_mutual_legal", "ExtraditionMLATAnalyzer"),
        ("International Humanitarian", "versalaw2.international_law.international_humanitarian", "InternationalHumanitarianLawAnalyzer"),
        ("International Trade", "versalaw2.international_law.international_trade", "InternationalTradeLawAnalyzer"),
        ("Law of the Sea", "versalaw2.international_law.law_of_the_sea", "LawOfTheSeaAnalyzer"),
    ]
    
    successful = 0
    for test_name, module_path, class_name in tests:
        try:
            # Dynamic import
            module = __import__(module_path, fromlist=[class_name])
            analyzer_class = getattr(module, class_name)
            analyzer = analyzer_class()
            
            # Test basic method
            test_data = {}
            if hasattr(analyzer, 'analyze'):
                result = analyzer.analyze(test_data)
            elif hasattr(analyzer, 'analyze_case'):
                result = analyzer.analyze_case(test_data)
            else:
                # Find any analyze method
                methods = [m for m in dir(analyzer) if m.startswith('analyze') and callable(getattr(analyzer, m))]
                if methods:
                    result = getattr(analyzer, methods[0])(test_data)
                else:
                    result = {"status": "no_analyze_method"}
            
            print(f"✅ {test_name}: SUCCESS")
            successful += 1
            
        except Exception as e:
            print(f"❌ {test_name}: FAILED - {e}")
    
    print(f"\n📊 RESULTS: {successful}/{len(tests)} analyzers working")
    return successful == len(tests)

if __name__ == "__main__":
    success = test_all_analyzers()
    if success:
        print("\n🎉 ALL ANALYZERS WORKING WITH CURRENT STRUCTURE!")
    else:
        print("\n⚠️  SOME ANALYZERS HAVE ISSUES - CHECK BEFORE MODIFYING STRUCTURE")
