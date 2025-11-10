#!/usr/bin/env python3
"""
TEST EXISTING FILES - Hanya test file yang benar-benar ada
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_existing_files():
    print("🎯 TEST FILE YANG ADA - HUKUM INDONESIA")
    print("=" * 60)
    
    # List file yang benar-benar ada
    import_modules = []
    
    # Specialized Law files yang ada
    specialized_files = [
        "versalaw2.indonesian_law.specialized_law.anti_corruption",
        "versalaw2.indonesian_law.specialized_law.terrorism_law", 
        "versalaw2.indonesian_law.specialized_law.narcotics",
        "versalaw2.indonesian_law.specialized_law.money_laundering",
        "versalaw2.indonesian_law.specialized_law.cyber_crime",
        "versalaw2.indonesian_law.specialized_law.human_trafficking",
        "versalaw2.indonesian_law.specialized_law.illegal_logging",
        "versalaw2.indonesian_law.specialized_law.illegal_mining",
        "versalaw2.indonesian_law.specialized_law.smuggling",
    ]
    
    # Professional Ethics
    ethics_files = [
        "versalaw2.indonesian_law.professional_ethics.legal_ethics",
    ]
    
    # Criminal Justice (files yang ada)
    criminal_files = [
        "versalaw2.indonesian_law.criminal_justice.police_regulations",
    ]
    
    all_files = specialized_files + ethics_files + criminal_files
    
    print("🔍 CHECKING EXISTING FILES:")
    print("-" * 30)
    
    working_files = []
    for file_path in all_files:
        try:
            # Coba import module
            module = __import__(file_path, fromlist=['*'])
            
            # Cari class Analyzer di module
            analyzer_classes = []
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and 'Analyzer' in attr_name and not attr_name.startswith('_'):
                    analyzer_classes.append(attr_name)
            
            if analyzer_classes:
                working_files.append((file_path, analyzer_classes[0], module))
                print(f"✅ {file_path.split('.')[-1]}: FOUND {analyzer_classes[0]}")
            else:
                print(f"⚠️  {file_path.split('.')[-1]}: NO ANALYZER CLASS")
                
        except Exception as e:
            print(f"❌ {file_path.split('.')[-1]}: ERROR - {e}")
    
    # Test functionality
    print(f"\n🔧 TESTING {len(working_files)} ANALYZERS:")
    print("=" * 60)
    
    successful = 0
    for file_path, class_name, module in working_files:
        try:
            analyzer_class = getattr(module, class_name)
            analyzer = analyzer_class()
            
            # Test dengan data sederhana
            test_data = {"test": True}
            
            # Coba method analyze
            if hasattr(analyzer, 'analyze'):
                result = analyzer.analyze(test_data)
            elif hasattr(analyzer, 'analyze_case'):
                result = analyzer.analyze_case(test_data)
            else:
                # Cari method lain
                methods = [m for m in dir(analyzer) if m.startswith('analyze') and callable(getattr(analyzer, m))]
                if methods:
                    result = getattr(analyzer, methods[0])(test_data)
                else:
                    result = {"status": "no_analyze_method"}
            
            print(f"✅ {class_name}: FUNCTIONAL")
            successful += 1
            
        except Exception as e:
            print(f"❌ {class_name}: FAILED - {e}")
    
    print(f"\n📊 RESULTS: {successful}/{len(working_files)} files working")
    return successful

if __name__ == "__main__":
    count = test_existing_files()
    if count > 0:
        print(f"🎉 {count} FILE HUKUM INDONESIA BERFUNGSI!")
    else:
        print("💥 TIDAK ADA FILE YANG BERFUNGSI!")
