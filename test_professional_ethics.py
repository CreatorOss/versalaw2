#!/usr/bin/env python3
"""
Test Professional Ethics Modules
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    print("⚖️ TEST MODUL PROFESSIONAL ETHICS")
    print("=" * 50)
    
    try:
        from versalaw2.indonesian_law.professional_ethics.legal_ethics import LegalEthicsAnalyzer
        
        print("✅ 1. Import LegalEthicsAnalyzer - SUCCESS")
        
        # Test analyzer
        ethics_analyzer = LegalEthicsAnalyzer()
        
        # Test case: Legal ethics scenario
        test_text = """
        Pengacara menerima kasus dari kedua belah pihak yang berkonflik.
        Terdapat potensi benturan kepentingan dalam penanganan kasus.
        Dokumen rahasia klien tidak boleh diungkapkan kepada pihak lawan.
        """
        
        result = ethics_analyzer.analyze_conduct(test_text, profession="pengacara")
        
        print("✅ 2. Legal ethics analysis - SUCCESS")
        print(f"   Confidentiality issues: {len(result['confidentiality_issues'])}")
        print(f"   Conflict of interest: {len(result['conflict_of_interest'])}")
        print(f"   Professional standards: {len(result['professional_standards'])}")
        print(f"   General ethics: {len(result['ethics_compliance'])}")
        
        # Show some findings
        if result['conflict_of_interest']:
            print("\n   Conflict of Interest found:")
            for conflict in result['conflict_of_interest']:
                print(f"     - {conflict['issue']}: {conflict['keyword']}")
        
        if result['confidentiality_issues']:
            print("\n   Confidentiality issues found:")
            for issue in result['confidentiality_issues']:
                print(f"     - {issue['issue']}: {issue['keyword']}")
        
        print("\n🎉 MODUL PROFESSIONAL ETHICS BERHASIL!")
        
    except Exception as e:
        print(f"❌ TEST GAGAL: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
