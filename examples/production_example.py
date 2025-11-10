#!/usr/bin/env python3
"""
Production-Ready VERSALAW2 Implementation
Example for enterprise use
"""

import versalaw2
import pandas as pd
from typing import Dict, List
import json
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EnterpriseContractAnalyzer:
    """Production-grade contract analyzer using VERSALAW2"""
    
    def __init__(self):
        self.analyzer = versalaw2
        self.supported_jurisdictions = ['INDONESIA', 'INTERNATIONAL', 'SINGAPORE']
    
    def analyze_contract_batch(self, contracts: Dict[str, str]) -> pd.DataFrame:
        """Analyze multiple contracts and return DataFrame"""
        logger.info(f"Analyzing {len(contracts)} contracts...")
        
        results = []
        for name, text in contracts.items():
            try:
                analysis = self.analyzer.analyze_contract(text)
                
                result_row = {
                    'contract_id': name,
                    'contract_text_preview': text[:100] + '...' if len(text) > 100 else text,
                    'risk_level': analysis['risk_level'],
                    'risk_score': analysis.get('risk_score', 0),
                    'jurisdiction': analysis['jurisdiction'],
                    'issues_count': len(analysis.get('issues', [])),
                    'main_issues': ' | '.join(analysis.get('issues', [])[:2]),
                    'analysis_timestamp': pd.Timestamp.now()
                }
                results.append(result_row)
                
                logger.info(f"✓ {name}: {analysis['risk_level']} risk")
                
            except Exception as e:
                logger.error(f"✗ Failed to analyze {name}: {e}")
                results.append({
                    'contract_id': name,
                    'error': str(e),
                    'analysis_timestamp': pd.Timestamp.now()
                })
        
        return pd.DataFrame(results)
    
    def generate_risk_report(self, df: pd.DataFrame) -> Dict:
        """Generate comprehensive risk report"""
        if df.empty:
            return {"error": "No data to analyze"}
        
        # Risk distribution
        risk_dist = df['risk_level'].value_counts().to_dict()
        
        # Jurisdiction distribution
        juris_dist = df['jurisdiction'].value_counts().to_dict()
        
        # High risk contracts
        high_risk = df[df['risk_level'] == 'HIGH'][['contract_id', 'risk_score', 'main_issues']].to_dict('records')
        
        report = {
            "summary": {
                "total_contracts": len(df),
                "high_risk_count": len(high_risk),
                "risk_distribution": risk_dist,
                "jurisdiction_distribution": juris_dist
            },
            "high_risk_contracts": high_risk,
            "recommendations": self._generate_recommendations(df)
        }
        
        return report
    
    def _generate_recommendations(self, df: pd.DataFrame) -> List[str]:
        """Generate business recommendations based on analysis"""
        recommendations = []
        
        high_risk_count = len(df[df['risk_level'] == 'HIGH'])
        if high_risk_count > 0:
            recommendations.append(f"🚨 Review {high_risk_count} high-risk contracts with legal team")
        
        unknown_juris = len(df[df['jurisdiction'] == 'UNKNOWN'])
        if unknown_juris > 0:
            recommendations.append(f"🔍 Clarify jurisdiction for {unknown_juris} contracts")
        
        avg_risk_score = df['risk_score'].mean()
        if avg_risk_score > 5:
            recommendations.append("⚖️ Consider implementing standardized contract templates")
        
        return recommendations

def main():
    """Production example execution"""
    print("🏢 ENTERPRISE VERSALAW2 IMPLEMENTATION")
    print("=" * 50)
    
    analyzer = EnterpriseContractAnalyzer()
    
    # Sample enterprise contracts
    enterprise_contracts = {
        "EMP-2024-001": "Perjanjian kerja tetap 3 tahun dengan masa percobaan 3 bulan. Denda 25% untuk pelanggaran disiplin. Berlaku di Indonesia.",
        "SW-LIC-2024-002": "Enterprise software license for 500 users. 2-year term with 10% penalty for late payments. Support included.",
        "PART-2024-003": "Kerjasama bisnis dengan pembagian hasil 60-40%. Jangka waktu 5 tahun. Hukum Indonesia berlaku.",
        "SVC-2024-004": "Monthly consulting services agreement. 30-day termination notice. Confidentiality clause included.",
        "LEASE-2024-005": "Sewa menyewa kantor 2 tahun dengan deposit 3 bulan. Perpanjangan otomatis. DKI Jakarta."
    }
    
    # Analyze contracts
    print("📊 Analyzing enterprise contracts...")
    results_df = analyzer.analyze_contract_batch(enterprise_contracts)
    
    # Display results
    print("\n📈 ANALYSIS RESULTS:")
    print(results_df[['contract_id', 'risk_level', 'risk_score', 'jurisdiction']].to_string(index=False))
    
    # Generate report
    print("\n📋 RISK REPORT:")
    report = analyzer.generate_risk_report(results_df)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    
    # Save to files
    results_df.to_csv('enterprise_contracts_analysis.csv', index=False)
    with open('enterprise_risk_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Files saved:")
    print(f"   - enterprise_contracts_analysis.csv")
    print(f"   - enterprise_risk_report.json")
    
    print(f"\n✅ ENTERPRISE IMPLEMENTATION COMPLETE!")
    print("🚀 VERSALAW2 is production-ready!")

if __name__ == "__main__":
    main()
