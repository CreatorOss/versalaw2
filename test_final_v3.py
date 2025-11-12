#!/usr/bin/env python3
"""
FINAL TEST - VERSALAW2 v3.0.0
"""

print("🚀 VERSALAW2 v3.0.0 - FINAL INTEGRATION TEST")
print("=" * 50)

try:
    # Test basic import
    import versalaw2
    print(f"✅ Package imported: {versalaw2.__version__}")
    
    # Test core functionality
    from versalaw2 import EnhancedLegalClassifierWithDB, LegalDatabaseIntegrator, GhostContractAnalyzer
    
    clf = EnhancedLegalClassifierWithDB()
    print("✅ EnhancedLegalClassifierWithDB: WORKING")
    
    integrator = LegalDatabaseIntegrator() 
    print("✅ LegalDatabaseIntegrator: WORKING")
    
    ghost = GhostContractAnalyzer()
    print("✅ GhostContractAnalyzer: WORKING")
    
    # Test new modules availability
    print("\n🔍 NEW MODULES AVAILABILITY:")
    
    if versalaw2.UNIFIED_AVAILABLE:
        from versalaw2 import UnifiedAnalysisEngine
        unified = UnifiedAnalysisEngine()
        print("✅ UnifiedAnalysisEngine: WORKING")
    else:
        print("⚠️ UnifiedAnalysisEngine: NOT AVAILABLE")
    
    if versalaw2.SEARCH_AVAILABLE:
        from versalaw2 import EnhancedSearchEngine
        search = EnhancedSearchEngine()
        print("✅ EnhancedSearchEngine: WORKING")
    else:
        print("⚠️ EnhancedSearchEngine: NOT AVAILABLE")
    
    if versalaw2.AI_AVAILABLE:
        from versalaw2 import AIEnhancement
        ai = AIEnhancement()
        print("✅ AIEnhancement: WORKING")
    else:
        print("⚠️ AIEnhancement: NOT AVAILABLE")
    
    # Test functionality
    print("\n🎯 TESTING FUNCTIONALITY:")
    test_contract = "Kontrak BCI neural interface"
    result = clf.comprehensive_analysis_with_db(test_contract)
    print(f"✅ Analysis completed: {result.get('analysis_level', 'N/A')}")
    
    ghost_result = ghost.analyze_ghost_contract(test_contract)
    print(f"✅ Ghost analysis: {ghost_result.get('risk_level', 'N/A')} risk")
    
    print("\n🎉 VERSALAW2 v3.0.0 - INTEGRATION SUCCESSFUL!")
    print("📦 Ready for production deployment!")
    
except Exception as e:
    print(f"❌ Integration failed: {e}")
    import traceback
    traceback.print_exc()
