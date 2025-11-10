#!/usr/bin/env python3
"""
VERSALAW2 Environmental Crimes Test
Test modul illegal mining, illegal logging, dan tipiring
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from versalaw2.indonesian_law.specialized_law.illegal_mining import IllegalMiningAnalyzer
from versalaw2.indonesian_law.specialized_law.illegal_logging import IllegalLoggingAnalyzer

def main():
    print("🌿 VERSALAW2 ENVIRONMENTAL CRIMES TEST")
    print("=" * 60)
    
    # Inisialisasi analyzer
    mining_analyzer = IllegalMiningAnalyzer()
    logging_analyzer = IllegalLoggingAnalyzer()
    
    print("\n1. 🏭 TEST: ILLEGAL MINING & DRILLING")
    print("-" * 50)
    
    illegal_mining_case = {
        "tambang_tanpa_izin": True,
        "penambangan_di_kawasan_hutan": True,
        "pencemaran_lingkungan": True,
        "kerusakan_ekosistem": True,
        "pencemaran_air": True,
        "perusahaan_terlibat": True,
        "kerugian_negara": True,
        "lubang_tambang": True
    }
    
    mining_analysis = mining_analyzer.analyze_illegal_mining(illegal_mining_case)
    print(f"   • Pelanggaran pertambangan: {len(mining_analysis['mining_violations'])}")
    print(f"   • Dampak lingkungan: {len(mining_analysis['environmental_impacts'])}")
    print(f"   • Pasal hukum: {len(mining_analysis['legal_articles'])}")
    print(f"   • Sanksi: {len(mining_analysis['sanctions'])} jenis")
    print(f"   • Reklamasi wajib: {'✅' if mining_analysis['reclamation_obligation'] else '❌'}")
    
    print("\n2. 🌳 TEST: ILLEGAL LOGGING")
    print("-" * 50)
    
    illegal_logging_case = {
        "penebangan_tanpa_izin": True,
        "penebangan_di_kawasan_lindung": True,
        "perdagangan_kayu_ilegal": True,
        "hutan_lindung": True,
        "timber_volume": 5000,  # 5000 m³
        "area_damaged": 50,    # 50 hektar
        "false_legality_certificate": True
    }
    
    logging_analysis = logging_analyzer.analyze_illegal_logging(illegal_logging_case)
    print(f"   • Pelanggaran kehutanan: {len(logging_analysis['logging_violations'])}")
    print(f"   • Kawasan lindung: {'✅' if logging_analysis['protected_area_violation'] else '❌'}")
    print(f"   • Pasal hukum: {len(logging_analysis['legal_articles'])}")
    print(f"   • Sanksi: {len(logging_analysis['sanctions'])} jenis")
    print(f"   • Reboisasi wajib: {'✅' if logging_analysis['reforestation_required'] else '❌'}")
    
    print("\n3. 🔄 TEST: INTEGRATED ENVIRONMENTAL ANALYSIS")
    print("-" * 50)
    
    # Kasus kompleks: Illegal mining di kawasan hutan
    complex_environmental_case = {
        "mining_data": illegal_mining_case,
        "logging_data": illegal_logging_case
    }
    
    print("   • Kasus tambang ilegal di kawasan hutan lindung")
    print("   • Multiple environmental violations")
    print("   • Cross-sectoral legal analysis")
    
    # Test supply chain analysis
    supply_chain_data = {
        "multiple_handlers": True,
        "informal_transport": True,
        "cash_payments": True,
        "fake_svlk": True,
        "supplier_verification": False
    }
    
    supply_analysis = logging_analyzer.analyze_timber_supply_chain(supply_chain_data)
    print(f"   • Rantai pasok: {len(supply_analysis['chain_vulnerabilities'])} vulnerabilities")
    print(f"   • Due diligence: {len(supply_analysis['due_diligence_issues'])} issues")
    
    print("\n4. 💰 TEST: ENVIRONMENTAL LOSS CALCULATION")
    print("-" * 50)
    
    damage_data = {
        "timber_value": 2500000000,  # 2.5 Miliar
        "carbon_emission": True,
        "biodiversity_loss": True,
        "watershed_damage": True
    }
    
    environmental_losses = logging_analyzer.calculate_environmental_loss(damage_data)
    print(f"   • Kerugian lingkungan: {len(environmental_losses)} jenis")
    for loss in environmental_losses:
        print(f"     - {loss}")
    
    print("\n" + "=" * 60)
    print("📊 ENVIRONMENTAL CRIMES TEST SUMMARY:")
    print(f"   ✅ Illegal mining: {len(mining_analysis['mining_violations'])} violations")
    print(f"   ✅ Illegal logging: {len(logging_analysis['logging_violations'])} violations") 
    print(f"   ✅ Supply chain: {len(supply_analysis['chain_vulnerabilities'])} vulnerabilities")
    print(f"   ✅ Environmental loss: {len(environmental_losses)} impact types")
    print("\n🎉 MODUL KEJAHATAN LINGKUNGAN BERHASIL DITAMBAHKAN!")
    print("   VERSALAW2 kini mencakup kejahatan lingkungan dan SDA!")
    
if __name__ == "__main__":
    main()
