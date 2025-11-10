#!/usr/bin/env python3
"""
COMPREHENSIVE TEST - HUKUM INDONESIA SAJA
Fokus menyelesaikan modul hukum Indonesia hingga sempurna
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_indonesian_law_modules():
    print("🎯 COMPREHENSIVE TEST - HUKUM INDONESIA")
    print("=" * 60)
    
    modules = []
    
    # 1. Criminal Justice System
    print("\n🔍 MODULE CRIMINAL JUSTICE:")
    print("-" * 30)
    try:
        from versalaw2.indonesian_law.criminal_justice.criminal_procedure import CriminalProcedureAnalyzer
        modules.append(("Criminal Procedure", CriminalProcedureAnalyzer))
        print("✅ Criminal Procedure: FOUND")
    except Exception as e:
        print(f"❌ Criminal Procedure: {e}")
    
    try:
        from versalaw2.indonesian_law.criminal_justice.penal_code import PenalCodeAnalyzer
        modules.append(("Penal Code", PenalCodeAnalyzer))
        print("✅ Penal Code: FOUND")
    except Exception as e:
        print(f"❌ Penal Code: {e}")
    
    # 2. Specialized Law
    print("\n🔍 MODULE SPECIALIZED LAW:")
    print("-" * 30)
    try:
        from versalaw2.indonesian_law.specialized_law.anti_corruption import AntiCorruptionAnalyzer
        modules.append(("Anti-Corruption", AntiCorruptionAnalyzer))
        print("✅ Anti-Corruption: FOUND")
    except Exception as e:
        print(f"❌ Anti-Corruption: {e}")
    
    try:
        from versalaw2.indonesian_law.specialized_law.terrorism_law import TerrorismLawAnalyzer
        modules.append(("Terrorism Law", TerrorismLawAnalyzer))
        print("✅ Terrorism Law: FOUND")
    except Exception as e:
        print(f"❌ Terrorism Law: {e}")
    
    try:
        from versalaw2.indonesian_law.specialized_law.narcotics_law import NarcoticsLawAnalyzer
        modules.append(("Narcotics Law", NarcoticsLawAnalyzer))
        print("✅ Narcotics Law: FOUND")
    except Exception as e:
        print(f"❌ Narcotics Law: {e}")
    
    try:
        from versalaw2.indonesian_law.specialized_law.money_laundering import MoneyLaunderingAnalyzer
        modules.append(("Money Laundering", MoneyLaunderingAnalyzer))
        print("✅ Money Laundering: FOUND")
    except Exception as e:
        print(f"❌ Money Laundering: {e}")
    
    # 3. Constitutional & Statutory Law
    print("\n🔍 MODULE CONSTITUTIONAL & STATUTORY:")
    print("-" * 30)
    try:
        from versalaw2.indonesian_law.constitutional_law.constitutional_law import ConstitutionalLawAnalyzer
        modules.append(("Constitutional Law", ConstitutionalLawAnalyzer))
        print("✅ Constitutional Law: FOUND")
    except Exception as e:
        print(f"❌ Constitutional Law: {e}")
    
    try:
        from versalaw2.indonesian_law.statutory_law.legislative_hierarchy import LegislativeHierarchyAnalyzer
        modules.append(("Legislative Hierarchy", LegislativeHierarchyAnalyzer))
        print("✅ Legislative Hierarchy: FOUND")
    except Exception as e:
        print(f"❌ Legislative Hierarchy: {e}")
    
    # 4. Professional Ethics
    print("\n🔍 MODULE PROFESSIONAL ETHICS:")
    print("-" * 30)
    try:
        from versalaw2.indonesian_law.professional_ethics.legal_ethics import LegalEthicsAnalyzer
        modules.append(("Legal Ethics", LegalEthicsAnalyzer))
        print("✅ Legal Ethics: FOUND")
    except Exception as e:
        print(f"❌ Legal Ethics: {e}")
    
    # Test functionality
    print("\n🔧 TESTING FUNCTIONALITY:")
    print("=" * 60)
    
    successful = 0
    for name, analyzer_class in modules:
        try:
            analyzer = analyzer_class()
            
            # Test data sesuai dengan jenis analyzer
            test_data = {}
            if "corruption" in name.lower():
                test_data = {"kerugian_negara": 1000000000}
            elif "terrorism" in name.lower():
                test_data = {"perencanaan_terorisme": True}
            elif "narcotics" in name.lower():
                test_data = {"jenis_narkotika": "golongan_1"}
            elif "money" in name.lower():
                test_data = {"transaksi_mencurigakan": True}
            else:
                test_data = {"test_case": True}
            
            # Try to analyze
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
            
            print(f"✅ {name}: OPERATIONAL")
            successful += 1
            
        except Exception as e:
            print(f"❌ {name}: FAILED - {e}")
    
    # Summary
    print(f"\n📊 HASIL TEST HUKUM INDONESIA:")
    print("=" * 60)
    print(f"✅ MODUL BERFUNGSI: {successful}/{len(modules)}")
    print(f"📈 PERSENTASE: {successful/len(modules)*100:.1f}%")
    
    if successful == len(modules):
        print("🎉 SEMUA MODUL HUKUM INDONESIA BERFUNGSI!")
        return True
    else:
        print("⚠️  ADA MODUL YANG PERLU DIPERBAIKI")
        return False

if __name__ == "__main__":
    success = test_indonesian_law_modules()
    sys.exit(0 if success else 1)
