import sys
import os
import importlib

# Setup path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
sys.path.insert(0, src_path)

print("🔍 COMPREHENSIVE TEST - MAYA LEGAL AI")
print("=" * 60)

def test_module_import(module_name, class_name):
    """Test importing a specific class from module"""
    try:
        module = importlib.import_module(f'versalaw2.{module_name}')
        class_obj = getattr(module, class_name)
        instance = class_obj()
        return True, instance
    except Exception as e:
        return False, str(e)

def test_method_execution(instance, method_name, test_input="test"):
    """Test executing a method on instance"""
    try:
        method = getattr(instance, method_name)
        result = method(test_input)
        return True, result
    except Exception as e:
        return False, str(e)

# Test all modules and their main methods
test_cases = [
    {
        "module": "maya_wisdom_processor",
        "class": "MayaWisdomProcessor", 
        "method": "process_legal_query",
        "test_input": "Test legal question"
    },
    {
        "module": "maya_legal_qa_system",
        "class": "MayaLegalQASystem",
        "method": "ask", 
        "test_input": "Test legal question"
    },
    {
        "module": "enhanced_legal_analyzer",
        "class": "EnhancedLegalAnalyzer",
        "method": "analyze_document",
        "test_input": "Test document text"
    },
    {
        "module": "document_processor", 
        "class": "DocumentProcessor",
        "method": "process_document",
        "test_input": "Test document"
    },
    {
        "module": "contract_analyzer",
        "class": "ContractAnalyzer",
        "method": "analyze_contract",
        "test_input": "Test contract text"
    },
    {
        "module": "unified_analyzer",
        "class": "UnifiedLegalAnalyzer", 
        "method": "analyze_legal_text",
        "test_input": "Test legal text"
    },
    {
        "module": "ai_legal_personhood_analyzer",
        "class": "AILegalPersonhoodAnalyzer",
        "method": "analyze_arion_case",
        "test_input": {}  # Empty dict for this method
    },
    {
        "module": "international_digital_law_analyzer",
        "class": "InternationalDigitalLawAnalyzer", 
        "method": "analyze_ghost_contract_case",
        "test_input": {}  # Empty dict for this method
    }
]

print("🧪 TESTING ALL MODULES:")
print("-" * 60)

success_count = 0
total_count = len(test_cases)

for i, test_case in enumerate(test_cases, 1):
    module_name = test_case["module"]
    class_name = test_case["class"]
    method_name = test_case["method"]
    test_input = test_case["test_input"]
    
    print(f"\n{i}. Testing {class_name}.{method_name}():")
    
    # Test import
    import_success, result = test_module_import(module_name, class_name)
    if not import_success:
        print(f"   ❌ IMPORT FAILED: {result}")
        continue
        
    instance = result
    print(f"   ✅ Import successful")
    
    # Test method execution
    method_success, method_result = test_method_execution(instance, method_name, test_input)
    if method_success:
        print(f"   ✅ Method executed successfully")
        print(f"   📊 Return type: {type(method_result)}")
        success_count += 1
    else:
        print(f"   ❌ METHOD FAILED: {method_result}")

print("\n" + "=" * 60)
print(f"📊 TEST RESULTS: {success_count}/{total_count} modules successful")

if success_count == total_count:
    print("🎉 ALL TESTS PASSED! READY FOR DEPLOYMENT!")
else:
    print(f"⚠️  {total_count - success_count} modules need attention")

print("\n🚀 TESTING PACKAGE LEVEL IMPORTS:")
print("-" * 60)

# Test package level imports
package_imports = [
    "MayaWisdomProcessor",
    "MayaLegalQASystem", 
    "EnhancedLegalAnalyzer",
    "DocumentProcessor",
    "ContractAnalyzer",
    "UnifiedLegalAnalyzer",
    "AILegalPersonhoodAnalyzer",
    "InternationalDigitalLawAnalyzer"
]

package_success = 0
for class_name in package_imports:
    try:
        exec(f"from versalaw2 import {class_name}")
        exec(f"instance = {class_name}()")
        print(f"✅ {class_name}: Package import successful")
        package_success += 1
    except Exception as e:
        print(f"❌ {class_name}: {e}")

print(f"\n📦 PACKAGE IMPORTS: {package_success}/{len(package_imports)} successful")

# Final verdict
if success_count == total_count and package_success == len(package_imports):
    print("\n💫 ALL SYSTEMS GO! READY FOR PyPI AND GIT DEPLOYMENT!")
else:
    print("\n🔧 SOME ADJUSTMENTS NEEDED BEFORE DEPLOYMENT")
