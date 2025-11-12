import sys
import os

def test_all_functions_fixed(version_name, use_local=False):
    """Test semua fungsi dengan fix untuk properties"""
    print(f"\n🔍 COMPREHENSIVE TEST (FIXED): {version_name}")
    print("=" * 50)
    
    if use_local:
        sys.path.insert(0, 'src')
    
    try:
        from versalaw2 import (
            MayaLegalQASystem, MayaWisdomProcessor, EnhancedLegalAnalyzer,
            DocumentProcessor, ContractAnalyzer, UnifiedLegalAnalyzer,
            AILegalPersonhoodAnalyzer, InternationalDigitalLawAnalyzer
        )
        
        print("✅ Semua modules imported")
        
        # Test cases yang sudah difix
        test_cases = [
            {
                "name": "MayaLegalQASystem",
                "instance": MayaLegalQASystem(),
                "methods": [
                    ("ask", "Test legal question", True),
                    ("classify_question", "What is contract law?", True)
                ]
            },
            {
                "name": "MayaWisdomProcessor", 
                "instance": MayaWisdomProcessor(),
                "methods": [
                    ("process_legal_query", "Test wisdom question", True),
                    ("get_legal_insights", "Contract analysis context", True)
                ]
            },
            {
                "name": "EnhancedLegalAnalyzer",
                "instance": EnhancedLegalAnalyzer(),
                "methods": [
                    ("analyze_document", "Sample legal document text", True),
                    ("compare_legislation", ["Doc1 text", "Doc2 text"], True)  # Fixed: 2 parameters
                ]
            },
            {
                "name": "DocumentProcessor",
                "instance": DocumentProcessor(),
                "methods": [
                    ("process_document", "Document to process", True),
                    ("preprocess", "Text to preprocess", True)
                ]
            },
            {
                "name": "ContractAnalyzer",
                "instance": ContractAnalyzer(),
                "methods": [
                    ("analyze_contract", "Contract text sample", True),
                    ("validate_contract", {"sample": "data"}, True)
                ]
            },
            {
                "name": "UnifiedLegalAnalyzer",
                "instance": UnifiedLegalAnalyzer(),
                "methods": [
                    ("analyze_legal_text", "Legal text for analysis", True),
                    ("cross_domain_analysis", "Complex legal issue", True)
                ]
            },
            {
                "name": "AILegalPersonhoodAnalyzer",
                "instance": AILegalPersonhoodAnalyzer(),
                "methods": [
                    ("analyze_arion_case", None, True),
                    ("consciousness_tests", None, False)  # Property, bukan method
                ]
            },
            {
                "name": "InternationalDigitalLawAnalyzer",
                "instance": InternationalDigitalLawAnalyzer(),
                "methods": [
                    ("analyze_ghost_contract_case", {}, True),
                    ("digital_law_framework", None, False)  # Property, bukan method
                ]
            }
        ]
        
        success_count = 0
        total_tests = 0
        
        for system in test_cases:
            print(f"\n📊 Testing {system['name']}:")
            instance = system["instance"]
            
            for method_name, test_input, is_method in system["methods"]:
                total_tests += 1
                try:
                    if hasattr(instance, method_name):
                        attr = getattr(instance, method_name)
                        
                        if is_method:
                            # Ini method, panggil dengan parameter
                            if isinstance(test_input, list):
                                result = attr(*test_input)  # Multiple parameters
                            elif test_input is None:
                                result = attr()  # No parameters
                            else:
                                result = attr(test_input)  # Single parameter
                            print(f"   ✅ {method_name}(): METHOD WORKING")
                        else:
                            # Ini property, akses langsung
                            result = attr
                            print(f"   ✅ {method_name}: PROPERTY WORKING")
                        
                        success_count += 1
                    else:
                        print(f"   ❌ {method_name}: NOT FOUND")
                        
                except Exception as e:
                    print(f"   ❌ {method_name}: FAILED - {e}")
        
        # Test integrated workflow
        print(f"\n🔄 Testing Integrated Workflow:")
        try:
            qa = MayaLegalQASystem()
            wisdom = MayaWisdomProcessor()
            analyzer = EnhancedLegalAnalyzer()
            
            question = "Integrated workflow test question"
            answer = qa.ask(question)
            wisdom_result = wisdom.process_legal_query(question)
            analysis = analyzer.analyze_document(question)
            
            print("   ✅ Integrated workflow: WORKING")
            success_count += 1
            total_tests += 1
            
        except Exception as e:
            print(f"   ❌ Integrated workflow: FAILED - {e}")
        
        print(f"\n📈 {version_name} RESULTS:")
        print(f"   Tests: {success_count}/{total_tests} successful")
        print(f"   Success rate: {(success_count/total_tests)*100:.1f}%")
        
        return success_count == total_tests
        
    except Exception as e:
        print(f"❌ Comprehensive test failed: {e}")
        return False

# Test kedua versi dengan fix
print("🚀 COMPREHENSIVE TEST WITH FIXES")
print("================================")

# Test local version (3.0.1 dengan fix)
print("\n1. TESTING LOCAL v3.0.1 (WITH FIXES)")
local_perfect = test_all_functions_fixed("LOCAL v3.0.1", use_local=True)

# Install PyPI version untuk testing
print("\n2. INSTALLING PyPI v3.0.0 FOR TESTING")
os.system("pip install versalaw2==3.0.0 > /dev/null 2>&1")

# Test PyPI version (3.0.0)
print("\n3. TESTING PyPI v3.0.0 (WITH FIXED TEST)")
pypi_perfect = test_all_functions_fixed("PyPI v3.0.0", use_local=False)

print("\n" + "=" * 60)
print("🎯 FINAL VERDICT (WITH FIXES):")
print(f"   Local v3.0.1: {'✅ PERFECT' if local_perfect else '❌ ISSUES'}")
print(f"   PyPI v3.0.0:  {'✅ PERFECT' if pypi_perfect else '❌ ISSUES'}")

if local_perfect and pypi_perfect:
    print("\n💫 BOTH VERSIONS ARE NOW PERFECT!")
    print("🚀 Safe to update to v3.0.1 on PyPI!")
else:
    print("\n🔧 Still some issues - need additional fixes")
