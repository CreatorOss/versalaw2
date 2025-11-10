#!/usr/bin/env python3
"""
Child Protection Analyzer - Indonesian Law
Analisis komprehensif perlindungan anak berdasarkan UU No. 35/2014 dan SPPA
"""

class ChildProtectionAnalyzer:
    def __init__(self):
        self.child_protection_framework = {
            "uu_pa": "Undang-Undang No. 35/2014 tentang Perlindungan Anak",
            "uu_sppa": "Undang-Undang No. 11/2012 tentang Sistem Peradilan Pidana Anak",
            "konvensi_hak_anak": "Konvention on the Rights of the Child (CRC)",
            "optional_protocols": "Protokol Opsional tentang Penjualan Anak, Prostitusi Anak, dan Pornografi Anak"
        }
        
        self.child_rights_principles = {
            "non_discrimination": "Prinsip Non-Diskriminasi",
            "best_interest": "Prinsip Kepentingan Terbaik bagi Anak",
            "life_survival_development": "Prinsip Hak untuk Hidup, Kelangsungan Hidup, dan Perkembangan",
            "participation": "Prinsip Penghargaan terhadap Pandangan Anak"
        }

    def analyze_child_rights_violation(self, case_data):
        """Analyze child rights violations with child-sensitive approach"""
        analysis_result = {
            "violated_child_rights": [],
            "protection_urgency": "low",
            "child_sensitive_procedures": [],
            "rehabilitation_services": [],
            "legal_guardianship": []
        }
        
        child_age = case_data.get("child_age", 0)
        violation_type = case_data.get("violation_type", "")
        
        # Analyze based on violation type
        if violation_type == "child_abuse":
            analysis_result["violated_child_rights"].append("Hak Perlindungan dari Kekerasan dan Eksploitasi")
            analysis_result["protection_urgency"] = "high"
            analysis_result["child_sensitive_procedures"].append("Pemeriksaan oleh psikolog anak")
            analysis_result["rehabilitation_services"].append("Trauma counseling dan pendampingan")
            
        if violation_type == "child_labor":
            analysis_result["violated_child_rights"].append("Hak atas Perlindungan dari Eksploitasi Ekonomi")
            analysis_result["protection_urgency"] = "medium"
            analysis_result["rehabilitation_services"].append("Program reintegrasi dan pendidikan")
            
        if violation_type == "child_marriage":
            analysis_result["violated_child_rights"].extend([
                "Hak atas Perlindungan dari Perkawinan Anak",
                "Hak atas Pendidikan",
                "Hak atas Kesehatan Reproduksi"
            ])
            analysis_result["protection_urgency"] = "high"
            analysis_result["legal_guardianship"].append("Penunjupan pendamping hukum khusus anak")
            
        if violation_type == "sexual_exploitation":
            analysis_result["violated_child_rights"].append("Hak atas Perlindungan dari Eksploitasi Seksual")
            analysis_result["protection_urgency"] = "very_high"
            analysis_result["child_sensitive_procedures"].extend([
                "Pemeriksaan di ruang anak yang ramah",
                "Pendampingan psikolog selama proses hukum",
                "Avoid multiple interviews dengan anak"
            ])
            
        # Age-specific considerations
        if child_age < 6:
            analysis_result["child_sensitive_procedures"].append("Pendekatan melalui terapi bermain")
        elif child_age < 12:
            analysis_result["child_sensitive_procedures"].append("Komunikasi dengan bahasa yang sesuai usia")
        elif child_age < 18:
            analysis_result["child_sensitive_procedures"].append("Konsiderasi partisipasi anak dalam proses")
            
        return analysis_result

    def analyze_juvenile_justice(self, case_data):
        """Analyze juvenile justice cases with restorative approach"""
        analysis_result = {
            "diversion_eligibility": False,
            "restorative_justice_options": [],
            "child_specific_sentencing": [],
            "rehabilitation_focus": [],
            "family_involvement": []
        }
        
        child_age = case_data.get("child_age", 0)
        offense_type = case_data.get("offense_type", "")
        prior_record = case_data.get("prior_record", False)
        
        # Diversion eligibility (UU SPPA)
        if child_age >= 14 and child_age < 18 and not prior_record:
            if offense_type in ["minor_theft", "vandalism", "simple_assault"]:
                analysis_result["diversion_eligibility"] = True
                analysis_result["restorative_justice_options"].extend([
                    "Restauration kepada korban",
                    "Community service",
                    "Counseling dan pembinaan"
                ])
        
        # Child-specific sentencing considerations
        analysis_result["child_specific_sentencing"].extend([
            "Prioritaskan pembinaan daripada penjara",
            "Pertimbangkan latar belakang keluarga dan sosial",
            "Libatkan psikolog anak dalam assessment"
        ])
        
        # Rehabilitation focus
        analysis_result["rehabilitation_focus"].extend([
            "Pendidikan dan pelatihan keterampilan",
            "Konseling perilaku",
            "Reintegrasi sosial"
        ])
        
        # Family involvement
        analysis_result["family_involvement"].extend([
            "Keluarga sebagai mitra dalam pembinaan",
            "Parenting education jika diperlukan",
            "Dukungan psikososial untuk keluarga"
        ])
        
        return analysis_result

    def analyze_child_in_emergency(self, emergency_data):
        """Analyze protection of children in emergency situations"""
        analysis_result = {
            "immediate_protection_needs": [],
            "family_tracing_reunification": [],
            "alternative_care": [],
            "psychosocial_support": [],
            "education_continuity": []
        }
        
        emergency_type = emergency_data.get("emergency_type", "")
        
        if emergency_type == "natural_disaster":
            analysis_result["immediate_protection_needs"].extend([
                "Identifikasi dan registrasi anak terpisah",
                "Tempat penampungan yang aman untuk anak",
                "Protection from exploitation in camps"
            ])
            analysis_result["family_tracing_reunification"].append("Sistem tracing dan reunifikasi keluarga")
            
        if emergency_type == "armed_conflict":
            analysis_result["immediate_protection_needs"].extend([
                "Protection from recruitment by armed groups",
                "Safe spaces for children",
                "Mental health and psychosocial support"
            ])
            analysis_result["education_continuity"].append("Temporary learning spaces")
            
        if emergency_type == "pandemic":
            analysis_result["immediate_protection_needs"].extend([
                "Protection from increased domestic violence",
                "Continuity of child protection services",
                "Alternative care arrangements if parents hospitalized"
            ])
            
        return analysis_result

    def analyze(self, case_data):
        """Main analysis method"""
        if case_data.get("case_category") == "juvenile_justice":
            return self.analyze_juvenile_justice(case_data)
        elif case_data.get("case_category") == "emergency":
            return self.analyze_child_in_emergency(case_data)
        else:
            return self.analyze_child_rights_violation(case_data)

    def analyze_case(self, case_data):
        """Alias for analyze method"""
        return self.analyze(case_data)
