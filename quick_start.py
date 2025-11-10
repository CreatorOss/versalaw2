#!/usr/bin/env python3
"""
VERSALAW2 Quick Start - Production Ready
"""
from versalaw2 import VERSALAW2
from versalaw2.indonesian_law import IndonesianLawAnalyzer

def main():
    print("🚀 VERSALAW2 QUICK START - PRODUCTION READY")
    print("=" * 50)
    
    # 1. Core Analysis
    print("\n1. 🔧 CORE CONTRACT ANALYSIS")
    client = VERSALAW2()
    
    contracts = [
        "Perjanjian kerjasama sederhana",
        "Kontrak dengan denda 50% untuk keterlambatan", 
        "Perjanjian investasi dengan denda 100% dan jaminan tanah"
    ]
    
    for contract in contracts:
        result = client.analyze_contract(contract)
        print(f"   '{contract[:30]}...' → Risk: {result['risk_level']}")
    
    # 2. Indonesian Law Analysis
    print("\n2. 🇮🇩 INDONESIAN LAW ANALYSIS")
    indo_analyzer = IndonesianLawAnalyzer()
    
    legal_doc = """
    Peraturan tentang ketertiban umum.
    Dilarang membatasi hak kebebasan berpendapat.
    Penyidikan dilakukan dengan berita acara.
    """
    
    result = indo_analyzer.comprehensive_analysis(legal_doc)
    print(f"   Constitutional: {result['compliance_summary']['constitutional_compliance']}")
    print(f"   Statutory: {result['compliance_summary']['statutory_compliance']}")
    print(f"   Overall Risk: {result['compliance_summary']['overall_risk']}")
    
    print("\n" + "=" * 50)
    print("🎉 VERSALAW2 PRODUCTION READY!")
    print("   All systems operational! 🚀")

if __name__ == "__main__":
    main()
