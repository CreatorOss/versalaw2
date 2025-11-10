from versalaw2 import EnhancedLegalClassifier, EnhancedLegalKnowledge

def test_all_features():
    print("🧪 COMPREHENSIVE FEATURE TEST")
    print("=" * 50)
    
    # Test 1: Comprehensive Analysis
    print("\n1. Testing Comprehensive Analysis...")
    clf = EnhancedLegalClassifier()
    comprehensive = clf.comprehensive_analysis("hakim menjatuhkan pidana di bawah minimum KUHP")
    
    print(f"   Query: {comprehensive['query']}")
    print(f"   Category: {comprehensive['classification']['category']}")
    print(f"   Complexity: {comprehensive['complexity_assessment']}")
    print(f"   Expert Insights: {comprehensive['classification'].get('has_expert_insights', False)}")
    print(f"   Suggestions: {len(comprehensive['suggestions'])} items")
    
    # Test 2: Direct Knowledge Access
    print("\n2. Testing Direct Knowledge Access...")
    knowledge = EnhancedLegalKnowledge()
    expert_analysis = knowledge.get_expert_analysis("ghost contract dispute")
    
    if expert_analysis:
        print(f"   Expert Type: {expert_analysis['type']}")
        print(f"   Source: {expert_analysis['source']}")
        print(f"   Confidence: {expert_analysis.get('confidence', 0):.2f}")
    else:
        print("   No expert analysis found for this query")
    
    # Test 3: Available Domains
    print("\n3. Testing Available Domains...")
    domains = knowledge.get_available_domains()
    print(f"   Available domains: {len(domains)}")
    for domain in domains[:3]:
        print(f"     - {domain}")

if __name__ == "__main__":
    test_all_features()
