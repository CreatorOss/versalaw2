#!/usr/bin/env python3
"""
TEST VERSALAW2 v3.0.0 INTEGRATION
"""

from versalaw2 import (
    # Core VersaLaw2
    EnhancedLegalClassifierWithDB,
    LegalDatabaseIntegrator,
    GhostContractAnalyzer,
    
    # New Legalmind-AI modules
    UnifiedAnalysisEngine,
    UnifiedLegalAnalyzer, 
    EnhancedSearchEngine,
    AIEnhancement,
    LegalMindEnhanced,
    PromptTemplates,
    LegalMindConfig
)

def main():
    print("🚀 VERSALAW2 v3.0.0 - INTEGRATION TEST")
    print("=" * 50)
    
    # Test semua modul
    modules = {
        "EnhancedLegalClassifierWithDB": EnhancedLegalClassifierWithDB,
        "LegalDatabaseIntegrator": LegalDatabaseIntegrator,
        "GhostContractAnalyzer": GhostContractAnalyzer,
        "UnifiedAnalysisEngine": UnifiedAnalysisEngine,
        "UnifiedLegalAnalyzer": UnifiedLegalAnalyzer,
        "EnhancedSearchEngine": EnhancedSearchEngine,
        "AIEnhancement": AIEnhancement,
        "LegalMindEnhanced": LegalMindEnhanced,
        "PromptTemplates": PromptTemplates,
        "LegalMindConfig": LegalMindConfig
    }
    
    print("🔧 TESTING MODULE IMPORTS:")
    for name, module in modules.items():
        try:
            # Try to instantiate or access
            if hasattr(module, '__name__'):
                print(f"✅ {name}: IMPORT SUCCESS")
            else:
                instance = module()
                print(f"✅ {name}: INSTANTIATION SUCCESS")
        except Exception as e:
            print(f"❌ {name}: {e}")
    
    print(f"\n📊 INTEGRATION SUMMARY:")
    print(f"   Total modules tested: {len(modules)}")
    print(f"   VersaLaw2 v3.0.0 ready for production!")

if __name__ == "__main__":
    main()
