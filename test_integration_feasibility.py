#!/usr/bin/env python3
"""
Test Integration Feasibility
"""

import sys
import os

# Add both paths
sys.path.insert(0, 'src/versalaw2')
sys.path.insert(0, '../legalmind-project/legalmind-ai')

def test_compatibility():
    print("🔧 TESTING INTEGRATION FEASIBILITY")
    print("=" * 50)
    
    try:
        # Test VersaLaw2 current modules
        from versalaw2 import EnhancedLegalClassifierWithDB, LegalDatabaseIntegrator
        print("✅ VersaLaw2 current modules: IMPORT SUCCESS")
        
        # Test Legalmind-AI unique modules
        try:
            import unified_analysis_engine
            print("✅ unified_analysis_engine: IMPORT SUCCESS")
        except:
            print("❌ unified_analysis_engine: IMPORT FAILED")
            
        try:
            import enhanced_search
            print("✅ enhanced_search: IMPORT SUCCESS") 
        except:
            print("❌ enhanced_search: IMPORT FAILED")
            
        try:
            import ai_anhancement
            print("✅ ai_enhancement: IMPORT SUCCESS")
        except:
            print("❌ ai_enhancement: IMPORT FAILED")
            
        # Test if they can work together
        print("\n🔗 TESTING CROSS-MODULE COMPATIBILITY:")
        clf = EnhancedLegalClassifierWithDB()
        print("✅ VersaLaw2 classifier instantiated")
        
        # Try to use together (conceptual)
        print("💡 Integration concept: Use unified_analysis_engine as wrapper")
        print("💡 EnhancedLegalClassifierWithDB + unified_analysis_engine = SUPER POWERFUL!")
        
    except Exception as e:
        print(f"❌ Compatibility test failed: {e}")

if __name__ == "__main__":
    test_compatibility()
