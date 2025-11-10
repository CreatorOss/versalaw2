#!/usr/bin/env python3
"""
Simple Test for Indonesian Law Modules
"""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    print("🇮🇩 SIMPLE TEST - MODUL HUKUM INDONESIA")
    print("=" * 50)
    
    try:
        # Test imports
        from versalaw2.indonesian_law import IndonesianLawAnalyzer
        from versalaw2.indonesian_law.hierarchy.constitutional_law import ConstitutionalLawAnalyzer
        from versalaw2.indonesian_law.hierarchy.statutory_law import StatutoryLawAnalyzer
        
        print("✅ 1. Import modules - SUCCESS")
        
        # Test instantiation
        const_analyzer = ConstitutionalLawAnalyzer()
        stat_analyzer = StatutoryLawAnalyzer()
        indo_analyzer = IndonesianLawAnalyzer()
        
        print("✅ 2. Instantiate analyzers - SUCCESS")
        
        # Test basic functionality
        test_text = "Perjanjian ini membatasi kebebasan berpendapat"
        
        const_result = const_analyzer.analyze_compliance(test_text)
        print("✅ 3. Constitutional analysis - SUCCESS")
        print(f"   Rights violations found: {len(const_result.get('rights_violations', []))}")
        
        stat_result = stat_analyzer.analyze_compliance(test_text) 
        print("✅ 4. Statutory analysis - SUCCESS")
        print(f"   Hierarchy issues found: {len(stat_result.get('hierarchy_issues', []))}")
        
        indo_result = indo_analyzer.comprehensive_analysis(test_text)
        print("✅ 5. Integrated analysis - SUCCESS")
        print(f"   Overall risk: {indo_result['compliance_summary']['overall_risk']}")
        
        print("\n🎉 SEMUA TEST MODUL HUKUM INDONESIA BERHASIL!")
        
    except Exception as e:
        print(f"❌ TEST GAGAL: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
