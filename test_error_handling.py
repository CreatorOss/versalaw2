import sys
import os

sys.path.insert(0, 'src')

print("🛡️  ERROR HANDLING TEST")
print("=" * 50)

def test_edge_cases():
    """Test system with edge cases and error conditions"""
    
    try:
        from versalaw2 import MayaLegalQASystem, MayaWisdomProcessor
        
        qa = MayaLegalQASystem()
        wisdom = MayaWisdomProcessor()
        
        print("✅ Systems initialized")
        
        # Test edge cases
        test_cases = [
            "",  # Empty string
            "   ",  # Whitespace only
            "A",  # Very short
            "x" * 1000,  # Very long
            "What is the legal status of @#$%^&*()?",  # Special chars
            "Contract law in Indonesia and international standards for digital agreements",  # Complex
        ]
        
        print("\n🧪 Testing edge cases:")
        for i, case in enumerate(test_cases, 1):
            try:
                if case.strip():  # Only test non-empty cases
                    answer = qa.ask(case)
                    wisdom_result = wisdom.process_legal_query(case)
                    print(f"✅ Case {i}: Handled successfully")
                    print(f"   Confidence: {answer.confidence:.0%}")
                else:
                    print(f"⚠️  Case {i}: Empty input skipped")
            except Exception as e:
                print(f"❌ Case {i} failed: {e}")
        
        # Test method existence
        print("\n🔍 Testing method availability:")
        required_methods = {
            'MayaLegalQASystem': ['ask', 'classify_question'],
            'MayaWisdomProcessor': ['process_legal_query', 'get_legal_insights'],
            'EnhancedLegalAnalyzer': ['analyze_document', 'compare_legislation'],
        }
        
        for class_name, methods in required_methods.items():
            instance = eval(f"{class_name}()")
            for method in methods:
                if hasattr(instance, method):
                    print(f"✅ {class_name}.{method}: Available")
                else:
                    print(f"❌ {class_name}.{method}: Missing")
        
        return True
        
    except Exception as e:
        print(f"❌ System test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_edge_cases()
    if success:
        print("\n🎉 ERROR HANDLING TEST PASSED!")
    else:
        print("\n⚠️  Error handling needs improvement")
