#!/usr/bin/env python3
"""
Land Law Analyzer - Indonesian Agrarian Law  
Analisis hukum pertanahan berdasarkan UUPA dan turunannya
"""

class LandLawAnalyzer:
    def __init__(self):
        self.land_framework = {
            "uupa": "Undang-Undang No. 5/1960 tentang Peraturan Dasar Pokok-Pokok Agraria",
            "hak_atas_tanah": ["Hak Milik", "Hak Guna Usaha", "Hak Guna Bangunan", "Hak Pakai"],
            "sertipikat": "Bukti kepemilikan tanah yang sah"
        }
    
    def analyze_land_dispute(self, dispute_data):
        """Analyze land ownership disputes"""
        analysis_result = {
            "jenis_sengketa": [],
            "bukti_kepemilikan": [],
            "proses_penyelesaian": [],
            "rekomendasi_hukum": []
        }
        
        # Identify dispute type
        if dispute_data.get("double_certificate"):
            analysis_result["jenis_sengketa"].append("Sertipikat ganda")
            analysis_result["proses_penyelesaian"].append("Gugatan ke Pengadilan Negeri")
            
        if dispute_data.get("boundary_dispute"):
            analysis_result["jenis_sengketa"].append("Sengketa batas tanah")
            analysis_result["proses_penyelesaian"].append("Mediasi melalui BPN")
            
        if dispute_data.get("inheritance_dispute"):
            analysis_result["jenis_sengketa"].append("Sengketa warisan")
            analysis_result["proses_penyelesaian"].append("Gugatan waris ke Pengadilan Agama/Negeri")
        
        # Evidence requirements
        analysis_result["bukti_kepemilikan"].extend([
            "Sertipikat tanah",
            "Surat ukur dari BPN", 
            "Bukti pembayaran PBB",
            "Bukti fisik penguasaan"
        ])
        
        return analysis_result

    def analyze_land_acquisition(self, acquisition_data):
        """Analyze land acquisition for development"""
        analysis_result = {
            "prosedur_pengadaan": [],
            "kompensasi": [],
            "kewajiban_pengembang": [],
            "hak_masyarakat": []
        }
        
        # Acquisition procedures
        analysis_result["prosedur_pengadaan"].extend([
            "Musyawarah dengan pemilik tanah",
            "Penilaian harga tanah oleh assessor",
            "Pembayaran ganti rugi",
            "Pelepasan hak secara notariil"
        ])
        
        # Compensation calculation
        analysis_result["kompensasi"].extend([
            "Nilai tanah berdasarkan NJOP",
            "Ganti rugi tanaman dan bangunan",
            "Biaya relokasi jika diperlukan",
            "Kompensasi immateriil"
        ])
        
        return analysis_result

    def analyze(self, case_data):
        """Main analysis method"""
        if case_data.get("analysis_type") == "dispute":
            return self.analyze_land_dispute(case_data)
        elif case_data.get("analysis_type") == "acquisition":
            return self.analyze_land_acquisition(case_data)
        else:
            return self.analyze_land_dispute(case_data)

    def analyze_case(self, case_data):
        """Alias for analyze method"""
        return self.analyze(case_data)
