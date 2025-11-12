#!/usr/bin/env python3
"""
Test Integration Potential - LegalMind-AI dengan VersaLaw2
"""

import sys
sys.path.append('legalmind-ai')

def test_modules():
    print("🔍 TESTING LEGALMIND-AI MODULES INTEGRATION")
    print("=" * 50)
    
    modules_to_test = [
        'unified_analysis_engine',
        'core_enhanced', 
        'enhanced_search'
    ]
    
    for module_name in modules_to_test:
        try:
            module = __import__(module_name)
            print(f"✅ {module_name}: IMPORT SUCCESS")
            # Show available classes/functions
            items = [item for item in dir(module) if not item.startswith('_')]
            print(f"   Available: {items[:5]}{'...' if len(items) > 5 else ''}")
        except Exception as e:
            print(f"❌ {module_name}: {e}")

if __name__ == "__main__":
    test_modules()
