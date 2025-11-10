#!/usr/bin/env python3
"""
Company Law Analyzer - Indonesian Commercial Law
Analisis hukum perusahaan berdasarkan UU Perseroan Terbatas
"""

class CompanyLawAnalyzer:
    def __init__(self):
        self.company_framework = {
            "uu_pt": "Undang-Undang No. 40/2007 tentang Perseroan Terbatas",
            "jenis_perseroan": ["PT Tertutup", "PT Terbuka", "PT PMA"],
            "organ_perusahaan": ["RUPS", "Direksi", "Dewan Komisaris"]
        }
    
    def analyze_company_formation(self, formation_data):
        """Analyze company formation requirements"""
        analysis_result = {
            "syar_pendirian": [],
            "dokumen_wajib": [],
            "modal_dasar": "tidak_terpenuhi",
            "rekomendasi": []
        }
        
        # Check formation requirements
        if formation_data.get("min_two_shareholders"):
            analysis_result["syar_pendirian"].append("Minimal 2 pemegang saham: TERPENUHI")
        else:
            analysis_result["syar_pendirian"].append("Minimal 2 pemegang saham: TIDAK TERPENUHI")
            
        if formation_data.get("min_capital_met"):
            analysis_result["syar_pendirian"].append("Modal dasar minimum: TERPENUHI")
            analysis_result["modal_dasar"] = "terpenuhi"
        else:
            analysis_result["syar_pendirian"].append("Modal dasar minimum: TIDAK TERPENUHI")
            
        if formation_data.get("akta_notaris"):
            analysis_result["syar_pendirian"].append("Akta Notaris: TERPENUHI")
        else:
            analysis_result["syar_pendirian"].append("Akta Notaris: TIDAK TERPENUHI")
            
        # Required documents
        analysis_result["dokumen_wajib"].extend([
            "Akta Pendirian dari Notaris",
            "Pengesahan Menkumham",
            "NIB (Nomor Induk Berusaha)",
            "SK Domisili Perusahaan"
        ])
        
        return analysis_result

    def analyze_director_liability(self, liability_data):
        """Analyze director liability and responsibilities"""
        analysis_result = {
            "tanggung_jawab_direksi": [],
            "syarat_pengangkatan": [],
            "sanksi_pelanggaran": [],
            "protection_measures": []
        }
        
        # Director responsibilities
        analysis_result["tanggung_jawab_direksi"].extend([
            "Bertindak untuk kepentingan perusahaan",
            "Menjaga rahasia perusahaan",
            "Melaporkan konflik kepentingan",
            "Bertanggung jawab atas kerugian perusahaan"
        ])
        
        # Appointment requirements
        analysis_result["syarat_pengangkatan"].extend([
            "Dapat bertindak hukum",
            "Tidak pernah dinyatakan pailit",
            "Tidak pernah menjabat direksi yang menyebabkan pailit"
        ])
        
        # Violation sanctions
        if liability_data.get("breach_of_duty"):
            analysis_result["sanksi_pelanggaran"].extend([
                "Ganti rugi kepada perusahaan",
                "Pidana penjara untuk tindak pidana korporasi",
                "Pencabutan izin usaha"
            ])
            
        return analysis_result

    def analyze(self, case_data):
        """Main analysis method"""
        if case_data.get("analysis_type") == "formation":
            return self.analyze_company_formation(case_data)
        elif case_data.get("analysis_type") == "director_liability":
            return self.analyze_director_liability(case_data)
        else:
            return self.analyze_company_formation(case_data)

    def analyze_case(self, case_data):
        """Alias for analyze method"""
        return self.analyze(case_data)
