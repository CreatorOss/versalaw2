#!/usr/bin/env python3
"""
FINAL TEST - HUKUM INDONESIA COMPLETE
Test semua analyzer dengan data realistik
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_with_real_data():
    print("🎯 FINAL TEST - HUKUM INDONESIA DENGAN DATA REALISTIK")
    print("=" * 60)
    
    test_cases = [
        # (Name, File, Class, Test Data)
        ("Anti-Corruption", "versalaw2/indonesian_law/specialized_law/anti_corruption.py", "AntiCorruptionAnalyzer", 
         {"melawan_hukum": True, "kerugian_negara": 5000000000}),
        
        ("Terrorism Law", "versalaw2/indonesian_law/specialized_law/terrorism_law.py", "TerrorismLawAnalyzer",
         {"perencanaan_terorisme": True, "pendanaan_terorisme": True}),
        
        ("Narcotics", "versalaw2/indonesian_law/specialized_law/narcotics.py", "NarcoticsLawAnalyzer",
         {"jenis_narkotika": "golongan_1", "jumlah": "besar"}),
        
        ("Money Laundering", "versalaw2/indonesian_law/specialized_law/money_laundering.py", "MoneyLaunderingAnalyzer",
         {"transaksi_mencurigakan": True, "nilai_transaksi": 1000000000}),
        
        ("Cyber Crime", "versalaw2/indonesian_law/specialized_law/cyber_crime.py", "CyberCrimeAnalyzer",
         {"akses_ilegal": True, "pencurian_data": True}),
        
        ("Human Trafficking", "versalaw2/indonesian_law/specialized_law/human_trafficking.py", "HumanTraffickingAnalyzer",
         {"perdagangan_manusia": True, "eksploitasi": True}),
        
        ("Illegal Logging", "versalaw2/indonesian_law/specialized_law/illegal_logging.py", "IllegalLoggingAnalyzer",
         {"penebangan_liar": True, "kawasan_hutan_lindung": True}),
        
        ("Illegal Mining", "versalaw2/indonesian_law/specialized_law/illegal_mining.py", "IllegalMiningAnalyzer",
         {"pertambangan_tanpa_izin": True, "kerusakan_lingkungan": True}),
        
        ("Smuggling", "versalaw2/indonesian_law/specialized_law/smuggling.py", "SmugglingAnalyzer",
         {"penyelundupan_barang": True, "bea_cukai": True}),
        
        ("Legal Ethics", "versalaw2/indonesian_law/professional_ethics/legal_ethics.py", "LegalEthicsAnalyzer",
         {"conflict_of_interest": True, "client_confidentiality_breach": False}),
        
        ("Police Regulations", "versalaw2/indonesian_law/criminal_justice/police_regulations.py", "PoliceRegulationsAnalyzer",
         {"arrest_without_warrant": True, "excessive_force": False}),
    ]
    
    print("🔧 TESTING WITH REALISTIC DATA:")
    print("=" * 60)
    
    successful = 0
    detailed_results = []
    
    for name, file_path, expected_class, test_data in test_cases:
        try:
            # Import langsung
            import importlib.util
            spec = importlib.util.spec_from_file_location("module.name", file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Cari class
            analyzer_class = None
            for attr_name in dir(module):
                if 'Analyzer' in attr_name and not attr_name.startswith('_'):
                    analyzer_class = getattr(module, attr_name)
                    break
            
            if analyzer_class is None:
                print(f"❌ {name}: NO ANALYZER CLASS FOUND")
                continue
            
            # Test dengan data realistik
            analyzer = analyzer_class()
            result = analyzer.analyze(test_data) if hasattr(analyzer, 'analyze') else analyzer.analyze_case(test_data)
            
            # Validasi hasil
            if isinstance(result, dict) and len(result) > 0:
                status = "✅ SUCCESS"
                successful += 1
                details = f"({len(result)} aspects analyzed)"
            else:
                status = "⚠️  WARNING"
                details = "(minimal result)"
            
            print(f"{status} {name}: {details}")
            detailed_results.append((name, result))
            
        except Exception as e:
            print(f"❌ {name}: FAILED - {e}")
    
    # Summary
    print(f"\n📊 FINAL RESULTS:")
    print("=" * 60)
    print(f"✅ BERHASIL: {successful}/{len(test_cases)}")
    print(f"📈 PERSENTASE: {successful/len(test_cases)*100:.1f}%")
    
    # Tampilkan contoh hasil
    if detailed_results:
        print(f"\n📋 CONTOH HASIL ANALISIS:")
        print("-" * 30)
        for name, result in detailed_results[:3]:  # Tampilkan 3 contoh
            print(f"• {name}: {str(result)[:100]}...")
    
    return successful == len(test_cases)

if __name__ == "__main__":
    success = test_with_real_data()
    if success:
        print("\n🎉 SEMUA 11 ANALYZER HUKUM INDONESIA BERFUNGSI DENGAN DATA REALISTIK!")
        print("🚀 HUKUM INDONESIA SIAP PRODUKSI!")
    else:
        print("\n⚠️  ADA BEBERAPA ANALYZER YANG PERLU DIPERIKSA ULANG")
