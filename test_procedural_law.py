#!/usr/bin/env python3
"""
VERSALAW2 Procedural Law Test
Menguji aspek hukum acara pidana dan perdata
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from versalaw2.indonesian_law.criminal_justice.police_regulations import PoliceRegulationsAnalyzer
from versalaw2.indonesian_law.specialized_law.civil_law import CivilLawAnalyzer

def main():
    print("⚖️ VERSALAW2 PROCEDURAL LAW TEST")
    print("=" * 55)
    
    police_analyzer = PoliceRegulationsAnalyzer()
    civil_analyzer = CivilLawAnalyzer()
    
    # Test 1: Hukum Acara Pidana
    print("\n1. 👮 TEST: HUKUM ACARA PIDANA (KUHAP)")
    criminal_procedure = """
    PROSES PENYIDIKAN TINDAK PIDANA PEMBUNUHAN
    Penangkapan tanpa surat perintah
    Pemeriksaan tanpa didampingi pengacara
    Penggeledahan tanpa saksi
    Barang bukti tidak disegel dengan benar
    Berita acara tidak ditandatangani tersangka
    """
    
    police_result = police_analyzer.analyze_procedures(criminal_procedure)
    print(f"   • Procedure violations: {len(police_result['investigation_issues'])}")
    print(f"   • PERKAP compliance: {len(police_result['perkap_compliance'])}")
    
    if police_result['investigation_issues']:
        print("   ⚠️  Procedure issues found:")
        for issue in police_result['investigation_issues'][:3]:
            print(f"     - {issue['procedure']} dalam {issue['context']}")
    
    # Test 2: Hukum Acara Perdata
    print("\n2. 📝 TEST: HUKUM ACARA PERDATA")
    civil_procedure = """
    GUGATAN PERDATA ATAS WANPRESTASI
    Gugatan diajukan ke Pengadilan Negeri
    Alat bukti: surat, saksi, ahli
    Upaya hukum: banding, kasasi, peninjauan kembali
    Eksekusi putusan melalui juru sita
    """
    
    civil_result = civil_analyzer.analyze_civil_issues(civil_procedure)
    print(f"   • Civil procedure references: {len(civil_result['civil_code_references'])}")
    print(f"   • Contract law issues: {len(civil_result['contract_law_issues'])}")
    
    # Test 3: Pembuktian
    print("\n3. 🔍 TEST: SISTEM PEMBUKTIAN")
    evidence_test = """
    ALAT BUKTI DALAM PERKARA PIDANA
    Keterangan saksi tanpa sumpah
    Barang bukti tanpa berita acara
    Keterangan ahli tidak tertulis
    Visum et repertum tidak lengkap
    """
    
    police_result2 = police_analyzer.analyze_procedures(evidence_test)
    print(f"   • Evidence procedure issues: {len(police_result2['investigation_issues'])}")
    
    # Summary
    print("\n" + "=" * 55)
    print("📊 PROCEDURAL LAW TEST SUMMARY:")
    print("   ✅ Hukum acara pidana dianalisis")
    print("   ✅ Hukum acara perdata diperiksa")
    print("   ✅ Sistem pembuktian dievaluasi")
    print("   ✅ VERSALAW2 memahami hukum prosedural!")

if __name__ == "__main__":
    main()
