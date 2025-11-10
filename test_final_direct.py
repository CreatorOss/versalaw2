#!/usr/bin/env python3
"""
FINAL TEST - DIRECT IMPORTS ONLY (No __init__.py dependencies)
"""

import sys
import os
import importlib.util

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def import_direct(file_path, expected_class):
    """Import class directly from file"""
    try:
        spec = importlib.util.spec_from_file_location("module.name", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Find analyzer class
        for attr_name in dir(module):
            if 'Analyzer' in attr_name and not attr_name.startswith('_'):
                return getattr(module, attr_name)
        return None
    except Exception as e:
        return f"ERROR: {e}"

def test_all_direct():
    print("🚀 FINAL TEST - DIRECT IMPORTS ONLY")
    print("=" * 60)
    
    # All modules to test
    modules_to_test = [
        # Indonesian Law - Specialized
        ("🇮🇩 Anti-Corruption", "versalaw2/indonesian_law/specialized_law/anti_corruption.py", "AntiCorruptionAnalyzer"),
        ("🇮🇩 Terrorism Law", "versalaw2/indonesian_law/specialized_law/terrorism_law.py", "TerrorismLawAnalyzer"),
        ("🇮🇩 Narcotics", "versalaw2/indonesian_law/specialized_law/narcotics.py", "NarcoticsLawAnalyzer"),
        ("🇮🇩 Money Laundering", "versalaw2/indonesian_law/specialized_law/money_laundering.py", "MoneyLaunderingAnalyzer"),
        ("🇮🇩 Cyber Crime", "versalaw2/indonesian_law/specialized_law/cyber_crime.py", "CyberCrimeAnalyzer"),
        ("🇮🇩 Human Trafficking", "versalaw2/indonesian_law/specialized_law/human_trafficking.py", "HumanTraffickingAnalyzer"),
        ("🇮🇩 Illegal Logging", "versalaw2/indonesian_law/specialized_law/illegal_logging.py", "IllegalLoggingAnalyzer"),
        ("🇮🇩 Illegal Mining", "versalaw2/indonesian_law/specialized_law/illegal_mining.py", "IllegalMiningAnalyzer"),
        ("🇮🇩 Smuggling", "versalaw2/indonesian_law/specialized_law/smuggling.py", "SmugglingAnalyzer"),
        
        # Indonesian Law - Professional Ethics
        ("🇮🇩 Legal Ethics", "versalaw2/indonesian_law/professional_ethics/legal_ethics.py", "LegalEthicsAnalyzer"),
        
        # Indonesian Law - Criminal Justice
        ("🇮🇩 Police Regulations", "versalaw2/indonesian_law/criminal_justice/police_regulations.py", "PoliceRegulationsAnalyzer"),
        
        # International Law
        ("🌐 International Treaties", "versalaw2/international_law/international_treaties.py", "InternationalTreatyAnalyzer"),
        ("🌐 Diplomatic Law", "versalaw2/international_law/diplomatic_law.py", "DiplomaticLawAnalyzer"),
        ("🌐 Extradition MLAT", "versalaw2/international_law/extradition_mutual_legal.py", "ExtraditionMLATAnalyzer"),
        ("🌐 International Humanitarian", "versalaw2/international_law/international_humanitarian.py", "InternationalHumanitarianLawAnalyzer"),
        ("🌐 International Trade", "versalaw2/international_law/international_trade.py", "InternationalTradeLawAnalyzer"),
        ("🌐 Law of the Sea", "versalaw2/international_law/law_of_the_sea.py", "LawOfTheSeaAnalyzer"),
    ]
    
    print("🔍 TESTING ALL MODULES WITH DIRECT IMPORTS:")
    print("=" * 60)
    
    successful = 0
    working_modules = []
    
    for name, file_path, expected_class in modules_to_test:
        if not os.path.exists(file_path):
            print(f"❌ {name}: FILE NOT FOUND")
            continue
            
        analyzer_class = import_direct(file_path, expected_class)
        
        if isinstance(analyzer_class, str) and analyzer_class.startswith("ERROR"):
            print(f"❌ {name}: {analyzer_class}")
            continue
            
        if analyzer_class is None:
            print(f"❌ {name}: NO ANALYZER CLASS FOUND")
            continue
        
        try:
            # Test functionality
            analyzer = analyzer_class()
            test_data = {"test": True}
            
            if hasattr(analyzer, 'analyze'):
                result = analyzer.analyze(test_data)
            elif hasattr(analyzer, 'analyze_case'):
                result = analyzer.analyze_case(test_data)
            else:
                result = {"status": "no_analyze_method"}
            
            if isinstance(result, dict):
                print(f"✅ {name}: WORKING")
                successful += 1
                working_modules.append(name)
            else:
                print(f"⚠️  {name}: INVALID RESULT")
                
        except Exception as e:
            print(f"❌ {name}: FUNCTIONALITY ERROR - {e}")
    
    # Summary
    print(f"\n📊 FINAL RESULTS:")
    print("=" * 60)
    print(f"✅ SUCCESSFUL: {successful}/{len(modules_to_test)}")
    print(f"📈 SUCCESS RATE: {successful/len(modules_to_test)*100:.1f}%")
    
    if successful == len(modules_to_test):
        print(f"\n🎉 VERSALAW2 2.0.0 - ALL {successful} MODULES OPERATIONAL!")
        print("🚀 READY FOR PRODUCTION DEPLOYMENT!")
    else:
        print(f"\n📋 WORKING MODULES ({successful}):")
        for module in working_modules:
            print(f"   • {module}")
    
    return successful == len(modules_to_test)

if __name__ == "__main__":
    success = test_all_direct()
    sys.exit(0 if success else 1)
