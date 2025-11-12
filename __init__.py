# versalaw2/__init__.py - Update
from .criminal_intelligence import CriminalIntelligence

class EnhancedLegalClassifier(LegalClassifier):
    def __init__(self):
        super().__init__()
        from .enhanced_knowledge import EnhancedLegalKnowledge
        from .criminal_intelligence import CriminalIntelligence
        
        self.enhanced_knowledge = EnhancedLegalKnowledge()
        self.criminal_intel = CriminalIntelligence()  # ✅ NEW
        print("🚀 Enhanced Legal Classifier with Criminal Intelligence initialized!")
    
    def analyze_criminal_case(self, case_data: Dict) -> Dict:
        """Comprehensive criminal case analysis"""
        legal_analysis = self.comprehensive_analysis(case_data.get('description', ''))
        perpetrator_profiles = self.criminal_intel.predict_perpetrator_profile(case_data)
        modus_operandi = self.criminal_intel.identify_modus_operandi(case_data.get('evidence', []))
        
        return {
            'case_id': case_data.get('case_id', 'unknown'),
            'legal_analysis': legal_analysis,
            'criminal_intelligence': {
                'perpetrator_profiles': perpetrator_profiles,
                'modus_operandi_analysis': modus_operandi,
                'investigation_recommendations': self.generate_investigation_plan(
                    perpetrator_profiles, modus_operandi
                ),
                'risk_assessment': self.assess_public_risk(case_data)
            }
        }
