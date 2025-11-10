#!/usr/bin/env python3
"""
Test All Fixed International Law Modules
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_module_import(module_name, class_name):
    """Test if a module can be imported"""
    try:
        module = __import__(f'versalaw2.international_law.{module_name}', fromlist=[class_name])
        analyzer_class = getattr(module, class_name)
        analyzer = analyzer_class()
        return True, f"✅ {class_name}"
    except ImportError as e:
        return False, f"❌ {class_name}: {e}"
    except Exception as e:
        return False, f"❌ {class_name}: {e}"

def main():
    print("🔍 TESTING ALL FIXED INTERNATIONAL LAW MODULES")
    print("=" * 60)
    
    modules_to_test = [
        ("international_treaties", "InternationalTreatyAnalyzer"),
        ("diplomatic_law", "DiplomaticLawAnalyzer"),
        ("law_of_the_sea", "LawOfTheSeaAnalyzer"),
        ("international_humanitarian", "InternationalHumanitarianAnalyzer"),
        ("international_trade", "InternationalTradeAnalyzer"),
        ("extradition_mutual_legal", "ExtraditionMLATAnalyzer")
    ]
    
    success_count = 0
    for module_name, class_name in modules_to_test:
        success, message = test_module_import(module_name, class_name)
        print(message)
        if success:
            success_count += 1
    
    print(f"\n📊 RESULTS: {success_count}/{len(modules_to_test)} modules operational")
    
    if success_count == len(modules_to_test):
        print("🎉 ALL INTERNATIONAL LAW MODULES FIXED AND OPERATIONAL!")
        
        # Test functionality
        print("\n🧪 TESTING FUNCTIONALITY...")
        from versalaw2.international_law.international_treaties import InternationalTreatyAnalyzer
        analyzer = InternationalTreatyAnalyzer()
        result = analyzer.analyze_treaty_ratification({"bilateral": True})
        print(f"✅ Treaty analysis working: {len(result)} aspects analyzed")
        
    else:
        print(f"⚠️  {len(modules_to_test) - success_count} modules need attention")

if __name__ == "__main__":
    main()
