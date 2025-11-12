# examples/criminal_intelligence_demo.py
from versalaw2 import EnhancedLegalClassifier

def demo_criminal_intelligence():
    print("🔍 VERSALAW2 CRIMINAL INTELLIGENCE DEMO")
    print("=" * 50)
    
    clf = EnhancedLegalClassifier()
    
    # Test case 1: Korupsi
    print("\n1. 🕵️ KORUPSI CASE ANALYSIS")
    corruption_case = {
        'case_id': 'KOR-001',
        'crime_type': 'korupsi',
        'description': 'markup proyek pengadaan barang fiktif',
        'evidence': ['faktur fiktif', 'markup harga', 'laporan keuangan tidak transparan'],
        'modus_operandi': 'penggelapan anggaran'
    }
    
    result = clf.analyze_criminal_case(corruption_case)
    print(f"   Primary Profile: {result['criminal_intelligence']['perpetrator_profiles']['primary_suspect_profile']['profile_type']}")
    print(f"   Confidence: {result['criminal_intelligence']['perpetrator_profiles']['primary_suspect_profile']['confidence']:.2f}")
    
    # Test case 2: Ghost Contract Fraud
    print("\n2. 👻 GHOST CONTRACT FRAUD ANALYSIS")
    ghost_fraud_case = {
        'case_id': 'GCF-001', 
        'crime_type': 'cyber_fraud',
        'description': 'BCI neural interface contract manipulation',
        'evidence': ['vague consent clauses', 'neural data misuse', 'asymmetric contract terms'],
        'modus_operandi': 'bci_consent_manipulation'
    }
    
    result2 = clf.analyze_criminal_case(ghost_fraud_case)
    print(f"   MO Identified: {result2['criminal_intelligence']['modus_operandi_analysis'][0]['modus_operandi']}")
    print(f"   Investigation Priority: {result2['criminal_intelligence']['modus_operandi_analysis'][0]['investigation_priority']}")

if __name__ == "__main__":
    demo_criminal_intelligence()
