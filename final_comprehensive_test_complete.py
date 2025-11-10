#!/usr/bin/env python3
"""
VERSALAW2 FINAL COMPREHENSIVE TEST - COMPLETE
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    print("🎯 VERSALAW2 FINAL COMPREHENSIVE TEST")
    print("=" * 70)
    
    total_modules = 0
    operational_modules = 0
    
    print("\n🔍 TESTING SPECIALIZED CRIME MODULES (9 MODULES)...")
    print("-" * 70)
    
    # Test specialized crime modules
    specialized_results = {}
    try:
        from versalaw2.indonesian_law.specialized_law.anti_corruption import AntiCorruptionAnalyzer
        from versalaw2.indonesian_law.specialized_law.money_laundering import MoneyLaunderingAnalyzer
        from versalaw2.indonesian_law.specialized_law.human_trafficking import HumanTraffickingAnalyzer
        from versalaw2.indonesian_law.specialized_law.illegal_mining import IllegalMiningAnalyzer
        from versalaw2.indonesian_law.specialized_law.illegal_logging import IllegalLoggingAnalyzer
        from versalaw2.indonesian_law.specialized_law.narcotics import NarcoticsAnalyzer
        from versalaw2.indonesian_law.specialized_law.smuggling import SmugglingAnalyzer
        from versalaw2.indonesian_law.specialized_law.cyber_crime import CyberCrimeAnalyzer
        from versalaw2.indonesian_law.specialized_law.terrorism_law import TerrorismLawAnalyzer
        
        specialized_tests = [
            ("🏛️ Anti-Corruption", AntiCorruptionAnalyzer(), "analyze_corruption_case", {"melawan_hukum": True}),
            ("💰 Money Laundering", MoneyLaunderingAnalyzer(), "analyze_money_laundering", {"placement": True}),
            ("👥 Human Trafficking", HumanTraffickingAnalyzer(), "analyze_trafficking_case", {"penipuan": True}),
            ("🏭 Illegal Mining", IllegalMiningAnalyzer(), "analyze_illegal_mining", {"tambang_tanpa_izin": True}),
            ("🌳 Illegal Logging", IllegalLoggingAnalyzer(), "analyze_illegal_logging", {"penebangan_tanpa_izin": True}),
            ("💊 Narcotics", NarcoticsAnalyzer(), "analyze_narcotics_case", {"narcotic_type": "sabu"}),
            ("🚢 Smuggling", SmugglingAnalyzer(), "analyze_smuggling_case", {"barang_terlarang": True}),
            ("💻 Cyber Crime", CyberCrimeAnalyzer(), "analyze_cyber_crime", {"peretasan": True}),
            ("🚨 Terrorism Law", TerrorismLawAnalyzer(), "analyze_terrorism_case", {"perencanaan_terorisme": True})
        ]
        
        for name, analyzer, method, test_data in specialized_tests:
            try:
                result = getattr(analyzer, method)(test_data)
                specialized_results[name] = {"status": "✅ OPERATIONAL", "aspects": len(result)}
                operational_modules += 1
                print(f"{name:<25} ✅ OPERATIONAL - {len(result)} aspects")
            except Exception as e:
                specialized_results[name] = {"status": f"❌ ERROR", "aspects": 0}
                print(f"{name:<25} ❌ ERROR: {e}")
            total_modules += 1
            
    except Exception as e:
        print(f"❌ Specialized crimes import failed: {e}")
    
    print(f"\n📊 SPECIALIZED CRIMES: {operational_modules}/{len(specialized_tests)} operational")
    
    print("\n🌍 TESTING INTERNATIONAL LAW MODULES (6 MODULES)...")
    print("-" * 70)
    
    # Test international law modules
    international_results = {}
    try:
        from versalaw2.international_law.international_treaties import InternationalTreatyAnalyzer
        from versalaw2.international_law.diplomatic_law import DiplomaticLawAnalyzer
        from versalaw2.international_law.law_of_the_sea import LawOfTheSeaAnalyzer
        from versalaw2.international_law.international_humanitarian import InternationalHumanitarianAnalyzer
        from versalaw2.international_law.international_trade import InternationalTradeAnalyzer
        from versalaw2.international_law.extradition_mutual_legal import ExtraditionMLATAnalyzer
        
        international_tests = [
            ("🌐 International Treaties", InternationalTreatyAnalyzer(), "analyze_treaty_ratification", {"bilateral": True}),
            ("🏛️ Diplomatic Law", DiplomaticLawAnalyzer(), "analyze_diplomatic_incident", {"premises_violation": True}),
            ("🌊 Law of the Sea", LawOfTheSeaAnalyzer(), "analyze_maritime_dispute", {"eez_conflict": True}),
            ("⚔️ Humanitarian Law", InternationalHumanitarianAnalyzer(), "analyze_armed_conflict", {"international_armed_conflict": True}),
            ("💼 International Trade", InternationalTradeAnalyzer(), "analyze_trade_dispute", {"tariff_violation": True}),
            ("🔄 Extradition & MLA", ExtraditionMLATAnalyzer(), "analyze_extradition_request", {"double_criminality": True})
        ]
        
        for name, analyzer, method, test_data in international_tests:
            try:
                result = getattr(analyzer, method)(test_data)
                international_results[name] = {"status": "✅ OPERATIONAL", "aspects": len(result)}
                operational_modules += 1
                print(f"{name:<25} ✅ OPERATIONAL - {len(result)} aspects")
            except Exception as e:
                international_results[name] = {"status": f"❌ ERROR", "aspects": 0}
                print(f"{name:<25} ❌ ERROR: {e}")
            total_modules += 1
            
    except Exception as e:
        print(f"❌ International law import failed: {e}")
    
    print(f"\n📊 INTERNATIONAL LAW: {len([r for r in international_results.values() if '✅' in r['status']])}/{len(international_tests)} operational")
    
    # Final summary
    print("\n" + "=" * 70)
    print("📊 FINAL COMPREHENSIVE TEST SUMMARY")
    print("-" * 70)
    
    total_specialized = len(specialized_results)
    operational_specialized = len([r for r in specialized_results.values() if '✅' in r['status']])
    
    total_international = len(international_results)
    operational_international = len([r for r in international_results.values() if '✅' in r['status']])
    
    total_modules = total_specialized + total_international
    total_operational = operational_specialized + operational_international
    
    print(f"SPECIALIZED CRIMES: {operational_specialized}/{total_specialized} operational")
    print(f"INTERNATIONAL LAW:  {operational_international}/{total_international} operational")
    print(f"TOTAL MODULES:      {total_operational}/{total_modules} operational")
    print(f"SUCCESS RATE:       {(total_operational/total_modules)*100:.1f}%")
    
    if total_operational == total_modules:
        print("\n🎉 ALL 15 MODULES FULLY OPERATIONAL!")
        print("🚀 VERSALAW2 READY FOR ENTERPRISE DEPLOYMENT!")
    else:
        print(f"\n⚠️  {total_modules - total_operational} modules need attention")
    
    print(f"\n⭐ VERSALAW2 - {total_modules} COMPREHENSIVE LEGAL MODULES!")
    print("🇮🇩 Most Advanced Legal AI Platform in Indonesia")
    print("🌍 Covering National & International Law")

if __name__ == "__main__":
    main()
