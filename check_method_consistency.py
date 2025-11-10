#!/usr/bin/env python3
"""
CHECK METHOD CONSISTENCY - Pastikan semua analyzer punya method yang sama
"""

import sys
import os
import importlib.util

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def check_all_analyzers():
    print("🔍 CHECKING METHOD CONSISTENCY")
    print("=" * 60)
    
    files_to_check = [
        "versalaw2/indonesian_law/specialized_law/anti_corruption.py",
        "versalaw2/indonesian_law/specialized_law/terrorism_law.py",
        "versalaw2/indonesian_law/specialized_law/narcotics.py",
        "versalaw2/indonesian_law/specialized_law/money_laundering.py",
        "versalaw2/indonesian_law/specialized_law/cyber_crime.py",
        "versalaw2/indonesian_law/specialized_law/human_trafficking.py",
        "versalaw2/indonesian_law/specialized_law/illegal_logging.py",
        "versalaw2/indonesian_law/specialized_law/illegal_mining.py",
        "versalaw2/indonesian_law/specialized_law/smuggling.py",
        "versalaw2/indonesian_law/professional_ethics/legal_ethics.py",
        "versalaw2/indonesian_law/criminal_justice/police_regulations.py",
    ]
    
    consistent = 0
    for file_path in files_to_check:
        try:
            spec = importlib.util.spec_from_file_location("module.name", file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Cari class Analyzer
            analyzer_class = None
            for attr_name in dir(module):
                if 'Analyzer' in attr_name and not attr_name.startswith('_'):
                    analyzer_class = getattr(module, attr_name)
                    break
            
            if analyzer_class:
                analyzer = analyzer_class()
                
                # Check required methods
                has_analyze = hasattr(analyzer, 'analyze') and callable(getattr(analyzer, 'analyze'))
                has_analyze_case = hasattr(analyzer, 'analyze_case') and callable(getattr(analyzer, 'analyze_case'))
                
                if has_analyze and has_analyze_case:
                    print(f"✅ {os.path.basename(file_path)}: CONSISTENT")
                    consistent += 1
                else:
                    print(f"❌ {os.path.basename(file_path)}: MISSING METHODS")
                    print(f"   - analyze: {has_analyze}")
                    print(f"   - analyze_case: {has_analyze_case}")
            else:
                print(f"❌ {os.path.basename(file_path)}: NO ANALYZER CLASS")
                
        except Exception as e:
            print(f"❌ {os.path.basename(file_path)}: ERROR - {e}")
    
    print(f"\n📊 RESULTS: {consistent}/{len(files_to_check)} analyzers consistent")
    return consistent == len(files_to_check)

if __name__ == "__main__":
    success = check_all_analyzers()
    if success:
        print("\n🎉 SEMUA ANALYZER MEMILIKI METHOD YANG KONSISTEN!")
    else:
        print("\n⚠️  ADA ANALYZER YANG PERLU DIPERBAIKI!")
