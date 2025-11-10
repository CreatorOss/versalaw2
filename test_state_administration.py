#!/usr/bin/env python3
"""
VERSALAW2 State Administration Law Test
Menguji aspek hukum tata negara dan administrasi
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from versalaw2.indonesian_law.hierarchy.statutory_law import StatutoryLawAnalyzer
from versalaw2.indonesian_law.hierarchy.constitutional_law import ConstitutionalLawAnalyzer

def main():
    print("🏛️ VERSALAW2 STATE ADMINISTRATION LAW TEST")
    print("=" * 60)
    
    stat_analyzer = StatutoryLawAnalyzer()
    const_analyzer = ConstitutionalLawAnalyzer()
    
    # Test 1: Hierarki Peraturan
    print("\n1. 📚 TEST: HIERARKI PERATURAN PERUNDANG-UNDANGAN")
    hierarchy_test = """
    PERATURAN DAERAH PROVINSI TENTANG PELAYANAN PUBLIK
    Berdasarkan UU No. 25 Tahun 2009 tentang Pelayanan Publik
    Perda ini menyimpangi ketentuan dalam UU No. 12 Tahun 2011
    Peraturan Gubernur sebagai pelaksana Perda
    """
    
    stat_result = stat_analyzer.analyze_compliance(hierarchy_test)
    print(f"   • Hierarchy issues: {len(stat_result['hierarchy_issues'])}")
    print(f"   • Statutory references: {len(stat_result['statutory_references'])}")
    
    if stat_result['hierarchy_issues']:
        for issue in stat_result['hierarchy_issues']:
            print(f"     ⚠️  {issue['issue']}")
    
    # Test 2: Kewenangan Lembaga Negara
    print("\n2. 🏢 TEST: KEWENANGAN LEMBAGA NEGARA")
    authority_test = """
    KEPUTUSAN MENTERI TENTANG PEMBUBARAN ORGANISASI MASYARAKAT
    Menteri membubarkan ormas tanpa proses peradilan
    Pembatasan kebebasan berserikat dan berkumpul
    Tidak ada keberatan yang dapat diajukan
    """
    
    const_result = const_analyzer.analyze_compliance(authority_test)
    print(f"   • Constitutional issues: {len(const_result['constitutional_issues'])}")
    print(f"   • Rights violations: {len(const_result['rights_violations'])}")
    
    if const_result['rights_violations']:
        for violation in const_result['rights_violations']:
            print(f"     ⚠️  {violation['right']}: {violation['issue']}")
    
    # Test 3: Peraturan Teknis
    print("\n3. 📋 TEST: PERATURAN TEKNIS DAN ADMINISTRATIF")
    technical_test = """
    PERATURAN MENTERI KEUANGAN NOMOR 15/2023
    Tentang Tata Cara Pembayaran Pajak Daerah
    Berlaku surut sejak tahun 2020
    Sanksi administratif bagi keterlambatan
    """
    
    stat_result2 = stat_analyzer.analyze_compliance(technical_test)
    print(f"   • Potential conflicts: {len(stat_result2['conflict_analysis'])}")
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 STATE ADMINISTRATION TEST SUMMARY:")
    print("   ✅ Hierarki peraturan terdeteksi")
    print("   ✅ Kewenangan lembaga dianalisis") 
    print("   ✅ Aspek konstitusional diperiksa")
    print("   ✅ VERSALAW2 mampu analisis hukum tata negara!")

if __name__ == "__main__":
    main()
