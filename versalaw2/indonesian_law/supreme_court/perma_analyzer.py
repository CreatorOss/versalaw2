#!/usr/bin/env python3
"""
PERMA Analyzer - Indonesian Law
Analisis Peraturan Mahkamah Agung (PERMA) dan implementasinya
"""

class PERMAAnalyzer:
    def __init__(self):
        self.perma_categories = {
            "procedure": "PERMA tentang Hukum Acara",
            "administration": "PERMA tentang Administrasi Peradilan", 
            "guidance": "PERMA tentang Pedoman",
            "fees": "PERMA tentang Biaya Perkara"
        }
        
        self.important_perma = {
            "perma_1_2019": "PERMA No. 1 Tahun 2019 tentang Administrasi Perkara dan Persidangan Elektronik",
            "perma_2_2019": "PERMA No. 2 Tahun 2019 tentang Tata Cara Penanganan Perkara Simple, Fast & Low Cost",
            "perma_3_2019": "PERMA No. 3 Tahun 2019 tentang Pedoman Mengadili Perkara Perempuan Berhadapan dengan Hukum",
            "perma_1_2020": "PERMA No. 1 Tahun 2020 tentang Keadilan Restoratif"
        }

    def analyze_perma_application(self, case_data):
        """Analyze application of PERMA in specific cases"""
        analysis_result = {
            "applicable_perma": [],
            "procedural_requirements": [],
            "compliance_issues": [],
            "implementation_guidance": []
        }
        
        case_type = case_data.get("case_type", "")
        
        # Determine applicable PERMA based on case type
        if case_type == "electronic_court":
            analysis_result["applicable_perma"].append("PERMA No. 1 Tahun 2019 tentang Administrasi Perkara Elektronik")
            analysis_result["procedural_requirements"].append("Pendaftaran perkara melalui sistem elektronik")
            
        if case_type == "simple_fast_low_cost":
            analysis_result["applicable_perma"].append("PERMA No. 2 Tahun 2019 tentang SPLC")
            analysis_result["procedural_requirements"].append("Pemeriksaan dengan prosedur sederhana")
            
        if case_data.get("involves_women"):
            analysis_result["applicable_perma"].append("PERMA No. 3 Tahun 2019 tentang Perempuan Berhadapan dengan Hukum")
            analysis_result["implementation_guidance"].append("Pertimbangan khusus kondisi perempuan")
            
        if case_data.get("restorative_justice_applicable"):
            analysis_result["applicable_perma"].append("PERMA No. 1 Tahun 2020 tentang Keadilan Restoratif")
            analysis_result["implementation_guidance"].append("Penyelesaian melalui pendekatan restoratif")
            
        return analysis_result

    def validate_perma_compliance(self, procedural_data):
        """Validate procedural compliance with PERMA"""
        validation_result = {
            "is_compliant": True,
            "compliance_issues": [],
            "required_corrections": [],
            "compliance_score": 100
        }
        
        # Check electronic filing compliance
        if procedural_data.get("requires_electronic_filing") and not procedural_data.get("electronic_filing_done"):
            validation_result["is_compliant"] = False
            validation_result["compliance_issues"].append("Tidak memenuhi persyaratan administrasi elektronik")
            validation_result["required_corrections"].append("Lakukan pendaftaran melalui sistem elektronik")
            validation_result["compliance_score"] -= 30
            
        # Check SPLC compliance
        if procedural_data.get("eligible_splc") and not procedural_data.get("splc_procedure_followed"):
            validation_result["compliance_issues"].append("Tidak mengikuti prosedur Simple, Fast & Low Cost")
            validation_result["required_corrections"].append("Terapkan prosedur SPLC sesuai PERMA No. 2/2019")
            validation_result["compliance_score"] -= 20
            
        return validation_result

    def analyze(self, case_data):
        """Main analysis method"""
        return self.analyze_perma_application(case_data)
        
    def analyze_case(self, case_data):
        """Alias for analyze method"""
        return self.analyze(case_data)
