#!/usr/bin/env python3
"""
Labor Law Analyzer - Indonesian Labor Law
Analisis hukum ketenagakerjaan berdasarkan UU Ketenagakerjaan
"""

class LaborLawAnalyzer:
    def __init__(self):
        self.labor_framework = {
            "uu_ketenagakerjaan": "Undang-Undang No. 13/2003 tentang Ketenagakerjaan",
            "uu_cipta_kerja": "Undang-Undang No. 11/2020 tentang Cipta Kerja",
            "hak_pekerja": ["Upah layak", "Waktu kerja", "Cuti", "Jaminan sosial"]
        }
    
    def analyze_employment_contract(self, contract_data):
        """Analyze employment contract validity"""
        analysis_result = {
            "syarat_sah_pkwt": [],
            "hak_pekerja": [],
            "kewajiban_pengusaha": [],
            "potensi_pelanggaran": []
        }
        
        # Check PKWT requirements
        if contract_data.get("written_contract"):
            analysis_result["syarat_sah_pkwt"].append("Perjanjian tertulis: TERPENUHI")
        else:
            analysis_result["syarat_sah_pkwt"].append("Perjanjian tertulis: TIDAK TERPENUHI")
            analysis_result["potensi_pelanggaran"].append("PKWT harus dibuat tertulis")
            
        if contract_data.get("specific_work"):
            analysis_result["syarat_sah_pkwt"].append("Pekerjaan tertentu dan sementara: TERPENUHI")
        else:
            analysis_result["syarat_sah_pkwt"].append("Pekerjaan tertentu dan sementara: TIDAK TERPENUHI")
            
        # Worker rights
        analysis_result["hak_pekerja"].extend([
            "Upah minimum provinsi",
            "Jaminan sosial (BPJS)",
            "Waktu kerja maksimal 40 jam/minggu",
            "Cuti tahunan 12 hari"
        ])
        
        # Employer obligations
        analysis_result["kewajiban_pengusaha"].extend([
            "Membayar upah tepat waktu",
            "Menyediakan lingkungan kerja aman",
            "Memberikan jaminan sosial",
            "Menghormati hak berserikat"
        ])
        
        return analysis_result

    def analyze_termination_dispute(self, termination_data):
        """Analyze employment termination disputes"""
        analysis_result = {
            "jenis_phk": [],
            "prosedur_phk": [],
            "pesangon": [],
            "upaya_hukum": []
        }
        
        # Termination types
        if termination_data.get("disciplinary_termination"):
            analysis_result["jenis_phk"].append("PHK karena pelanggaran")
            analysis_result["prosedur_phk"].append("Peringatan tertulis 3x + BAP pelanggaran")
            
        if termination_data.get("company_restructuring"):
            analysis_result["jenis_phk"].append("PHK karena efisiensi")
            analysis_result["prosedur_phk"].append("Musyawarah bipartit + pemberitahuan")
            
        # Severance calculation
        analysis_result["pesangon"].extend([
            "Masa kerja <1 tahun: 1 bulan upah",
            "Masa kerja 1-2 tahun: 2 bulan upah", 
            "Masa kerja 2-3 tahun: 3 bulan upah",
            "Masa kerja >3 tahun: 4+ bulan upah"
        ])
        
        # Legal remedies
        analysis_result["upaya_hukum"].extend([
            "Gugatan ke Pengadilan Hubungan Industrial",
            "Mediasi melalui Dinas Tenaga Kerja",
            "Bantuan hukum serikat pekerja"
        ])
        
        return analysis_result

    def analyze(self, case_data):
        """Main analysis method"""
        if case_data.get("analysis_type") == "termination":
            return self.analyze_termination_dispute(case_data)
        else:
            return self.analyze_employment_contract(case_data)

    def analyze_case(self, case_data):
        """Alias for analyze method"""
        return self.analyze(case_data)
