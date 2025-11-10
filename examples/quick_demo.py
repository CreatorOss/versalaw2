#!/usr/bin/env python3
"""
VERSALAW2 Quick Demo
Demonstrasi cepat kemampuan analisis hukum VERSALAW2
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from versalaw2 import VERSALAW2

def main():
    print("⚖️  VERSALAW2 QUICK DEMO")
    print("=" * 50)
    print("Indonesian Legal AI Platform v2.0.0")
    print()
    
    # Initialize client
    client = VERSALAW2()
    
    # Demo contracts
    demo_contracts = [
        {
            "name": "📄 KONTRAK RENDAH RISIKO",
            "text": """PERJANJIAN KERJASAMA
Pasal 1: Para pihak setuju bekerjasama dalam pertukaran informasi.
Pasal 2: Kerjasama berlangsung selama 12 bulan.
Pasal 3: Tidak ada denda yang berlaku."""
        },
        {
            "name": "📄 KONTRAK MENENGAH RISIKO", 
            "text": """PERJANJIAN JASA KONSULTASI
Pasal 1: Nilai kontrak Rp 500.000.000.
Pasal 2: Denda 25% untuk keterlambatan penyelesaian.
Pasal 3: Confidentiality clause berlaku."""
        },
        {
            "name": "📄 KONTRAK TINGGI RISIKO",
            "text": """PERJANJIAN INVESTASI PROPERTI
Pasal 1: Nilai investasi Rp 10.000.000.000.
Pasal 2: Denda 100% untuk wanprestasi.
Pasal 3: Jaminan sertifikat tanah disertakan.
Pasal 4: Berlaku hukum Indonesia."""
        }
    ]
    
    for contract in demo_contracts:
        print(contract["name"])
        print("-" * 40)
        
        result = client.analyze_contract(contract["text"])
        
        # Display results dengan format yang rapi
        print(f"🎯 RISK LEVEL: {result['risk_level'].upper()}")
        print(f"📊 RISK SCORE: {result['risk_score']}")
        print(f"🌍 JURISDICTION: {result['jurisdiction']}")
        
        if result['issues']:
            print("⚠️  ISSUES:")
            for issue in result['issues']:
                print(f"   • {issue}")
        
        if result['risk_factors']:
            print("🔍 RISK FACTORS:")
            for factor in result['risk_factors'][:3]:  # Tampilkan max 3 faktor
                print(f"   • {factor}")
        
        if result['clauses']:
            print("📑 CLAUSES DETECTED:")
            for clause in result['clauses']:
                print(f"   • {clause}")
        
        print()
    
    print("=" * 50)
    print("✅ DEMO SELESAI! VERSALAW2 SIAP DIGUNAKAN!")
    print()
    print("📋 FITUR YANG BERFUNGSI:")
    print("   • Analisis tingkat risiko kontrak")
    print("   • Deteksi yurisdiksi hukum") 
    print("   • Identifikasi masalah potensial")
    print("   • Deteksi faktor risiko")
    print("   • Ekstraksi klausa kontrak")
    print()
    print("🚀 Untuk penggunaan lanjutan:")
    print("   python run_versalaw2.py")

if __name__ == "__main__":
    main()
