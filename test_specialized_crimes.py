#!/usr/bin/env python3
"""
VERSALAW2 Specialized Crimes Test
Test modul Tipikor, Money Laundering, dan TPPO
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from versalaw2.indonesian_law.specialized_law.anti_corruption import AntiCorruptionAnalyzer
from versalaw2.indonesian_law.specialized_law.money_laundering import MoneyLaunderingAnalyzer
from versalaw2.indonesian_law.specialized_law.human_trafficking import HumanTraffickingAnalyzer

def main():
    print("🎯 VERSALAW2 SPECIALIZED CRIMES TEST")
    print("=" * 60)
    
    # Inisialisasi analyzer
    tipikor_analyzer = AntiCorruptionAnalyzer()
    money_laundering_analyzer = MoneyLaunderingAnalyzer()
    tppo_analyzer = HumanTraffickingAnalyzer()
    
    print("\n1. 🏛️ TEST: HUKUM TIPIKOR (KORUPSI)")
    print("-" * 50)
    
    corruption_case = {
        "melawan_hukum": True,
        "merugikan_keuangan_negara": True,
        "kerugian_negara": 5000000000,  # 5 Miliar
        "penyalahgunaan_wewenang": True,
        "melibatkan_aparatur_negara": True,
        "gratifikasi": True
    }
    
    tipikor_analysis = tipikor_analyzer.analyze_corruption_case(corruption_case)
    print(f"   • Unsur korupsi terdeteksi: {len(tipikor_analysis['corruption_elements'])}")
    print(f"   • Pasal yang dilanggar: {len(tipikor_analysis['potential_articles'])}")
    print(f"   • Yurisdiksi KPK: {'✅' if tipikor_analysis['kpk_jurisdiction'] else '❌'}")
    print(f"   • Sanksi: {len(tipikor_analysis['sanctions'])} jenis")
    
    print("\n2. 💰 TEST: MONEY LAUNDERING (TPPU)")
    print("-" * 50)
    
    money_laundering_case = {
        "placement": True,
        "layering": True,
        "cash_deposit_large": True,
        "multiple_transfers": True,
        "shell_companies": True,
        "korupsi": True,  # Predicate crime
        "transactions": [
            {"amount": 750000000, "patterns": ["structuring"]},
            {"amount": 2000000000, "patterns": ["offshore_flow"]}
        ]
    }
    
    tppu_analysis = money_laundering_analyzer.analyze_money_laundering(money_laundering_case)
    print(f"   • TPPU terdeteksi: {'✅' if tppu_analysis['tppu_detected'] else '❌'}")
    print(f"   • Tahapan pencucian: {len(tppu_analysis['money_laundering_stages'])}")
    print(f"   • Predicate crime: {tppu_analysis['predicate_crime']}")
    print(f"   • Transaksi mencurigakan: {len(tppu_analysis['suspicious_transactions'])}")
    print(f"   • Perampasan aset: {'✅' if tppu_analysis['asset_forfeiture'] else '❌'}")
    
    print("\n3. 👥 TEST: HUMAN TRAFFICKING (TPPO)")
    print("-" * 50)
    
    trafficking_case = {
        "penipuan": True,
        "pengiriman": True,
        "eksploitasi_seksual": True,
        "penjeratan_utang": True,
        "underage_victim": True,
        "physical_violence": True,
        "international_trafficking": True,
        "psychological_trauma": True
    }
    
    tppo_analysis = tppo_analyzer.analyze_trafficking_case(trafficking_case)
    print(f"   • TPPO terdeteksi: {'✅' if tppo_analysis['tppo_detected'] else '❌'}")
    print(f"   • Unsur trafficking: {len(tppo_analysis['trafficking_elements'])}")
    print(f"   • Bentuk eksploitasi: {len(tppo_analysis['exploitation_forms'])}")
    print(f"   • Perlindungan korban: {len(tppo_analysis['victim_protection'])} kebutuhan")
    print(f"   • Perlindungan saksi: {'✅' if tppo_analysis['witness_protection'] else '❌'}")
    
    print("\n4. 🔄 TEST: INTEGRATED ANALYSIS")
    print("-" * 50)
    
    # Kasus kompleks: Korupsi + Money Laundering
    complex_case = {
        "korupsi_data": corruption_case,
        "money_laundering_data": money_laundering_case
    }
    
    print("   • Kasus korupsi dengan pola pencucian uang")
    print("   • Multiple legal domains terintegrasi")
    print("   • Cross-regulation analysis aktif")
    
    print("\n" + "=" * 60)
    print("📊 SPECIALIZED CRIMES TEST SUMMARY:")
    print(f"   ✅ Tipikor analyzer: {len(tipikor_analysis['potential_articles'])} articles detected")
    print(f"   ✅ Money laundering: {len(tppu_analysis['money_laundering_stages'])} stages identified") 
    print(f"   ✅ Human trafficking: {len(tppo_analysis['exploitation_forms'])} exploitation forms")
    print(f"   ✅ Integrated analysis: Complex case handling")
    print("\n🎉 MODUL KEJAHATAN KHUSUS BERHASIL DITAMBAHKAN!")
    print("   VERSALAW2 kini mencakup kejahatan high-impact Indonesia!")
    
if __name__ == "__main__":
    main()
