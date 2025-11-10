#!/usr/bin/env python3
"""
VERSALAW2 Demo Application
A real-world example of using versalaw2 for contract analysis
"""

import versalaw2
import json
import os
from datetime import datetime

class ContractAnalyzer:
    def __init__(self):
        self.version = "1.0.0"
        self.analyzer = versalaw2
    
    def analyze_single_contract(self, contract_text, contract_name="Unknown"):
        """Analyze a single contract"""
        print(f"🔍 Analyzing: {contract_name}")
        print("-" * 50)
        
        result = self.analyzer.analyze_contract(contract_text)
        
        # Display results
        print(f"📊 RISK ASSESSMENT:")
        print(f"   Level: {result['risk_level']}")
        print(f"   Score: {result['risk_score']}")
        print(f"   Jurisdiction: {result['jurisdiction']}")
        print(f"   Issues Found: {len(result.get('issues', []))}")
        
        # Show issues
        if result.get('issues'):
            print(f"   ⚠️  ISSUES:")
            for i, issue in enumerate(result['issues'], 1):
                print(f"      {i}. {issue}")
        
        print()
        return result
    
    def analyze_multiple_contracts(self, contracts_dict):
        """Analyze multiple contracts and compare"""
        print("📑 BATCH CONTRACT ANALYSIS")
        print("=" * 50)
        
        results = {}
        for name, text in contracts_dict.items():
            results[name] = self.analyze_single_contract(text, name)
        
        return results
    
    def generate_report(self, results, output_file="contract_analysis_report.json"):
        """Generate a detailed report"""
        report = {
            "generated_at": datetime.now().isoformat(),
            "analyzer_version": versalaw2.__version__,
            "total_contracts": len(results),
            "analysis_results": results
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"📄 Report saved: {output_file}")
        return report

def main():
    print("🎯 VERSALAW2 DEMO APPLICATION")
    print("=" * 50)
    print(f"Using VERSALAW2 version: {versalaw2.__version__}")
    print()
    
    analyzer = ContractAnalyzer()
    
    # Sample contracts for demonstration
    sample_contracts = {
        "High Risk Employment": """
        PERJANJIAN KERJA
        DIBUAT OLEH PT. EXAMPLE INDONESIA
        
        Pasal 1 - Masa Kerja
        Perjanjian ini berlaku untuk jangka waktu 7 (tujuh) tahun.
        
        Pasal 2 - Sanksi dan Denda
        Karyawan yang melanggar peraturan dikenakan denda sebesar 100% dari gaji bulanan.
        
        Pasal 3 - Jaminan
        Karyawan wajib menyerahkan jaminan berupa sertifikat tanah.
        
        Pasal 4 - Hukum yang Berlaku
        Perjanjian ini tunduk pada Hukum Republik Indonesia.
        """,
        
        "Medium Risk Software License": """
        SOFTWARE LICENSE AGREEMENT
        BETWEEN TECH CORP AND CLIENT LTD
        
        Clause 1 - Term
        This agreement is valid for 2 years with automatic renewal.
        
        Clause 2 - Payment
        License fee: $10,000 per year, payable quarterly.
        
        Clause 3 - Penalties
        Late payments incur 5% monthly penalty.
        
        Clause 4 - Confidentiality
        Both parties agree to maintain confidentiality.
        """,
        
        "Low Risk Service Agreement": """
        SERVICE LEVEL AGREEMENT
        BETWEEN SERVICE PROVIDER AND CLIENT
        
        Section 1 - Services
        Provider will deliver consulting services as described.
        
        Section 2 - Term
        Agreement duration: 1 year with 30 days notice for termination.
        
        Section 3 - Review
        This agreement may be reviewed quarterly by mutual consent.
        """,
        
        "International Business Contract": """
        INTERNATIONAL DISTRIBUTION AGREEMENT
        BETWEEN COMPANY A (USA) AND COMPANY B (SINGAPORE)
        
        Article 1 - Distribution Rights
        Company B granted exclusive distribution rights in Southeast Asia.
        
        Article 2 - Term and Renewal
        Initial term: 3 years with option to renew.
        
        Article 3 - Governing Law
        This agreement shall be governed by Singapore law.
        
        Article 4 - Arbitration
        Disputes shall be resolved through international arbitration.
        """
    }
    
    # Analyze all contracts
    results = analyzer.analyze_multiple_contracts(sample_contracts)
    
    # Generate summary
    print("📈 ANALYSIS SUMMARY")
    print("=" * 50)
    
    high_risk = sum(1 for r in results.values() if r['risk_level'] == 'HIGH')
    medium_risk = sum(1 for r in results.values() if r['risk_level'] == 'MEDIUM')
    low_risk = sum(1 for r in results.values() if r['risk_level'] == 'LOW')
    
    print(f"📊 Risk Distribution:")
    print(f"   HIGH Risk: {high_risk} contracts")
    print(f"   MEDIUM Risk: {medium_risk} contracts") 
    print(f"   LOW Risk: {low_risk} contracts")
    print()
    
    # Generate report
    analyzer.generate_report(results, "demo_analysis_report.json")
    
    print()
    print("✅ DEMO COMPLETED SUCCESSFULLY!")
    print("🎯 VERSALAW2 is ready for your real projects!")

if __name__ == "__main__":
    main()
