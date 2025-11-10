#!/usr/bin/env python3
"""
VERSALAW2 NEW SPECIALIZED CRIMES TEST
Test modul narkoba, penyeludupan, dan cyber crime
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from versalaw2.indonesian_law.specialized_law.narcotics import NarcoticsAnalyzer
from versalaw2.indonesian_law.specialized_law.smuggling import SmugglingAnalyzer
from versalaw2.indonesian_law.specialized_law.cyber_crime import CyberCrimeAnalyzer

def main():
    print("🆕 VERSALAW2 NEW SPECIALIZED CRIMES TEST")
    print("=" * 60)
    
    # Inisialisasi analyzer baru
    narcotics_analyzer = NarcoticsAnalyzer()
    smuggling_analyzer = SmugglingAnalyzer()
    cyber_analyzer = CyberCrimeAnalyzer()
    
    print("\n1. 💊 TEST: NARKOTIKA CASE")
    print("-" * 50)
    
    narcotics_case = {
        "narcotic_type": "sabu",
        "quantity": 250,  # gram
        "unit": "gram",
        "peredaran_narkotika": True,
        "kepemilikan_narkotika": True,
        "involved_minors": False,
        "international_network": True,
        "addicted_user": False
    }
    
    narcotics_analysis = narcotics_analyzer.analyze_narcotics_case(narcotics_case)
    print(f"   • Narkotika terdeteksi: {'✅' if narcotics_analysis['narcotics_detected'] else '❌'}")
    print(f"   • Kategori: {narcotics_analysis['narcotics_category']}")
    print(f"   • Pelanggaran: {len(narcotics_analysis['offenses_detected'])}")
    print(f"   • Pasal hukum: {len(narcotics_analysis['legal_articles'])}")
    print(f"   • Sanksi: {len(narcotics_analysis['sanctions'])} jenis")
    print(f"   • Rehabilitasi mungkin: {'✅' if narcotics_analysis['rehabilitation_possible'] else '❌'}")
    
    print("\n2. 🚢 TEST: PENYELUDUPAN CASE")
    print("-" * 50)
    
    smuggling_case = {
        "barang_terlarang": True,
        "narkotika": True,
        "false_declaration": True,
        "undeclared_goods": True,
        "goods_value": 5000000000,  # 5 Miliar
        "organized_smuggling": True
    }
    
    smuggling_analysis = smuggling_analyzer.analyze_smuggling_case(smuggling_case)
    print(f"   • Penyeludupan terdeteksi: {'✅' if smuggling_analysis['smuggling_detected'] else '❌'}")
    print(f"   • Barang terlarang: {len(smuggling_analysis['prohibited_goods_detected'])}")
    print(f"   • Pelanggaran bea cukai: {len(smuggling_analysis['customs_violations'])}")
    print(f"   • Pasal hukum: {len(smuggling_analysis['legal_articles'])}")
    print(f"   • Bea cukai: Rp {smuggling_analysis['customs_duties']:,}")
    print(f"   • Pertanggungjawaban pidana: {'✅' if smuggling_analysis['criminal_liability'] else '❌'}")
    
    print("\n3. 💻 TEST: CYBER CRIME CASE")
    print("-" * 50)
    
    cyber_case = {
        "peretasan": True,
        "akses_ilegal": True,
        "penipuan_daring": True,
        "pelanggaran_data_pribadi": True,
        "data_breach": True,
        "affected_records": 10000,
        "sensitive_data": True,
        "cross_border_attack": True
    }
    
    cyber_analysis = cyber_analyzer.analyze_cyber_crime(cyber_case)
    print(f"   • Kejahatan siber terdeteksi: {'✅' if cyber_analysis['cyber_crime_detected'] else '❌'}")
    print(f"   • Pelanggaran siber: {len(cyber_analysis['cyber_offenses'])}")
    print(f"   • Pelanggaran data: {len(cyber_analysis['data_violations'])}")
    print(f"   • Pasal hukum: {len(cyber_analysis['legal_articles'])}")
    print(f"   • Bukti digital: {len(cyber_analysis['digital_evidence'])} jenis")
    print(f"   • Masalah yurisdiksi: {len(cyber_analysis['jurisdictional_issues'])}")
    
    print("\n4. 🔄 TEST: ADVANCED ANALYSIS")
    print("-" * 50)
    
    # Test jaringan narkotika
    network_data = {
        "international_connections": True,
        "large_cash_transactions": True,
        "shell_companies": True,
        "cross_border": True
    }
    
    network_analysis = narcotics_analyzer.analyze_drug_trafficking_network(network_data)
    print(f"   • Jaringan narkotika: {network_analysis['network_scale']} scale")
    print(f"   • Money laundering risk: {'✅' if network_analysis['money_laundering_risk'] else '❌'}")
    print(f"   • Rekomendasi penegakan: {len(network_analysis['enforcement_recommendations'])}")
    
    # Test compliance kepabeanan
    compliance_data = {
        "late_declarations": True,
        "classification_errors": True,
        "high_value_goods": True
    }
    
    compliance_analysis = smuggling_analyzer.analyze_customs_compliance(compliance_data)
    print(f"   • Skor compliance: {compliance_analysis['compliance_score']}/100")
    print(f"   • Prioritas audit: {compliance_analysis['audit_priority']}")
    
    # Test incident response
    incident_data = {
        "data_breach": True,
        "affected_records": 50000,
        "sensitive_data": True,
        "financial_loss": 2000000000
    }
    
    incident_analysis = cyber_analyzer.analyze_incident_response(incident_data)
    print(f"   • Severity insiden: {incident_analysis['incident_severity']}")
    print(f"   • Kewajiban hukum: {len(incident_analysis['legal_obligations'])}")
    
    print("\n" + "=" * 60)
    print("📊 NEW CRIMES TEST SUMMARY:")
    print(f"   ✅ Narcotics: {len(narcotics_analysis['legal_articles'])} articles")
    print(f"   ✅ Smuggling: {len(smuggling_analysis['legal_articles'])} articles") 
    print(f"   ✅ Cyber Crime: {len(cyber_analysis['legal_articles'])} articles")
    print(f"   ✅ Advanced Analysis: Network, Compliance, Incident Response")
    print("\n🎉 3 MODUL KEJAHATAN BARU BERHASIL DITAMBAHKAN!")
    print("   VERSALAW2 semakin komprehensif!")
    
if __name__ == "__main__":
    main()
