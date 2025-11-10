#!/usr/bin/env python3
"""
FINAL COMPLETE TEST - ALL 17 MODULES VERSALAW2 2.0.0
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_all_modules():
    print("🚀 FINAL COMPLETE TEST - VERSALAW2 2.0.0")
    print("=" * 60)
    
    modules = []
    
    # Indonesian Law Modules
    print("\n🇮🇩 TESTING INDONESIAN LAW MODULES (11):")
    print("-" * 40)
    
    indonesian_modules = [
        ("Anti-Corruption", "versalaw2.indonesian_law.specialized_law.anti_corruption", "AntiCorruptionAnalyzer"),
        ("Terrorism Law", "versalaw2.indonesian_law.specialized_law.terrorism_law", "TerrorismLawAnalyzer"),
        ("Narcotics", "versalaw2.indonesian_law.specialized_law.narcotics", "NarcoticsLawAnalyzer"),
        ("Money Laundering", "versalaw2.indonesian_law.specialized_law.money_laundering", "MoneyLaunderingAnalyzer"),
        ("Cyber Crime", "versalaw2.indonesian_law.specialized_law.cyber_crime", "CyberCrimeAnalyzer"),
        ("Human Trafficking", "versalaw2.indonesian_law.specialized_law.human_trafficking", "HumanTraffickingAnalyzer"),
        ("Illegal Logging", "versalaw2.indonesian_law.specialized_law.illegal_logging", "IllegalLoggingAnalyzer"),
        ("Illegal Mining", "versalaw2.indonesian_law.specialized_law.illegal_mining", "IllegalMiningAnalyzer"),
        ("Smuggling", "versalaw2.indonesian_law.specialized_law.smuggling", "SmugglingAnalyzer"),
        ("Legal Ethics", "versalaw2.indonesian_law.professional_ethics.legal_ethics", "LegalEthicsAnalyzer"),
        ("Police Regulations", "versalaw2.indonesian_law.criminal_justice.police_regulations", "PoliceRegulationsAnalyzer"),
    ]
    
    indo_success = 0
    for name, module_path, class_name in indonesian_modules:
        try:
            module = __import__(module_path, fromlist=[class_name])
            analyzer_class = getattr(module, class_name)
            analyzer = analyzer_class()
            
            # Test data sesuai module
            test_data = {"test": True}
            result = analyzer.analyze(test_data)
            
            modules.append((f"🇮🇩 {name}", analyzer_class))
            print(f"✅ {name}")
            indo_success += 1
            
        except Exception as e:
            print(f"❌ {name}: {e}")
    
    # International Law Modules
    print(f"\n🌐 TESTING INTERNATIONAL LAW MODULES (6):")
    print("-" * 40)
    
    international_modules = [
        ("International Treaties", "versalaw2.international_law.international_treaties", "InternationalTreatyAnalyzer"),
        ("Diplomatic Law", "versalaw2.international_law.diplomatic_law", "DiplomaticLawAnalyzer"),
        ("Extradition MLAT", "versalaw2.international_law.extradition_mutual_legal", "ExtraditionMLATAnalyzer"),
        ("International Humanitarian", "versalaw2.international_law.international_humanitarian", "InternationalHumanitarianLawAnalyzer"),
        ("International Trade", "versalaw2.international_law.international_trade", "InternationalTradeLawAnalyzer"),
        ("Law of the Sea", "versalaw2.international_law.law_of_the_sea", "LawOfTheSeaAnalyzer"),
    ]
    
    intl_success = 0
    for name, module_path, class_name in international_modules:
        try:
            module = __import__(module_path, fromlist=[class_name])
            analyzer_class = getattr(module, class_name)
            analyzer = analyzer_class()
            
            test_data = {"test": True}
            result = analyzer.analyze(test_data)
            
            modules.append((f"🌐 {name}", analyzer_class))
            print(f"✅ {name}")
            intl_success += 1
            
        except Exception as e:
            print(f"❌ {name}: {e}")
    
    # Final Summary
    total_modules = len(indonesian_modules) + len(international_modules)
    total_success = indo_success + intl_success
    
    print(f"\n📊 FINAL RESULTS:")
    print("=" * 60)
    print(f"🇮🇩 Indonesian Law: {indo_success}/{len(indonesian_modules)}")
    print(f"🌐 International Law: {intl_success}/{len(international_modules)}")
    print(f"🚀 TOTAL: {total_success}/{total_modules} modules")
    print(f"📈 SUCCESS RATE: {total_success/total_modules*100:.1f}%")
    
    if total_success == total_modules:
        print(f"\n🎉 VERSALAW2 2.0.0 READY FOR PRODUCTION!")
        print("💪 All 17 legal analysis modules operational!")
        return True
    else:
        print(f"\n⚠️  {total_modules - total_success} modules need attention")
        return False

if __name__ == "__main__":
    success = test_all_modules()
    sys.exit(0 if success else 1)
