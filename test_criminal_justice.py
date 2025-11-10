#!/usr/bin/env python3
"""
Test Criminal Justice Modules
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    print("👮 TEST MODUL CRIMINAL JUSTICE")
    print("=" * 50)
    
    try:
        from versalaw2.indonesian_law.criminal_justice.police_regulations import PoliceRegulationsAnalyzer
        
        print("✅ 1. Import PoliceRegulationsAnalyzer - SUCCESS")
        
        # Test analyzer
        police_analyzer = PoliceRegulationsAnalyzer()
        
        # Test case: Police procedures
        test_text = """
        Proses penyidikan dilakukan dengan membuat berita acara pemeriksaan.
        Penyidik mengeluarkan surat perintah penangkapan terhadap tersangka.
        Dalam pemeriksaan, tersangka didampingi oleh pengacara.
        """
        
        result = police_analyzer.analyze_procedures(test_text)
        
        print("✅ 2. Police procedures analysis - SUCCESS")
        print(f"   PERKAP references: {len(result['perkap_compliance'])}")
        print(f"   Investigation issues: {len(result['investigation_issues'])}")
        print(f"   Human rights checks: {len(result['human_rights_compliance'])}")
        
        # Show some findings
        if result['perkap_compliance']:
            print("\n   PERKAP References found:")
            for ref in result['perkap_compliance'][:2]:
                print(f"     - {ref['keyword']}: {ref['regulation']}")
        
        print("\n🎉 MODUL CRIMINAL JUSTICE BERHASIL!")
        
    except Exception as e:
        print(f"❌ TEST GAGAL: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
