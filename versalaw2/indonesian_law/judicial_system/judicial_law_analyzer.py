#!/usr/bin/env python3
"""
Judicial Law Analyzer - Indonesian Law
Analisis UU Kehakiman dan kerangka hukum peradilan Indonesia
"""

class JudicialLawAnalyzer:
    def __init__(self):
        self.judicial_framework = {
            "uu_kehakiman": "Undang-Undang No. 48/2009 tentang Kekuasaan Kehakiman",
            "uu_mahkamah_agung": "Undang-Undang No. 5/2004 tentang Mahkamah Agung",
            "uu_peradilan_umum": "Undang-Undang No. 8/2004 tentang Peradilan Umum",
            "uu_peradilan_tun": "Undang-Undang No. 5/1986 tentang Peradilan Tata Usaha Negara",
            "uu_peradilan_agama": "Undang-Undang No. 7/1989 tentang Peradilan Agama",
            "uu_peradilan_militer": "Undang-Undang No. 31/1997 tentang Peradilan Militer"
        }
        
        self.judicial_principles = {
            "independence": "Kemandirian Kekuasaan Kehakiman",
            "impartiality": "Sifat Tidak Memihak",
            "competence": "Kompetensi dan Profesionalitas",
            "integrity": "Integritas dan Akuntabilitas",
            "transparency": "Transparansi dan Akuntabilitas Publik"
        }

    def analyze_judicial_independence(self, case_data):
        """Analyze judicial independence and impartiality issues"""
        analysis_result = {
            "independence_issues": [],
            "impartiality_concerns": [],
            "external_influences": [],
            "institutional_safeguards": [],
            "remedial_actions": []
        }
        
        # Check for independence violations
        if case_data.get("executive_interference"):
            analysis_result["independence_issues"].append("Campur tangan eksekutif dalam peradilan")
            analysis_result["external_influences"].append("Pelanggaran prinsip pemisahan kekuasaan")
            
        if case_data.get("legislative_pressure"):
            analysis_result["independence_issues"].append("Tekanan dari lembaga legislatif")
            analysis_result["remedial_actions"].append("Pelaporan ke Komisi Yudisial")
            
        # Check for impartiality concerns
        if case_data.get("judge_bias"):
            analysis_result["impartiality_concerns"].append("Kecurigaan keberpihakan hakim")
            analysis_result["remedial_actions"].append("Pengajuan keberatan dan penggantian hakim")
            
        if case_data.get("conflict_of_interest"):
            analysis_result["impartiality_concerns"].append("Konflik kepentingan dalam persidangan")
            analysis_result["remedial_actions"].append("Pengunduran diri hakim yang bersangkutan")
            
        # Institutional safeguards
        analysis_result["institutional_safeguards"].extend([
            "Komisi Yudisial sebagai pengawas eksternal",
            "Majelis Kehormatan Hakim untuk etik internal",
            "Kode Etik dan Pedoman Perilaku Hakim (KEPPH)"
        ])
        
        return analysis_result

    def analyze_court_jurisdiction(self, jurisdiction_data):
        """Analyze court jurisdiction and competence"""
        analysis_result = {
            "proper_jurisdiction": "unknown",
            "jurisdictional_issues": [],
            "competence_analysis": [],
            "forum_selection_guidance": []
        }
        
        case_type = jurisdiction_data.get("case_type", "")
        disputed_amount = jurisdiction_data.get("disputed_amount", 0)
        
        # Determine proper jurisdiction based on case type
        if case_type == "civil_dispute":
            if disputed_amount <= 500000000:  # <= 500 juta
                analysis_result["proper_jurisdiction"] = "Pengadilan Negeri"
                analysis_result["forum_selection_guidance"].append("Gugatan diajukan ke Pengadilan Negeri")
            else:
                analysis_result["proper_jurisdiction"] = "Pengadilan Negeri (dapat banding ke PT)"
                
        elif case_type == "administrative_dispute":
            analysis_result["proper_jurisdiction"] = "Pengadilan Tata Usaha Negara"
            analysis_result["forum_selection_guidance"].append("Gugatan TUN diajukan ke PTUN")
            
        elif case_type == "religious_dispute":
            analysis_result["proper_jurisdiction"] = "Pengadilan Agama"
            analysis_result["forum_selection_guidance"].append("Sengketa perdata agama ke Pengadilan Agama")
            
        elif case_type == "military_offense":
            analysis_result["proper_jurisdiction"] = "Pengadilan Militer"
            analysis_result["forum_selection_guidance"].append("Tindak pidana militer diadili Pengadilan Militer")
            
        # Check for jurisdictional issues
        if jurisdiction_data.get("wrong_forum_filed"):
            analysis_result["jurisdictional_issues"].append("Gugatan diajukan di forum yang tidak tepat")
            analysis_result["competence_analysis"].append("Pengadilan tidak berwenang mengadili perkara")
            
        return analysis_result

    def analyze_judicial_reform(self, reform_data):
        """Analyze judicial reform and modernization efforts"""
        analysis_result = {
            "reform_initiatives": [],
            "transparency_measures": [],
            "accountability_mechanisms": [],
            "technology_adoption": [],
            "capacity_building": []
        }
        
        # Judicial reform initiatives
        analysis_result["reform_initiatives"].extend([
            "E-Court system implementation",
            "Case management modernization",
            "Judicial training and education"
        ])
        
        # Transparency measures
        analysis_result["transparency_measures"].extend([
            "Putusan online dan terbuka untuk publik",
            "Proses rekrutmen hakim yang transparan",
            "Pengumuman jadwal persidangan secara terbuka"
        ])
        
        # Technology adoption
        if reform_data.get("digital_transformation"):
            analysis_result["technology_adoption"].extend([
                "Sistem persidangan elektronik",
                "Aplikasi mobile untuk informasi pengadilan",
                "Digital case filing dan document management"
            ])
            
        return analysis_result

    def analyze(self, case_data):
        """Main analysis method"""
        if case_data.get("analysis_type") == "jurisdiction":
            return self.analyze_court_jurisdiction(case_data)
        elif case_data.get("analysis_type") == "judicial_reform":
            return self.analyze_judicial_reform(case_data)
        else:
            return self.analyze_judicial_independence(case_data)

    def analyze_case(self, case_data):
        """Alias for analyze method"""
        return self.analyze(case_data)
