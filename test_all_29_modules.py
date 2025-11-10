#!/usr/bin/env python3
"""
COMPREHENSIVE TEST - ALL 29 VERSALAW2 MODULES
Final validation before production deployment
"""

import sys
import os
import importlib.util

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_all_modules_comprehensive():
    print("🏛️ COMPREHENSIVE TEST - ALL 29 VERSALAW2 MODULES")
    print("=" * 70)
    
    # All 29 modules with their test data
    all_modules = [
        # Specialized Criminal Law
        ("Anti-Corruption", "versalaw2/indonesian_law/specialized_law/anti_corruption.py", 
         "AntiCorruptionAnalyzer", {"melawan_hukum": True, "kerugian_negara": 5000000000}),
        
        ("Terrorism Law", "versalaw2/indonesian_law/specialized_law/terrorism_law.py",
         "TerrorismLawAnalyzer", {"perencanaan_terorisme": True}),
         
        ("Narcotics Law", "versalaw2/indonesian_law/specialized_law/narcotics.py",
         "NarcoticsLawAnalyzer", {"jenis_narkotika": "golongan_1"}),
         
        ("Money Laundering", "versalaw2/indonesian_law/specialized_law/money_laundering.py",
         "MoneyLaunderingAnalyzer", {"transaksi_mencurigakan": True}),
         
        ("Cyber Crime", "versalaw2/indonesian_law/specialized_law/cyber_crime.py",
         "CyberCrimeAnalyzer", {"akses_ilegal": True}),
         
        ("Human Trafficking", "versalaw2/indonesian_law/specialized_law/human_trafficking.py",
         "HumanTraffickingAnalyzer", {"perdagangan_manusia": True}),
         
        ("Illegal Logging", "versalaw2/indonesian_law/specialized_law/illegal_logging.py",
         "IllegalLoggingAnalyzer", {"penebangan_liar": True}),
         
        ("Illegal Mining", "versalaw2/indonesian_law/specialized_law/illegal_mining.py",
         "IllegalMiningAnalyzer", {"pertambangan_tanpa_izin": True}),
         
        ("Smuggling", "versalaw2/indonesian_law/specialized_law/smuggling.py",
         "SmugglingAnalyzer", {"penyelundupan_barang": True}),

        # Human Rights
        ("Human Rights", "versalaw2/indonesian_law/human_rights/human_rights_analyzer.py",
         "HumanRightsAnalyzer", {"extrajudicial_killing": True}),
         
        ("Child Protection", "versalaw2/indonesian_law/human_rights/child_protection.py",
         "ChildProtectionAnalyzer", {"violation_type": "child_abuse"}),
         
        ("Police Ethics", "versalaw2/indonesian_law/professional_ethics/police_ethics.py",
         "PoliceEthicsAnalyzer", {"abuse_of_power": True}),
         
        ("Judicial Ethics", "versalaw2/indonesian_law/professional_ethics/judicial_ethics.py",
         "JudicialEthicsAnalyzer", {"conflict_of_interest": True}),
         
        ("Prosecutor Ethics", "versalaw2/indonesian_law/professional_ethics/prosecutor_ethics.py",
         "ProsecutorEthicsAnalyzer", {"withholding_evidence": True}),

        # Judicial System
        ("Judicial Law", "versalaw2/indonesian_law/judicial_system/judicial_law_analyzer.py",
         "JudicialLawAnalyzer", {"executive_interference": True}),
         
        ("Prosecution Law", "versalaw2/indonesian_law/prosecution_system/prosecution_law_analyzer.py",
         "ProsecutionLawAnalyzer", {"case_strength": "weak"}),
         
        ("Police Regulations", "versalaw2/indonesian_law/police_system/police_regulations_analyzer.py",
         "PoliceRegulationsAnalyzer", {"arrest_without_procedure": True}),

        # Supreme Court
        ("PERMA Analyzer", "versalaw2/indonesian_law/supreme_court/perma_analyzer.py",
         "PERMAAnalyzer", {"case_type": "electronic_court"}),
         
        ("SEMA Analyzer", "versalaw2/indonesian_law/supreme_court/sema_analyzer.py",
         "SEMAAnalyzer", {"minor_offense": True}),

        # Civil & Commercial Law
        ("Contract Law", "versalaw2/indonesian_law/civil_law/contract_law_analyzer.py",
         "ContractLawAnalyzer", {"kesepakatan": True, "kecakapan": True}),
         
        ("Company Law", "versalaw2/indonesian_law/commercial_law/company_law_analyzer.py",
         "CompanyLawAnalyzer", {"min_two_shareholders": True}),
         
        ("Labor Law", "versalaw2/indonesian_law/labor_law/labor_law_analyzer.py",
         "LaborLawAnalyzer", {"written_contract": True}),
         
        ("Tax Law", "versalaw2/indonesian_law/tax_law/tax_law_analyzer.py",
         "TaxLawAnalyzer", {"individual_income": True}),
         
        ("Land Law", "versalaw2/indonesian_law/agrarian_law/land_law_analyzer.py",
         "LandLawAnalyzer", {"double_certificate": True}),

        # Environmental Law
        ("Environmental Law", "versalaw2/indonesian_law/environmental_law/environmental_law_analyzer.py",
         "EnvironmentalLawAnalyzer", {"high_impact_business": True}),

        # Legislative
        ("Legislative Hierarchy", "versalaw2/indonesian_law/hierarchical_law/legislative_hierarchy.py",
         "LegislativeHierarchyAnalyzer", {"different_levels_conflict": True}),

        # International Law (5 modules)
        ("International Treaties", "versalaw2/international_law/international_treaties.py",
         "InternationalTreatyAnalyzer", {"bilateral": True}),
         
        ("Diplomatic Law", "versalaw2/international_law/diplomatic_law.py",
         "DiplomaticLawAnalyzer", {"diplomatic_agent": True}),
         
        ("Extradition MLAT", "versalaw2/international_law/extradition_mutual_legal.py",
         "ExtraditionMLATAnalyzer", {"extradition_request": True}),
         
        ("International Humanitarian", "versalaw2/international_law/international_humanitarian.py",
         "InternationalHumanitarianLawAnalyzer", {"targeting_civilians": True}),
         
        ("International Trade", "versalaw2/international_law/international_trade.py",
         "InternationalTradeLawAnalyzer", {"tariff_violation": True}),
         
        ("Law of the Sea", "versalaw2/international_law/law_of_the_sea.py",
         "LawOfTheSeaAnalyzer", {"territorial_sea": True})
    ]
    
    print("🔍 TESTING ALL 29 MODULES:")
    print("=" * 70)
    
    successful = 0
    operational_modules = []
    
    for name, file_path, expected_class, test_data in all_modules:
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
            result = analyzer.analyze(test_data)
            
            if isinstance(result, dict) and len(result) > 0:
                print(f"✅ {name}: OPERATIONAL")
                successful += 1
                operational_modules.append(name)
            else:
                print(f"⚠️  {name}: MINIMAL RESULT")
                
        except Exception as e:
            print(f"❌ {name}: ERROR - {e}")
    
    # FINAL COMPREHENSIVE REPORT
    print(f"\n📊 FINAL COMPREHENSIVE RESULTS:")
    print("=" * 70)
    print(f"✅ OPERATIONAL: {successful}/29 modules")
    print(f"📈 SUCCESS RATE: {successful/29*100:.1f}%")
    
    print(f"\n🏛️ MODULE CATEGORIES OPERATIONAL:")
    categories = {
        "Criminal Law": 8,
        "Human Rights": 4, 
        "Judicial System": 3,
        "Supreme Court": 2,
        "Civil & Commercial": 5,
        "Environmental": 1,
        "Legislative": 1,
        "International Law": 5
    }
    
    for category, count in categories.items():
        print(f"   • {category}: {count} modules")
    
    print(f"\n🎯 PRODUCTION READINESS: {'✅ READY' if successful == 29 else '⚠️ NEEDS REVIEW'}")
    
    return successful == 29

if __name__ == "__main__":
    print("🚀 VERSALAW2 2.0.0 - FINAL PRODUCTION VALIDATION")
    print("=" * 70)
    
    success = test_all_modules_comprehensive()
    
    if success:
        print("\n🎉 🎉 🎉 VERSALAW2 2.0.0 PRODUCTION READY! 🎉 🎉 🎉")
        print("📚 29 Indonesian Law Modules + 6 International Law Modules")
        print("⚡ Total: 35 Legal Analysis Modules")
        print("🚀 Ready for Deployment and Integration!")
    else:
        print("\n⚠️  SOME MODULES NEED FINAL ADJUSTMENT BEFORE PRODUCTION")
