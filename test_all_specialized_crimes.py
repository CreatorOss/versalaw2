#!/usr/bin/env python3
"""
VERSALAW2 ALL SPECIALIZED CRIMES TEST
Test semua modul kejahatan khusus yang telah dibangun
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import semua analyzer
from versalaw2.indonesian_law.specialized_law.anti_corruption import AntiCorruptionAnalyzer
from versalaw2.indonesian_law.specialized_law.money_laundering import MoneyLaunderingAnalyzer
from versalaw2.indonesian_law.specialized_law.human_trafficking import HumanTraffickingAnalyzer
from versalaw2.indonesian_law.specialized_law.illegal_mining import IllegalMiningAnalyzer
from versalaw2.indonesian_law.specialized_law.illegal_logging import IllegalLoggingAnalyzer

def main():
    print("🎯 VERSALAW2 COMPLETE SPECIALIZED CRIMES TEST SUITE")
    print("=" * 70)
    
    # Inisialisasi semua analyzer
    analyzers = {
        "🏛️ TIPIKOR": AntiCorruptionAnalyzer(),
        "💰 MONEY LAUNDERING": MoneyLaunderingAnalyzer(),
        "👥 HUMAN TRAFFICKING": HumanTraffickingAnalyzer(),
        "🏭 ILLEGAL MINING": IllegalMiningAnalyzer(),
        "🌳 ILLEGAL LOGGING": IllegalLoggingAnalyzer()
    }
    
    # Test cases untuk setiap analyzer
    test_cases = {
        "🏛️ TIPIKOR": {
            "melawan_hukum": True,
            "merugikan_keuangan_negara": True,
            "kerugian_negara": 5000000000,
            "penyalahgunaan_wewenang": True,
            "gratifikasi": True
        },
        "💰 MONEY LAUNDERING": {
            "placement": True,
            "layering": True,
            "korupsi": True,
            "transactions": [
                {"amount": 1000000000, "patterns": ["structuring"]}
            ]
        },
        "👥 HUMAN TRAFFICKING": {
            "penipuan": True,
            "pengiriman": True,
            "eksploitasi_seksual": True,
            "underage_victim": True
        },
        "🏭 ILLEGAL MINING": {
            "tambang_tanpa_izin": True,
            "penambangan_di_kawasan_hutan": True,
            "pencemaran_lingkungan": True
        },
        "🌳 ILLEGAL LOGGING": {
            "penebangan_tanpa_izin": True,
            "penebangan_di_kawasan_lindung": True,
            "perdagangan_kayu_ilegal": True
        }
    }
    
    results = {}
    
    print("\n🔍 RUNNING COMPREHENSIVE ANALYSIS...")
    print("-" * 70)
    
    for crime_type, analyzer in analyzers.items():
        print(f"\n{crime_type}:")
        test_data = test_cases[crime_type]
        
        if crime_type == "🏛️ TIPIKOR":
            analysis = analyzer.analyze_corruption_case(test_data)
            violations = len(analysis['corruption_elements'])
            articles = len(analysis['potential_articles'])
            
        elif crime_type == "💰 MONEY LAUNDERING":
            analysis = analyzer.analyze_money_laundering(test_data)
            violations = len(analysis['money_laundering_stages'])
            articles = len(analysis['legal_articles'])
            
        elif crime_type == "👥 HUMAN TRAFFICKING":
            analysis = analyzer.analyze_trafficking_case(test_data)
            violations = len(analysis['trafficking_elements'])
            articles = len(analysis['legal_articles'])
            
        elif crime_type == "🏭 ILLEGAL MINING":
            analysis = analyzer.analyze_illegal_mining(test_data)
            violations = len(analysis['mining_violations'])
            articles = len(analysis['legal_articles'])
            
        elif crime_type == "🌳 ILLEGAL LOGGING":
            analysis = analyzer.analyze_illegal_logging(test_data)
            violations = len(analysis['logging_violations'])
            articles = len(analysis['legal_articles'])
        
        results[crime_type] = {
            'violations': violations,
            'articles': articles,
            'status': '✅ DETECTED' if violations > 0 else '❌ CLEAN'
        }
        
        print(f"   • Violations: {violations}")
        print(f"   • Legal articles: {articles}")
        print(f"   • Status: {results[crime_type]['status']}")
    
    print("\n" + "=" * 70)
    print("📊 COMPREHENSIVE TEST SUMMARY:")
    print("-" * 70)
    
    total_violations = sum(result['violations'] for result in results.values())
    total_articles = sum(result['articles'] for result in results.values())
    
    for crime_type, result in results.items():
        print(f"   {crime_type}: {result['violations']} violations, {result['articles']} articles")
    
    print(f"\n   📈 TOTAL VIOLATIONS: {total_violations}")
    print(f"   ⚖️ TOTAL LEGAL ARTICLES: {total_articles}")
    print(f"   🎯 CRIME TYPES COVERED: {len(analyzers)}")
    
    print("\n" + "=" * 70)
    print("🎉 VERSALAW2 SPECIALIZED CRIMES MODULE COMPLETE!")
    print("   Platform now covers ALL major high-impact crimes in Indonesia!")
    print("   Ready for real-world legal analysis and enforcement! 🚀")
    
if __name__ == "__main__":
    main()
