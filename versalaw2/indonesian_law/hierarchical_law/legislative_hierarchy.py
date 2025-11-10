#!/usr/bin/env python3
"""
Legislative Hierarchy Analyzer - Indonesian Law
Analisis hierarki peraturan perundang-undangan berdasarkan UU No. 12/2011
"""

class LegislativeHierarchyAnalyzer:
    def __init__(self):
        self.hierarchy = {
            "uud_1945": "Undang-Undang Dasar 1945",
            "tap_mpr": "Ketetapan Majelis Permusyawaratan Rakyat",
            "uu_perpu": "Undang-Undang/Peraturan Pemerintah Pengganti Undang-Undang",
            "peraturan_pemerintah": "Peraturan Pemerintah",
            "peraturan_presiden": "Peraturan Presiden",
            "peraturan_daerah": "Peraturan Daerah (Provinsi/Kabupaten/Kota)",
            "keputusan_presiden": "Keputusan Presiden",
            "instruksi_presiden": "Instruksi Presiden"
        }
        
        self.conflict_rules = {
            "asas_lex_superior": "Peraturan yang lebih tinggi mengesampingkan peraturan yang lebih rendah",
            "asas_lex_posterior": "Peraturan yang baru mengesampingkan peraturan yang lama", 
            "asas_lex_specialis": "Peraturan yang khusus mengesampingkan peraturan yang umum"
        }

    def analyze_hierarchy_conflict(self, regulation_data):
        """Analyze hierarchy conflicts between regulations"""
        analysis_result = {
            "hierarchy_levels": [],
            "potential_conflicts": [],
            "applicable_principles": [],
            "resolution_recommendations": []
        }
        
        # Check hierarchy levels
        for reg_type in regulation_data.get("regulation_types", []):
            if reg_type in self.hierarchy:
                analysis_result["hierarchy_levels"].append({
                    "type": reg_type,
                    "description": self.hierarchy[reg_type]
                })
        
        # Check for conflicts
        if regulation_data.get("different_levels_conflict"):
            analysis_result["potential_conflicts"].append("Konflik hierarki peraturan")
            analysis_result["applicable_principles"].append("Asas lex superior derogat legi inferiori")
            
        if regulation_data.get("same_level_timing_conflict"):
            analysis_result["potential_conflicts"].append("Konflik peraturan setingkat berbeda waktu")
            analysis_result["applicable_principles"].append("Asas lex posterior derogat legi priori")
            
        if regulation_data.get("general_specific_conflict"):
            analysis_result["potential_conflicts"].append("Konflik peraturan umum dan khusus")
            analysis_result["applicable_principles"].append("Asas lex specialis derogat legi generali")
            
        return analysis_result

    def validate_regulation_hierarchy(self, regulation_data):
        """Validate if regulation follows proper hierarchy"""
        validation_result = {
            "is_valid": True,
            "violations": [],
            "hierarchy_issues": [],
            "compliance_score": 100
        }
        
        higher_regs = regulation_data.get("higher_regulations", [])
        current_reg = regulation_data.get("current_regulation", "")
        
        # Check if current regulation contradicts higher regulations
        if regulation_data.get("contradicts_higher_regulation"):
            validation_result["is_valid"] = False
            validation_result["violations"].append("Melanggar asas lex superior")
            validation_result["compliance_score"] -= 40
            
        # Check procedural compliance
        if not regulation_data.get("proper_procedure_followed"):
            validation_result["violations"].append("Tidak mengikuti prosedur pembentukan yang benar")
            validation_result["compliance_score"] -= 30
            
        return validation_result

    def analyze(self, case_data):
        """Main analysis method"""
        return self.analyze_hierarchy_conflict(case_data)
        
    def analyze_case(self, case_data):
        """Alias for analyze method"""
        return self.analyze(case_data)
