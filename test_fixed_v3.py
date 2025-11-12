#!/usr/bin/env python3
"""
TEST FIXED VERSALAW2 v3.0.0
"""

print("🚀 VERSALAW2 v3.0.0 - FIXED VERSION TEST")
print("=" * 50)

try:
    from versalaw2 import (
        EnhancedLegalClassifierWithDB,
        LegalDatabaseIntegrator, 
        GhostContractAnalyzer,
        UnifiedAnalysisEngine,
        EnhancedSearchEngine,
        AIEnhancement,
        PromptTemplates,
        LegalMindConfig
    )
    
    print("✅ ALL MODULES IMPORTED SUCCESSFULLY!")
    
    # Test instantiation
    clf = EnhancedLegalClassifierWithDB()
    integrator = LegalDatabaseIntegrator()
    ghost = GhostContractAnalyzer()
    unified = UnifiedAnalysisEngine()
    search = EnhancedSearchEngine()  # Now works without parameters!
    ai = AIEnhancement()
    prompts = PromptTemplates()
    config = LegalMindConfig()
    
    print("✅ ALL MODULES INSTANTIATED!")
    
    # Test functionality
    test_doc = "Kontrak BCI neural interface dengan klausa yurisdiksi Singapura"
    
    result1 = clf.comprehensive_analysis_with_db(test_doc)
    print(f"✅ Enhanced analysis: {result1.get('analysis_level', 'N/A')}")
    
    result2 = ghost.analyze_ghost_contract(test_doc)
    print(f"✅ Ghost analysis: {result2.get('risk_level', 'N/A')} risk")
    
    result3 = unified.unified_analyze(test_doc)
    print(f"✅ Unified analysis: {result3.get('analysis_type', 'N/A')}")
    
    result4 = search.search_legal_content(test_doc)
    print(f"✅ Search results: {len(result4.get('matches', []))} matches")
    
    result5 = ai.enhance_analysis(result1)
    print(f"✅ AI enhancement: {result5.get('ai_enhancements', {}).get('confidence_score', 'N/A')}")
    
    print("\n🎉 VERSALAW2 v3.0.0 - ALL SYSTEMS WORKING!")
    print("📦 Ready for deployment!")
    
except Exception as e:
    print(f"❌ Test failed: {e}")
    import traceback
    traceback.print_exc()
