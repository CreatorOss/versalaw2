#!/usr/bin/env python3
"""
TEST RAW FILES - Import langsung tanpa melalui __init__.py
"""

import sys
import os
import importlib.util

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def import_directly(file_path, class_name):
    """Import class langsung dari file"""
    try:
        spec = importlib.util.spec_from_file_location("module.name", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Cari class
        if hasattr(module, class_name):
            return getattr(module, class_name)
        else:
            # Cari class yang mengandung 'Analyzer'
            for attr_name in dir(module):
                if 'Analyzer' in attr_name and not attr_name.startswith('_'):
                    return getattr(module, attr_name)
            return None
    except Exception as e:
        return f"ERROR: {e}"

def test_raw_files():
    print("🎯 TEST RAW FILE IMPORTS - HUKUM INDONESIA")
    print("=" * 60)
    
    test_cases = [
        # Specialized Law
        ("Anti-Corruption", "versalaw2/indonesian_law/specialized_law/anti_corruption.py", "AntiCorruptionAnalyzer"),
        ("Terrorism Law", "versalaw2/indonesian_law/specialized_law/terrorism_law.py", "TerrorismLawAnalyzer"),
        ("Narcotics", "versalaw2/indonesian_law/specialized_law/narcotics.py", "NarcoticsLawAnalyzer"),
        ("Money Laundering", "versalaw2/indonesian_law/specialized_law/money_laundering.py", "MoneyLaunderingAnalyzer"),
        ("Cyber Crime", "versalaw2/indonesian_law/specialized_law/cyber_crime.py", "CyberCrimeAnalyzer"),
        ("Human Trafficking", "versalaw2/indonesian_law/specialized_law/human_trafficking.py", "HumanTraffickingAnalyzer"),
        ("Illegal Logging", "versalaw2/indonesian_law/specialized_law/illegal_logging.py", "IllegalLoggingAnalyzer"),
        ("Illegal Mining", "versalaw2/indonesian_law/specialized_law/illegal_mining.py", "IllegalMiningAnalyzer"),
        ("Smuggling", "versalaw2/indonesian_law/specialized_law/smuggling.py", "SmugglingAnalyzer"),
        
        # Professional Ethics
        ("Legal Ethics", "versalaw2/indonesian_law/professional_ethics/legal_ethics.py", "LegalEthicsAnalyzer"),
        
        # Criminal Justice
        ("Police Regulations", "versalaw2/indonesian_law/criminal_justice/police_regulations.py", "PoliceRegulationsAnalyzer"),
    ]
    
    print("🔍 CHECKING FILE EXISTENCE:")
    print("-" * 30)
    
    existing_files = []
    for name, file_path, expected_class in test_cases:
        if os.path.exists(file_path):
            existing_files.append((name, file_path, expected_class))
            print(f"✅ {name}: FILE EXISTS")
        else:
            print(f"❌ {name}: FILE NOT FOUND")
    
    print(f"\n🔧 TESTING {len(existing_files)} FILES:")
    print("=" * 60)
    
    working_analyzers = []
    for name, file_path, expected_class in existing_files:
        try:
            # Import langsung dari file
            analyzer_class = import_directly(file_path, expected_class)
            
            if isinstance(analyzer_class, str) and analyzer_class.startswith("ERROR"):
                print(f"❌ {name}: IMPORT FAILED - {analyzer_class}")
                continue
                
            if analyzer_class is None:
                print(f"❌ {name}: NO ANALYZER CLASS FOUND")
                continue
            
            # Test instantiation dan functionality
            analyzer = analyzer_class()
            test_data = {"test": True}
            
            # Coba method analyze
            if hasattr(analyzer, 'analyze'):
                result = analyzer.analyze(test_data)
            elif hasattr(analyzer, 'analyze_case'):
                result = analyzer.analyze_case(test_data)
            else:
                methods = [m for m in dir(analyzer) if m.startswith('analyze') and callable(getattr(analyzer, m))]
                if methods:
                    result = getattr(analyzer, methods[0])(test_data)
                else:
                    result = {"status": "no_analyze_method"}
            
            working_analyzers.append((name, analyzer_class))
            print(f"✅ {name}: WORKING")
            
        except Exception as e:
            print(f"❌ {name}: FAILED - {e}")
    
    print(f"\n📊 FINAL RESULTS: {len(working_analyzers)}/{len(existing_files)} files working")
    
    # Tampilkan detail analyzer yang berhasil
    if working_analyzers:
        print(f"\n🎉 ANALYZER YANG BERHASIL:")
        for name, analyzer_class in working_analyzers:
            print(f"   • {name}: {analyzer_class.__name__}")
    
    return len(working_analyzers)

if __name__ == "__main__":
    count = test_raw_files()
    if count > 0:
        print(f"\n🎉 {count} ANALYZER HUKUM INDONESIA BERFUNGSI!")
    else:
        print("\n💥 TIDAK ADA ANALYZER YANG BERFUNGSI!")
