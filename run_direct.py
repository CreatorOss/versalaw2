#!/usr/bin/env python3
"""
VERSALAW2 - Run Direct from Source
"""
import sys
import os

# Add current directory to Python path
sys.path.insert(0, '/root/dragon/global/versalaw2')

def main():
    print("🚀 VERSALAW2 - RUNNING DIRECT FROM SOURCE")
    print("=" * 50)
    
    try:
        # Import langsung dari source
        from versalaw2.core import VERSALAW2
        from versalaw2.indonesian_law import IndonesianLawAnalyzer
        
        print("✅ Semua modules berhasil diimport!")
        
        # Test core functionality
        print("\n1. 🔧 TESTING CORE VERSALAW2")
        client = VERSALAW2()
        
        test_contracts = [
            "Perjanjian kerjasama sederhana",
            "Kontrak dengan denda 50%",
            "Perjanjian investasi dengan jaminan tanah dan denda 100%"
        ]
        
        for contract in test_contracts:
            result = client.analyze_contract(contract)
            print(f"   '{contract}' → Risk: {result['risk_level']}")
        
        # Test Indonesian law
        print("\n2. 🇮🇩 TESTING INDONESIAN LAW")
        indo = IndonesianLawAnalyzer()
        result = indo.comprehensive_analysis("Sample legal text")
        print(f"   Integrated analysis working! Overall risk: {result['compliance_summary']['overall_risk']}")
        
        print("\n" + "=" * 50)
        print("🎉 VERSALAW2 BERJALAN SEMPURNA!")
        print("   Semua modul bekerja dengan baik! 🚀")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
