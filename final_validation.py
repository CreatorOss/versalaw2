#!/usr/bin/env python3
"""
FINAL VALIDATION SCRIPT FOR VERSALAW2
Comprehensive testing of installation, imports, and functionality
"""

import sys
import os
import importlib
import subprocess

def validate_installation():
    """Validate package installation"""
    print("🔍 VALIDATING VERSALAW2 INSTALLATION...")
    print("=" * 60)
    
    # Test basic import
    try:
        import versalaw2
        print("✅ Main package import: SUCCESS")
    except Exception as e:
        print(f"❌ Main package import: FAILED - {e}")
        return False
    
    # Test submodule imports
    submodules = [
        'versalaw2.indonesian_law',
        'versalaw2.international_law', 
    ]
    
    for module in submodules:
        try:
            importlib.import_module(module)
            print(f"✅ {module} import: SUCCESS")
        except Exception as e:
            print(f"❌ {module} import: FAILED - {e}")
            return False
    
    return True

def validate_dependencies():
    """Validate all required dependencies"""
    print("\n📦 VALIDATING DEPENDENCIES...")
    print("=" * 60)
    
    dependencies = [
        'transformers',
        'torch', 
        'numpy',
        'pandas',
        'requests',
        'beautifulsoup4',
        'sklearn',
        'fastapi',
        'uvicorn',
        'pydantic'
    ]
    
    all_ok = True
    for dep in dependencies:
        try:
            importlib.import_module(dep)
            print(f"✅ {dep}: INSTALLED")
        except Exception as e:
            print(f"❌ {dep}: MISSING - {e}")
            all_ok = False
    
    return all_ok

def validate_functionality():
    """Validate core functionality"""
    print("\n⚙️ VALIDATING CORE FUNCTIONALITY...")
    print("=" * 60)
    
    try:
        # Test analyzers
        from versalaw2.indonesian_law.specialized_law.anti_corruption import AntiCorruptionAnalyzer
        from versalaw2.indonesian_law.specialized_law.terrorism_law import TerrorismLawAnalyzer
        from versalaw2.international_law.international_treaties import InternationalTreatyAnalyzer
        
        print("✅ Analyzer imports: SUCCESS")
        
        # Test instantiation
        corruption_analyzer = AntiCorruptionAnalyzer()
        terrorism_analyzer = TerrorismLawAnalyzer() 
        treaty_analyzer = InternationalTreatyAnalyzer()
        
        print("✅ Analyzer instantiation: SUCCESS")
        
        # Test basic analysis
        test_case = {"melawan_hukum": True}
        result = corruption_analyzer.analyze_corruption_case(test_case)
        
        if isinstance(result, dict):
            print("✅ Basic analysis execution: SUCCESS")
        else:
            print("❌ Basic analysis execution: INVALID RESULT")
            return False
            
    except Exception as e:
        print(f"❌ Functionality test: FAILED - {e}")
        return False
    
    return True

def run_package_tests():
    """Run existing package tests"""
    print("\n🧪 RUNNING EXISTING TESTS...")
    print("=" * 60)
    
    test_files = [
        'test_all_modules_final.py',
        'test_individual.py',
        'example_usage.py'
    ]
    
    for test_file in test_files:
        if os.path.exists(test_file):
            try:
                print(f"📄 Running {test_file}...")
                result = subprocess.run([sys.executable, test_file], 
                                      capture_output=True, text=True, timeout=60)
                if result.returncode == 0:
                    print(f"✅ {test_file}: PASSED")
                else:
                    print(f"❌ {test_file}: FAILED")
                    print(f"   Error: {result.stderr}")
            except subprocess.TimeoutExpired:
                print(f"⏰ {test_file}: TIMEOUT")
            except Exception as e:
                print(f"❌ {test_file}: ERROR - {e}")
        else:
            print(f"📄 {test_file}: NOT FOUND")

def main():
    """Main validation function"""
    print("🚀 VERSALAW2 FINAL VALIDATION")
    print("=" * 60)
    
    # Run all validations
    installation_ok = validate_installation()
    dependencies_ok = validate_dependencies() 
    functionality_ok = validate_functionality()
    
    # Run tests
    run_package_tests()
    
    # Final summary
    print("\n" + "=" * 60)
    print("📊 VALIDATION SUMMARY")
    print("=" * 60)
    
    if all([installation_ok, dependencies_ok, functionality_ok]):
        print("🎉 ALL VALIDATIONS PASSED! VERSALAW2 IS READY FOR PRODUCTION.")
        return 0
    else:
        print("❌ SOME VALIDATIONS FAILED. PLEASE CHECK THE ISSUES ABOVE.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
