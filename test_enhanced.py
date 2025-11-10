from versalaw2.legal_classifier import EnhancedLegalClassifier

def main():
    print("🧪 TEST ENHANCED CLASSIFIER")
    print("=" * 40)
    
    # Initialize
    clf = EnhancedLegalClassifier()
    
    # Test questions
    test_questions = [
        "hakim menjatuhkan pidana di bawah minimum",
        "BCI neural interface contract", 
        "standard employment contract",
        "kasasi di mahkamah agung"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n{i}. Question: {question}")
        result = clf.classify_with_expert_analysis(question)
        print(f"   Category: {result['category']}")
        print(f"   Confidence: {result['confidence']:.2f}")
        print(f"   Expert Insights: {result.get('has_expert_insights', False)}")
        if result.get('has_expert_insights'):
            expert = result['expert_analysis']
            print(f"   Expert Type: {expert['type']}")
            print(f"   Expert Confidence: {expert.get('confidence', 0):.2f}")

if __name__ == "__main__":
    main()
