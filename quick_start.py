from versalaw2 import EnhancedLegalClassifier, GhostContractAnalyzer, LegalExpertSystem

# Initialize all components
clf = EnhancedLegalClassifier()
ghost_analyzer = GhostContractAnalyzer()
expert_system = LegalExpertSystem()

# Example 1: Comprehensive legal analysis
print("=== COMPREHENSIVE LEGAL ANALYSIS ===")
result = clf.comprehensive_analysis("BCI neural interface contract validity")
print(f"Domain: {result['classification']['legal_domain']}")
print(f"Analysis Level: {result['classification']['analysis_level']}")
print(f"Confidence: {result['classification']['confidence_score']}")

# Example 2: Ghost contract analysis
print("\n=== GHOST CONTRACT ANALYSIS ===")
contract_result = clf.analyze_complex_contract("digital neural link agreement")
print(f"Contract Type: {contract_result['contract_category']}")
print(f"Risk Level: {contract_result['risk_level']}")
print(f"Tech Elements: {contract_result['future_tech_elements']}")

# Example 3: Expert system consultation
print("\n=== EXPERT SYSTEM CONSULTATION ===")
expert_advice = expert_system.get_expert_analysis("bci_contract")
print(f"Case Type: {expert_advice['case_type']}")
print(f"Precedents: {expert_advice['relevant_precedents']}")
