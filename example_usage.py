#!/usr/bin/env python3
"""
VERSALAW2 Usage Example
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the analyzers
from versalaw2.indonesian_law.specialized_law.anti_corruption import AntiCorruptionAnalyzer
from versalaw2.indonesian_law.specialized_law.terrorism_law import TerrorismLawAnalyzer
from versalaw2.international_law.international_treaties import InternationalTreatyAnalyzer

def main():
    print("🎯 VERSALAW2 USAGE EXAMPLE")
    print("=" * 50)
    
    # 1. Analyze corruption case
    print("\n1. 🏛️ ANALYZING CORRUPTION CASE:")
    corruption_analyzer = AntiCorruptionAnalyzer()
    corruption_case = {
        "melawan_hukum": True,
        "merugikan_keuangan_negara": True,
        "kerugian_negara": 5000000000,
        "penyalahgunaan_wewenang": True
    }
    corruption_result = corruption_analyzer.analyze_corruption_case(corruption_case)
    print(f"   • Violations: {len(corruption_result['corruption_elements'])}")
    print(f"   • Legal articles: {len(corruption_result['potential_articles'])}")
    
    # 2. Analyze terrorism case
    print("\n2. 🚨 ANALYZING TERRORISM CASE:")
    terrorism_analyzer = TerrorismLawAnalyzer()
    terrorism_case = {
        "perencanaan_terorisme": True,
        "pendanaan_terorisme": True
    }
    terrorism_result = terrorism_analyzer.analyze_terrorism_case(terrorism_case)
    print(f"   • Terrorism detected: {terrorism_result['terrorism_detected']}")
    print(f"   • Offenses: {len(terrorism_result['terrorism_offenses'])}")
    
    # 3. Analyze international treaty
    print("\n3. 🌐 ANALYZING INTERNATIONAL TREATY:")
    treaty_analyzer = InternationalTreatyAnalyzer()
    treaty_case = {
        "bilateral": True,
        "mengatur_materi_uu": True
    }
    treaty_result = treaty_analyzer.analyze_treaty_ratification(treaty_case)
    print(f"   • Treaty type: {treaty_result['treaty_type']}")
    print(f"   • Parliament approval: {treaty_result['parliament_approval']}")
    
    print("\n✅ VERSALAW2 USAGE EXAMPLE COMPLETED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
