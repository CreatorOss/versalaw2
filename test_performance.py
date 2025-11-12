import sys
import os
import time

sys.path.insert(0, 'src')

print("⚡ PERFORMANCE TEST")
print("=" * 50)

def performance_test():
    """Test system performance and response times"""
    
    try:
        from versalaw2 import MayaLegalQASystem, MayaWisdomProcessor
        
        # Initialize systems
        start_time = time.time()
        qa = MayaLegalQASystem()
        wisdom = MayaWisdomProcessor()
        init_time = time.time() - start_time
        
        print(f"✅ Systems initialized in {init_time:.2f}s")
        
        # Test questions
        test_questions = [
            "What is contract law?",
            "Explain data protection",
            "Legal requirements for business",
            "International trade agreements",
            "Digital signature validity"
        ]
        
        print(f"\n🧪 Testing {len(test_questions)} questions:")
        
        total_qa_time = 0
        total_wisdom_time = 0
        
        for i, question in enumerate(test_questions, 1):
            print(f"\n{i}. {question}")
            
            # Test QA system
            qa_start = time.time()
            answer = qa.ask(question)
            qa_time = time.time() - qa_start
            total_qa_time += qa_time
            print(f"   ❓ QA: {qa_time:.2f}s (Confidence: {answer.confidence:.0%})")
            
            # Test wisdom system
            wisdom_start = time.time()
            wisdom_result = wisdom.process_legal_query(question)
            wisdom_time = time.time() - wisdom_start
            total_wisdom_time += wisdom_time
            print(f"   🔮 Wisdom: {wisdom_time:.2f}s")
        
        # Calculate averages
        avg_qa = total_qa_time / len(test_questions)
        avg_wisdom = total_wisdom_time / len(test_questions)
        
        print(f"\n📊 PERFORMANCE SUMMARY:")
        print(f"   Average QA response: {avg_qa:.2f}s")
        print(f"   Average Wisdom response: {avg_wisdom:.2f}s")
        print(f"   Total initialization: {init_time:.2f}s")
        
        # Performance thresholds (adjust as needed)
        if avg_qa < 2.0 and avg_wisdom < 2.0:
            print("🎉 PERFORMANCE: EXCELLENT")
            return True
        elif avg_qa < 5.0 and avg_wisdom < 5.0:
            print("✅ PERFORMANCE: ACCEPTABLE") 
            return True
        else:
            print("⚠️  PERFORMANCE: NEEDS OPTIMIZATION")
            return False
            
    except Exception as e:
        print(f"❌ Performance test failed: {e}")
        return False

if __name__ == "__main__":
    success = performance_test()
    if success:
        print("\n🚀 Performance acceptable for deployment")
    else:
        print("\n🔧 Performance improvements needed")
