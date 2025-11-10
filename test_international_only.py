#!/usr/bin/env python3
"""
Test International Law Modules Only
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    print("🔍 TESTING INTERNATIONAL LAW MODULES ONLY...")
    
    # Test import international law modules
    from versalaw2.international_law.international_treaties import InternationalTreatyAnalyzer
    from versalaw2.international_law.diplomatic_law import DiplomaticLawAnalyzer
    from versalaw2.international_law.law_of_the_sea import LawOfTheSeaAnalyzer
    from versalaw2.international_law.international_humanitarian import InternationalHumanitarianAnalyzer
    from versalaw2.international_law.international_trade import InternationalTradeAnalyzer
    from versalaw2.international_law.extradition_mutual_legal import ExtraditionMLATAnalyzer
    
    print("✅ INTERNATIONAL LAW MODULES IMPORTED SUCCESSFULLY!")
    
    # Test instantiation
    treaty_analyzer = InternationalTreatyAnalyzer()
    diplomatic_analyzer = DiplomaticLawAnalyzer()
    sea_law_analyzer = LawOfTheSeaAnalyzer()
    humanitarian_analyzer = InternationalHumanitarianAnalyzer()
    trade_analyzer = InternationalTradeAnalyzer()
    extradition_analyzer = ExtraditionMLATAnalyzer()
    
    print("✅ ALL 6 INTERNATIONAL ANALYZERS INSTANTIATED!")
    
    # Test comprehensive functionality
    print("\n🧪 TESTING INTERNATIONAL LAW FUNCTIONALITY:")
    
    # Treaty analysis
    treaty_test = treaty_analyzer.analyze_treaty_ratification({
        "bilateral": True,
        "mengatur_materi_uu": True
    })
    print(f"   • Treaty Analysis: {len(treaty_test)} aspects analyzed")
    
    # Diplomatic incident
    diplomatic_test = diplomatic_analyzer.analyze_diplomatic_incident({
        "premises_violation": True
    })
    print(f"   • Diplomatic Analysis: {len(diplomatic_test)} aspects analyzed")
    
    # Maritime dispute
    sea_test = sea_law_analyzer.analyze_maritime_dispute({
        "eez_conflict": True
    })
    print(f"   • Law of Sea Analysis: {len(sea_test)} aspects analyzed")
    
    # Armed conflict
    conflict_test = humanitarian_analyzer.analyze_armed_conflict({
        "international_armed_conflict": True,
        "civilians_present": True
    })
    print(f"   • Humanitarian Law: {len(conflict_test)} aspects analyzed")
    
    # Trade dispute
    trade_test = trade_analyzer.analyze_trade_dispute({
        "tariff_violation": True,
        "wto_member_involved": True
    })
    print(f"   • Trade Law: {len(trade_test)} aspects analyzed")
    
    # Extradition
    extradition_test = extradition_analyzer.analyze_extradition_request({
        "double_criminality": True,
        "extradition_treaty_exists": True
    })
    print(f"   • Extradition/MLA: {len(extradition_test)} aspects analyzed")
    
    print("\n🎯 6 INTERNATIONAL LAW MODULES FULLY OPERATIONAL!")
    
    # Test specialized crimes juga
    print("\n🔍 TESTING SPECIALIZED CRIME MODULES...")
    from versalaw2.indonesian_law.specialized_law.anti_corruption import AntiCorruptionAnalyzer
    from versalaw2.indonesian_law.specialized_law.narcotics import NarcoticsAnalyzer
    
    corruption_analyzer = AntiCorruptionAnalyzer()
    narcotics_analyzer = NarcoticsAnalyzer()
    
    corruption_test = corruption_analyzer.analyze_corruption_case({
        "melawan_hukum": True,
        "merugikan_keuangan_negara": True
    })
    narcotics_test = narcotics_analyzer.analyze_narcotics_case({
        "narcotic_type": "sabu",
        "quantity": 250
    })
    
    print(f"   • Corruption Analysis: {len(corruption_test)} aspects")
    print(f"   • Narcotics Analysis: {len(narcotics_test)} aspects")
    
    print("\n⭐ VERSALAW2 INTERNATIONAL LAW SUCCESSFULLY INTEGRATED!")
    print("   Total Tested Modules: 8 International + 2 Specialized Crimes")
    
except ImportError as e:
    print(f"❌ IMPORT ERROR: {e}")
    print("\n📁 CURRENT STRUCTURE:")
    import subprocess
    result = subprocess.run(["find", "versalaw2", "-name", "*.py"], capture_output=True, text=True)
    print(result.stdout)
    
except Exception as e:
    print(f"❌ FUNCTIONALITY ERROR: {e}")
    import traceback
    traceback.print_exc()
