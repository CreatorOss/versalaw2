#!/usr/bin/env python3
"""
Test Fixed International Law Modules
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    print("🔍 TESTING FIXED INTERNATIONAL LAW MODULES...")
    
    # Test international treaties first
    from versalaw2.international_law.international_treaties import InternationalTreatyAnalyzer
    print("✅ InternationalTreatyAnalyzer imported successfully!")
    
    treaty_analyzer = InternationalTreatyAnalyzer()
    treaty_test = treaty_analyzer.analyze_treaty_ratification({"bilateral": True})
    print(f"✅ Treaty analysis working: {len(treaty_test)} aspects")
    
    # Test other international modules
    from versalaw2.international_law.diplomatic_law import DiplomaticLawAnalyzer
    from versalaw2.international_law.law_of_the_sea import LawOfTheSeaAnalyzer
    from versalaw2.international_law.international_humanitarian import InternationalHumanitarianAnalyzer
    from versalaw2.international_law.international_trade import InternationalTradeAnalyzer
    from versalaw2.international_law.extradition_mutual_legal import ExtraditionMLATAnalyzer
    
    print("✅ All international law modules imported successfully!")
    
    # Test instantiation
    diplomatic_analyzer = DiplomaticLawAnalyzer()
    sea_law_analyzer = LawOfTheSeaAnalyzer()
    humanitarian_analyzer = InternationalHumanitarianAnalyzer()
    trade_analyzer = InternationalTradeAnalyzer()
    extradition_analyzer = ExtraditionMLATAnalyzer()
    
    print("✅ All international analyzers instantiated!")
    
    # Quick functionality test
    diplomatic_test = diplomatic_analyzer.analyze_diplomatic_incident({})
    sea_test = sea_law_analyzer.analyze_maritime_dispute({})
    humanitarian_test = humanitarian_analyzer.analyze_armed_conflict({})
    trade_test = trade_analyzer.analyze_trade_dispute({})
    extradition_test = extradition_analyzer.analyze_extradition_request({})
    
    print(f"✅ Diplomatic analysis: {len(diplomatic_test)} aspects")
    print(f"✅ Law of Sea analysis: {len(sea_test)} aspects")
    print(f"✅ Humanitarian analysis: {len(humanitarian_test)} aspects")
    print(f"✅ Trade analysis: {len(trade_test)} aspects")
    print(f"✅ Extradition analysis: {len(extradition_test)} aspects")
    
    print("\n🎯 ALL 6 INTERNATIONAL LAW MODULES OPERATIONAL!")
    
except ImportError as e:
    print(f"❌ IMPORT ERROR: {e}")
    import traceback
    traceback.print_exc()
except Exception as e:
    print(f"❌ FUNCTIONALITY ERROR: {e}")
    import traceback
    traceback.print_exc()
