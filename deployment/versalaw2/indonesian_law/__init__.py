"""
Indonesian Legal System Integration Module
Integrator utama untuk sistem hukum Indonesia
"""

from .hierarchy.constitutional_law import ConstitutionalLawAnalyzer
from .hierarchy.statutory_law import StatutoryLawAnalyzer

class IndonesianLawAnalyzer:
    """Main integrator for comprehensive Indonesian legal system analysis"""
    
    def __init__(self):
        self.constitutional = ConstitutionalLawAnalyzer()
        self.statutory = StatutoryLawAnalyzer()
    
    def comprehensive_analysis(self, legal_text, context=None):
        """
        Perform complete Indonesian legal analysis
        
        Args:
            legal_text (str): Legal document or provision text
            context (dict): Additional context (document_type, etc.)
        
        Returns:
            dict: Comprehensive legal analysis results
        """
        analysis = {
            "hierarchy_analysis": {},
            "constitutional_analysis": {},
            "statutory_analysis": {},
            "compliance_summary": {},
            "recommendations": []
        }
        
        # Constitutional law analysis
        analysis["constitutional_analysis"] = self.constitutional.analyze_compliance(legal_text)
        
        # Statutory law analysis  
        analysis["statutory_analysis"] = self.statutory.analyze_compliance(legal_text)
        
        # Generate compliance summary
        analysis["compliance_summary"] = self._generate_compliance_summary(analysis)
        
        # Generate recommendations
        analysis["recommendations"] = self._generate_recommendations(analysis)
        
        return analysis
    
    def _generate_compliance_summary(self, analysis):
        """Generate overall compliance summary"""
        summary = {
            "constitutional_compliance": "pending",
            "statutory_compliance": "pending",
            "overall_risk": "unknown"
        }
        
        # Evaluate constitutional compliance
        const_issues = len(analysis["constitutional_analysis"].get("constitutional_issues", []))
        rights_issues = len(analysis["constitutional_analysis"].get("rights_violations", []))
        
        if const_issues == 0 and rights_issues == 0:
            summary["constitutional_compliance"] = "compliant"
        elif rights_issues > 0:
            summary["constitutional_compliance"] = "high_risk"
        else:
            summary["constitutional_compliance"] = "needs_review"
        
        # Evaluate statutory compliance
        hierarchy_issues = len(analysis["statutory_analysis"].get("hierarchy_issues", []))
        conflicts = len(analysis["statutory_analysis"].get("conflict_analysis", []))
        
        if hierarchy_issues == 0 and conflicts == 0:
            summary["statutory_compliance"] = "compliant"
        elif hierarchy_issues > 0:
            summary["statutory_compliance"] = "high_risk"
        else:
            summary["statutory_compliance"] = "needs_review"
        
        # Overall risk assessment
        if "high_risk" in [summary["constitutional_compliance"], summary["statutory_compliance"]]:
            summary["overall_risk"] = "high"
        elif "needs_review" in [summary["constitutional_compliance"], summary["statutory_compliance"]]:
            summary["overall_risk"] = "medium"
        else:
            summary["overall_risk"] = "low"
        
        return summary
    
    def _generate_recommendations(self, analysis):
        """Generate legal recommendations based on analysis"""
        recommendations = []
        
        # Constitutional recommendations
        if analysis["constitutional_analysis"].get("rights_violations"):
            recommendations.append({
                "type": "constitutional",
                "priority": "high",
                "message": "Tinjau potensi pelanggaran hak asasi manusia",
                "suggestion": "Konsultasi dengan ahli hukum konstitusi"
            })
        
        # Statutory recommendations
        if analysis["statutory_analysis"].get("hierarchy_issues"):
            recommendations.append({
                "type": "statutory",
                "priority": "high", 
                "message": "Periksa hierarki peraturan perundang-undangan",
                "suggestion": "Pastikan tidak ada pelanggaran tata urutan peraturan"
            })
        
        # General recommendations
        if not recommendations:
            recommendations.append({
                "type": "general",
                "priority": "low",
                "message": "Dokumen tampak sesuai dengan kerangka hukum Indonesia",
                "suggestion": "Lakukan peninjauan hukum secara berkala"
            })
        
        return recommendations

__all__ = ['IndonesianLawAnalyzer']
