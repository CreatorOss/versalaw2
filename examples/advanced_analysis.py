#!/usr/bin/env python3
"""
Advanced VERSALAW2 Usage Examples
Showing real-world integration patterns
"""

import versalaw2
import json
import csv
from datetime import datetime

class AdvancedContractAnalyzer:
    def __init__(self):
        self.analyzer = versalaw2
    
    def risk_assessment_dashboard(self, contracts):
        """Create a risk assessment dashboard"""
        print("🎯 CONTRACT RISK DASHBOARD")
        print("=" * 60)
        
        dashboard_data = {
            "total_contracts": len(contracts),
            "risk_breakdown": {"HIGH": 0, "MEDIUM": 0, "LOW": 0, "UNKNOWN": 0},
            "jurisdiction_breakdown": {},
            "high_risk_contracts": []
        }
        
        for name, text in contracts.items():
            result = self.analyzer.analyze_contract(text)
            
            # Update counters
            dashboard_data["risk_breakdown"][result['risk_level']] += 1
            
            jurisdiction = result['jurisdiction']
            dashboard_data["jurisdiction_breakdown"][jurisdiction] = \
                dashboard_data["jurisdiction_breakdown"].get(jurisdiction, 0) + 1
            
            # Track high risk contracts
            if result['risk_level'] == 'HIGH':
                dashboard_data["high_risk_contracts"].append({
                    "name": name,
                    "risk_score": result['risk_score'],
                    "issues": result.get('issues', [])[:3]  # First 3 issues
                })
        
        return dashboard_data
    
    def export_to_csv(self, results, filename="contract_analysis.csv"):
        """Export analysis results to CSV"""
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['contract_name', 'risk_level', 'risk_score', 'jurisdiction', 'issues_count', 'main_issues']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for name, result in results.items():
                writer.writerow({
                    'contract_name': name,
                    'risk_level': result['risk_level'],
                    'risk_score': result['risk_score'],
                    'jurisdiction': result['jurisdiction'],
                    'issues_count': len(result.get('issues', [])),
                    'main_issues': '; '.join(result.get('issues', [])[:2])  # First 2 issues
                })
        
        print(f"📊 CSV exported: {filename}")
    
    def continuous_monitoring(self, contract_text, threshold='MEDIUM'):
        """Simulate continuous contract monitoring"""
        print("🔍 CONTINUOUS CONTRACT MONITORING")
        print("-" * 40)
        
        result = self.analyzer.analyze_contract(contract_text)
        
        risk_levels = {'LOW': 1, 'MEDIUM': 2, 'HIGH': 3}
        current_risk = risk_levels.get(result['risk_level'], 0)
        threshold_risk = risk_levels.get(threshold, 2)
        
        if current_risk >= threshold_risk:
            print(f"🚨 ALERT: Contract exceeds {threshold} risk threshold!")
            print(f"   Current Risk: {result['risk_level']}")
            print(f"   Issues: {len(result.get('issues', []))}")
            return True
        else:
            print(f"✅ OK: Contract within acceptable risk limits")
            print(f"   Current Risk: {result['risk_level']}")
            return False

def demo_advanced_features():
    print("🚀 VERSALAW2 ADVANCED FEATURES DEMO")
    print("=" * 50)
    
    advanced_analyzer = AdvancedContractAnalyzer()
    
    # Sample contracts
    contracts = {
        "Employment_Contract_001": "Perjanjian kerja 5 tahun dengan denda 50% di Indonesia",
        "Software_License_002": "Software license with 10% penalty and 2-year term",
        "Partnership_Agreement_003": "Partnership agreement dengan bagi hasil 70-30%",
        "Service_Contract_004": "Service agreement with monthly payments and 30-day notice"
    }
    
    # 1. Dashboard
    print("\n1. 📈 RISK DASHBOARD")
    dashboard = advanced_analyzer.risk_assessment_dashboard(contracts)
    
    print(f"Total Contracts: {dashboard['total_contracts']}")
    print("Risk Breakdown:")
    for risk, count in dashboard['risk_breakdown'].items():
        print(f"  {risk}: {count}")
    
    print("Jurisdictions:")
    for juris, count in dashboard['jurisdiction_breakdown'].items():
        print(f"  {juris}: {count}")
    
    # 2. Export to CSV
    print("\n2. 💾 DATA EXPORT")
    results = {}
    for name, text in contracts.items():
        results[name] = versalaw2.analyze_contract(text)
    
    advanced_analyzer.export_to_csv(results)
    
    # 3. Continuous Monitoring
    print("\n3. 🔄 CONTINUOUS MONITORING")
    high_risk_contract = "Perjanjian dengan denda 100% dan jaminan tanah untuk 10 tahun"
    advanced_analyzer.continuous_monitoring(high_risk_contract, 'MEDIUM')
    
    low_risk_contract = "Simple agreement dengan notice period 30 hari"
    advanced_analyzer.continuous_monitoring(low_risk_contract, 'MEDIUM')

if __name__ == "__main__":
    demo_advanced_features()
