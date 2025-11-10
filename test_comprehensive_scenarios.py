#!/usr/bin/env python3
"""
VERSALAW2 Comprehensive Legal Scenarios Test
Menguji berbagai aspek hukum Indonesia yang kompleks
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from versalaw2 import VERSALAW2
from versalaw2.indonesian_law import IndonesianLawAnalyzer
from versalaw2.indonesian_law.hierarchy.constitutional_law import ConstitutionalLawAnalyzer
from versalaw2.indonesian_law.hierarchy.statutory_law import StatutoryLawAnalyzer
from versalaw2.indonesian_law.criminal_justice.police_regulations import PoliceRegulationsAnalyzer
from versalaw2.indonesian_law.professional_ethics.legal_ethics import LegalEthicsAnalyzer
from versalaw2.indonesian_law.specialized_law.civil_law import CivilLawAnalyzer

def main():
    print("🎯 VERSALAW2 COMPREHENSIVE LEGAL SCENARIOS TEST")
    print("=" * 65)
    print("Menguji berbagai aspek hukum Indonesia yang kompleks")
    print()
    
    # Initialize analyzers
    client = VERSALAW2()
    indo_analyzer = IndonesianLawAnalyzer()
    const_analyzer = ConstitutionalLawAnalyzer()
    stat_analyzer = StatutoryLawAnalyzer()
    police_analyzer = PoliceRegulationsAnalyzer()
    ethics_analyzer = LegalEthicsAnalyzer()
    civil_analyzer = CivilLawAnalyzer()
    
    # SCENARIO 1: Hukum Konstitusional - Hak Asasi Manusia
    print("1. 🏛️ SCENARIO: HUKUM KONSTITUSIONAL - HAK ASASI MANUSIA")
    print("-" * 55)
    
    constitutional_case = """
    PERATURAN DAERAH TENTANG PEMBATASAN KEBEBASAN BERKumpul
    Pasal 1: Dilarang melakukan kegiatan berkumpul tanpa izin
    Pasal 2: Pembatasan berlaku untuk kegiatan politik
    Pasal 3: Sanksi pidana bagi pelanggar
    """
    
    const_result = const_analyzer.analyze_compliance(constitutional_case)
    print(f"   • Rights violations: {len(const_result['rights_violations'])}")
    print(f"   • Constitutional issues: {len(const_result['constitutional_issues'])}")
    
    if const_result['rights_violations']:
        for violation in const_result['rights_violations']:
            print(f"     ⚠️  {violation['right']}: {violation['issue']}")
    
    # SCENARIO 2: Hukum Pidana - Proses Penyidikan
    print("\n2. 👮 SCENARIO: HUKUM PIDANA - PROSES PENYIDIKAN")
    print("-" * 55)
    
    criminal_case = """
    PROSES PENYIDIKAN TINDAK PIDANA KORUPSI
    Penyidik melakukan penyidikan tanpa surat perintah
    Berita acara pemeriksaan tidak dibuat dengan benar
    Tersangka tidak didampingi pengacara
    Penggeledahan dilakukan tanpa saksi
    """
    
    police_result = police_analyzer.analyze_procedures(criminal_case)
    print(f"   • PERKAP violations: {len(police_result['perkap_compliance'])}")
    print(f"   • Investigation issues: {len(police_result['investigation_issues'])}")
    
    if police_result['investigation_issues']:
        for issue in police_result['investigation_issues'][:3]:
            print(f"     ⚠️  {issue['procedure']} dalam konteks {issue['context']}")
    
    # SCENARIO 3: Hukum Perdata - Kontrak Kompleks
    print("\n3. 📝 SCENARIO: HUKUM PERDATA - KONTRAK KOMPLEKS")
    print("-" * 55)
    
    civil_contract = """
    PERJANJIAN INVESTASI PROPERTI BERDASARKAN KUH PERDATA
    Nilai investasi: Rp 50.000.000.000
    Jangka waktu: 60 bulan
    Denda: 100% untuk wanprestasi
    Jaminan: Sertifikat Hak Milik dan Hak Guna Bangunan
    Force majeure: Berlaku untuk bencana alam
    Penyelesaian sengketa: Arbitrase
    """
    
    civil_result = civil_analyzer.analyze_civil_issues(civil_contract)
    core_result = client.analyze_contract(civil_contract)
    
    print(f"   • Civil code references: {len(civil_result['civil_code_references'])}")
    print(f"   • Contract risk: {core_result['risk_level']} (score: {core_result['risk_score']})")
    print(f"   • Issues detected: {len(core_result['issues'])}")
    
    # SCENARIO 4: Etika Profesi Hukum
    print("\n4. ⚖️ SCENARIO: ETIKA PROFESI HUKUM")
    print("-" * 55)
    
    ethics_case = """
    PENGACARA MEWAKILI DUA PIHAK YANG BERTENTANGAN
    Terdapat benturan kepentingan dalam penanganan kasus
    Dokumen rahasia klien diungkapkan kepada pihak lawan
    Pengacara menerima gratifikasi dari klien
    """
    
    ethics_result = ethics_analyzer.analyze_conduct(ethics_case, "pengacara")
    print(f"   • Conflict of interest: {len(ethics_result['conflict_of_interest'])}")
    print(f"   • Confidentiality breaches: {len(ethics_result['confidentiality_issues'])}")
    print(f"   • Ethics violations: {len(ethics_result['ethics_compliance'])}")
    
    if ethics_result['conflict_of_interest']:
        for conflict in ethics_result['conflict_of_interest']:
            print(f"     ⚠️  {conflict['issue']}")
    
    # SCENARIO 5: Analisis Terintegrasi - Dokumen Kompleks
    print("\n5. 🔄 SCENARIO: ANALISIS TERINTEGRASI - DOKUMEN KOMPLEKS")
    print("-" * 55)
    
    complex_document = """
    RANCANGAN PERATURAN DAERAH TENTANG PENGELOLAAN LINGKUNGAN HIDUP
    
    DASAR HUKUM:
    - UUD 1945 Pasal 28H tentang Hak atas Lingkungan Hidup yang Baik
    - UU No. 32 Tahun 2009 tentang Perlindungan dan Pengelolaan Lingkungan Hidup
    - PERDA No. 5 Tahun 2018 tentang Ketertiban Umum
    
    PASAL 1: Setiap kegiatan usaha wajib memiliki AMDAL
    PASAL 2: Pembatasan hak masyarakat untuk protes dampak lingkungan
    PASAL 3: Sanksi pidana bagi pelaku pencemaran lingkungan
    PASAL 4: Penyidikan oleh penyidik pegawai negeri sipil
    PASAL 5: Keterangan ahli lingkungan sebagai alat bukti
    """
    
    integrated_result = indo_analyzer.comprehensive_analysis(complex_document)
    core_analysis = client.analyze_contract(complex_document)
    
    print("   📊 COMPLIANCE SUMMARY:")
    print(f"     • Constitutional: {integrated_result['compliance_summary']['constitutional_compliance']}")
    print(f"     • Statutory: {integrated_result['compliance_summary']['statutory_compliance']}")
    print(f"     • Overall risk: {integrated_result['compliance_summary']['overall_risk']}")
    print(f"     • Core risk: {core_analysis['risk_level']} (score: {core_analysis['risk_score']})")
    
    # Recommendations
    print("\n6. 💡 REKOMENDASI DAN TEMUAN UTAMA")
    print("-" * 55)
    
    if integrated_result['recommendations']:
        for rec in integrated_result['recommendations']:
            print(f"   • [{rec['priority'].upper()}] {rec['message']}")
    
    # Summary
    print("\n" + "=" * 65)
    print("📈 TEST SUMMARY:")
    print(f"   • Constitutional analysis: {len(const_result['rights_violations'])} HAM issues")
    print(f"   • Criminal procedure: {len(police_result['investigation_issues'])} investigation issues")
    print(f"   • Civil law: {len(civil_result['civil_code_references'])} KUH Perdata references")
    print(f"   • Professional ethics: {len(ethics_result['conflict_of_interest'])} conflict issues")
    print(f"   • Integrated compliance: {integrated_result['compliance_summary']['overall_risk']} risk")
    
    print("\n🎉 VERSALAW2 BERHASIL MENGANALISIS BERBAGAI ASPEK HUKUM INDONESIA!")
    print("   Platform siap untuk analisis hukum yang kompleks! 🚀")

if __name__ == "__main__":
    main()
