#!/usr/bin/env python3
"""
TEST INTERNATIONAL LAW - Terpisah dari Indonesian Law
"""

import sys
import os
import importlib.util

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_international_law():
    print("🌐 TEST INTERNATIONAL LAW MODULES")
    print("=" * 60)
    
    test_cases = [
        ("International Treaties", "versalaw2/international_law/international_treaties.py", "InternationalTreatyAnalyzer",
         {"bilateral": True, "mengatur_materi_uu": True}),
        
        ("Diplomatic Law", "versalaw2/international_law/diplomatic_law.py", "DiplomaticLawAnalyzer",
         {"diplomatic_agent": True}),
        
        ("Extradition MLAT", "versalaw2/international_law/extradition_mutual_legal.py", "ExtraditionMLATAnalyzer",
         {"extradition_request": True}),
        
        ("International Humanitarian", "versalaw2/international_law/international_humanitarian.py", "InternationalHumanitarianLawAnalyzer",
         {"targeting_civilians": True}),
        
        ("International Trade", "versalaw2/international_law/international_trade.py", "InternationalTradeLawAnalyzer",
         {"tariff_violation": True}),
        
        ("Law of the Sea", "versalaw2/international_law/law_of_the_sea.py", "LawOfTheSeaAnalyzer",
         {"territorial_sea": True}),
    ]
    
    successful = 0
    for name, file_path, expected_class, test_data in test_cases:
        try:
            # Import langsung dari file
            spec = importlib.util.spec_from_file_location("module.name", file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Cari class
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
            result = analyzer.analyze(test_data) if hasattr(analyzer, 'analyze') else analyzer.analyze_case(test_data)
            
            print(f"✅ {name}: WORKING")
            successful += 1
            
        except Exception as e:
            print(f"❌ {name}: FAILED - {e}")
    
    print(f"\n📊 RESULTS: {successful}/{len(test_cases)} international modules working")
    return successful

if __name__ == "__main__":
    count = test_international_law()
    if count > 0:
        print(f"🎉 {count} INTERNATIONAL LAW MODULES BERFUNGSI!")
    else:
        print("💥 TIDAK ADA INTERNATIONAL MODULE YANG BERFUNGSI!")
