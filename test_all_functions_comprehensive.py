import sys
import os

def test_all_functions(version_name, use_local=False):
    """Test semua fungsi untuk versi tertentu"""
    print(f"\n🔍 COMPREHENSIVE TEST: {version_name}")
    print("=" * 50)
    
    if use_local:
        sys.path.insert(0, 'src')
    
    try:
        # Import semua modules
        from versalaw2 import (
            MayaLegalQASystem, MayaWisdomProcessor, EnhancedLegalAnalyzer,
            DocumentProcessor, ContractAnalyzer, UnifiedLegalAnalyzer,
            AILegalPersonhoodAnalyzer, InternationalDigitalLawAnalyzer
        )
        
        print("✅ Semua modules imported")
        
        # Test setiap system dengan semua method-nya
        test_cases = [
            {
                "name": "MayaLegalQASystem",
                "instance": MayaLegalQASystem(),
                "methods": [
                    ("ask", "Test legal question"),
                    ("classify_question", "What is contract law?")
                ]
            },
            {
                "name": "MayaWisdomProcessor", 
                "instance": MayaWisdomProcessor(),
                "methods": [
                    ("process_legal_query", "Test wisdom question"),
                    ("get_legal_insights", "Contract analysis context")
                ]
            },
            {
                "name": "EnhancedLegalAnalyzer",
                "instance": EnhancedLegalAnalyzer(),
                "methods": [
                    ("analyze_document", "Sample legal document text"),
                    ("compare_legislation", "Compare two laws")
                ]
            },
            {
                "name": "DocumentProcessor",
                "instance": DocumentProcessor(),
                "methods": [
                    ("process_document", "Document to process"),
                    ("preprocess", "Text to preprocess")
                ]
            },
            {
                "name": "ContractAnalyzer",
                "instance": ContractAnalyzer(),
                "methods": [
                    ("analyze_contract", "Contract text sample"),
                    ("validate_contract", {"sample": "data"})
                ]
            },
            {
                "name": "UnifiedLegalAnalyzer",
                "instance": UnifiedLegalAnalyzer(),
                "methods": [
                    ("analyze_legal_text", "Legal text for analysis"),
                    ("cross_domain_analysis", "Complex legal issue")
                ]
            },
            {
                "name": "AILegalPersonhoodAnalyzer",
                "instance": AILegalPersonhoodAnalyzer(),
                "methods": [
                    ("analyze_arion_case", None),
                    ("consciousness_tests", None)
                ]
            },
            {
                "name": "InternationalDigitalLawAnalyzer",
                "instance": InternationalDigitalLawAnalyzer(),
                "methods": [
                    ("analyze_ghost_contract_case", {}),
                    ("digital_law_framework", None)
                ]
            }
        ]
        
        success_count = 0
        total_methods = 0
        
        for system in test_cases:
            print(f"\n📊 Testing {system['name']}:")
            instance = system["instance"]
            
            for method_name, test_input in system["methods"]:
                total_methods += 1
                try:
                    method = getattr(instance, method_name)
                    
                    if test_input is None:
                        result = method()
                    else:
                        result = method(test_input)
                    
                    print(f"   ✅ {method_name}(): WORKING")
                    success_count += 1
                    
                except Exception as e:
                    print(f"   ❌ {method_name}(): FAILED - {e}")
        
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
            success_count += 3
            total_methods += 3
            
        except Exception as e:
            print(f"   ❌ Integrated workflow: FAILED - {e}")
        
        print(f"\n📈 {version_name} RESULTS:")
        print(f"   Methods: {success_count}/{total_methods} successful")
        print(f"   Success rate: {(success_count/total_methods)*100:.1f}%")
        
        return success_count == total_methods
        
    except Exception as e:
        print(f"❌ Comprehensive test failed: {e}")
        return False

# Test kedua versi
print("🚀 COMPREHENSIVE FUNCTIONALITY TEST")
print("====================================")

# Test local version (3.0.1)
print("\n1. TESTING LOCAL v3.0.1")
local_perfect = test_all_functions("LOCAL v3.0.1", use_local=True)

# Install PyPI version untuk testing
print("\n2. INSTALLING PyPI v3.0.0 FOR TESTING")
os.system("pip install versalaw2==3.0.0 > /dev/null 2>&1")

# Test PyPI version (3.0.0)
print("\n3. TESTING PyPI v3.0.0")
pypi_perfect = test_all_functions("PyPI v3.0.0", use_local=False)

print("\n" + "=" * 60)
print("🎯 FINAL VERDICT:")
print(f"   Local v3.0.1: {'✅ PERFECT' if local_perfect else '❌ ISSUES'}")
print(f"   PyPI v3.0.0:  {'✅ PERFECT' if pypi_perfect else '❌ ISSUES'}")

if local_perfect and pypi_perfect:
    print("\n💫 BOTH VERSIONS ARE PERFECT!")
    print("🚀 Safe to update to v3.0.1 on PyPI!")
elif local_perfect and not pypi_perfect:
    print("\n⚠️  Local version better than PyPI version")
    print("🚀 Recommended to update to v3.0.1")
else:
    print("\n🔧 Both versions have issues - need fixes")
