#!/usr/bin/env python3
"""
VERSALAW2 Illegal Mining & Drilling Analyzer
Analisis hukum pertambangan ilegal dan pengeboran tanpa izin
"""

class IllegalMiningAnalyzer:
    def __init__(self):
        self.mining_laws = {
            "uu_4_2009": "UU No. 4 Tahun 2009 tentang Pertambangan Mineral dan Batubara",
            "uu_22_2001": "UU No. 22 Tahun 2001 tentang Minyak dan Gas Bumi",
            "uu_32_2009": "UU No. 32 Tahun 2009 tentang Perlindungan dan Pengelolaan Lingkungan Hidup",
            "uu_41_1999": "UU No. 41 Tahun 1999 tentang Kehutanan"
        }
        
        self.mining_violations = [
            "tambang_tanpa_izin",
            "izin_palsu",
            "melampaui_wilayah_izin",
            "penggunaan_bahan_berbahaya",
            "pencemaran_lingkungan",
            "penambangan_di_kawasan_hutan",
            "penambangan_di_kawasan_lindung"
        ]
        
        self.environmental_impacts = [
            "kerusakan_ekosistem",
            "pencemaran_air",
            "pencemaran_tanah", 
            "polusi_udara",
            "banjir_dan_longsor"
        ]
    
    def analyze_illegal_mining(self, case_data):
        """Analisis kasus pertambangan ilegal"""
        analysis = {
            "illegal_mining_detected": False,
            "mining_violations": [],
            "environmental_impacts": [],
            "legal_articles": [],
            "sanctions": [],
            "reclamation_obligation": False,
            "criminal_liability": [],
            "civil_liability": []
        }
        
        # Deteksi pelanggaran pertambangan
        for violation in self.mining_violations:
            if case_data.get(violation):
                analysis["mining_violations"].append(violation)
                analysis["illegal_mining_detected"] = True
        
        # Analisis dampak lingkungan
        for impact in self.environmental_impacts:
            if case_data.get(impact):
                analysis["environmental_impacts"].append(impact)
        
        # Identifikasi pasal hukum
        analysis["legal_articles"] = self._identify_mining_articles(case_data)
        
        # Analisis sanksi
        analysis["sanctions"] = self._calculate_sanctions(case_data)
        
        # Kewajiban reklamasi
        analysis["reclamation_obligation"] = self._reclamation_required(case_data)
        
        # Pertanggungjawaban pidana
        analysis["criminal_liability"] = self._criminal_liability_analysis(case_data)
        
        # Pertanggungjawaban perdata
        analysis["civil_liability"] = self._civil_liability_analysis(case_data)
        
        return analysis
    
    def _identify_mining_articles(self, data):
        """Identifikasi pasal UU yang dilanggar"""
        articles = []
        
        if data.get("tambang_tanpa_izin"):
            articles.append("Pasal 158 UU 4/2009 (Pidana penjara 10 tahun + denda 10M)")
            
        if data.get("izin_palsu"):
            articles.append("Pasal 159 UU 4/2009 (Pidana penjara 6 tahun + denda 6M)")
            
        if data.get("penambangan_di_kawasan_hutan"):
            articles.append("Pasal 78 UU 41/1999 (Pidana penjara 10 tahun + denda 5M)")
            
        if data.get("pencemaran_lingkungan"):
            articles.append("Pasal 98 UU 32/2009 (Pidana penjara 10 tahun + denda 10M)")
            
        if data.get("melampaui_wilayah_izin"):
            articles.append("Pasal 161 UU 4/2009 (Pidana penjama 5 tahun + denda 5M)")
        
        return articles
    
    def _calculate_sanctions(self, data):
        """Hitung sanksi berdasarkan pelanggaran"""
        sanctions = []
        
        if data.get("tambang_tanpa_izin"):
            sanctions.extend([
                "Pidana penjara maksimal 10 tahun",
                "Denda maksimal Rp 10.000.000.000",
                "Pencabutan izin usaha"
            ])
            
        if data.get("pencemaran_lingkungan"):
            sanctions.extend([
                "Pidana penjara maksimal 10 tahun", 
                "Denda maksimal Rp 10.000.000.000",
                "Kewajiban pemulihan lingkungan"
            ])
            
        if data.get("penambangan_di_kawasan_hutan"):
            sanctions.extend([
                "Pidana penjara maksimal 10 tahun",
                "Denda maksimal Rp 5.000.000.000",
                "Rehabilitasi kawasan hutan"
            ])
            
        return sanctions
    
    def _reclamation_required(self, data):
        """Cek apakah wajib reklamasi"""
        return any([
            data.get("kerusakan_lahan", False),
            data.get("lubang_tambang", False),
            data.get("pencemaran_air_tanah", False)
        ])
    
    def _criminal_liability_analysis(self, data):
        """Analisis pertanggungjawaban pidana"""
        liabilities = []
        
        if data.get("perusahaan_terlibat"):
            liabilities.append("Pidana korporasi sesuai Pasal 160 UU 4/2009")
            
        if data.get("pengurus_terlibat"):
            liabilities.append("Pertanggungjawaban pengurus/pengelola")
            
        if data.get("penyalahgunaan_wewenang"):
            liabilities.append("Penyalahgunaan wewenang aparat")
            
        return liabilities
    
    def _civil_liability_analysis(self, data):
        """Analisis pertanggungjawaban perdata"""
        liabilities = []
        
        if data.get("kerugian_negara"):
            liabilities.append("Ganti rugi kepada negara")
            
        if data.get("kerusakan_lingkungan"):
            liabilities.append("Pemulihan fungsi lingkungan hidup")
            
        if data.get("dampak_sosial"):
            liabilities.append("Ganti rugi kepada masyarakat terdampak")
            
        return liabilities
    
    def analyze_mining_licensing(self, license_data):
        """Analisis perizinan pertambangan"""
        return {
            "required_licenses": self._get_required_licenses(license_data),
            "compliance_check": self._license_compliance_check(license_data),
            "violations": self._license_violations(license_data)
        }
    
    def _get_required_licenses(self, data):
        """Dapatkan izin yang diperlukan"""
        licenses = ["IUP (Izin Usaha Pertambangan)"]
        
        if data.get("mineral_type") == "batubara":
            licenses.append("IUPK Khusus Batubara")
            
        if data.get("production_stage"):
            licenses.append("IUP Operasi Produksi")
            
        if data.get("processing_activity"):
            licenses.append("IUP Pengolahan dan Pemurnian")
            
        return licenses
    
    def _license_compliance_check(self, data):
        """Cek kepatuhan perizinan"""
        checks = []
        
        if not data.get("has_iup"):
            checks.append("❌ Tidak memiliki IUP")
        else:
            checks.append("✅ Memiliki IUP")
            
        if data.get("area_exceeded"):
            checks.append("❌ Luas area melebihi izin")
        else:
            checks.append("✅ Luas area sesuai izin")
            
        if data.get("environmental_permits"):
            checks.append("✅ Memiliki izin lingkungan")
        else:
            checks.append("❌ Tidak memiliki izin lingkungan")
            
        return checks
    
    def _license_violations(self, data):
        """Identifikasi pelanggaran perizinan"""
        violations = []
        
        if data.get("mining_without_license"):
            violations.append("Kegiatan tambang tanpa izin")
            
        if data.get("license_expired"):
            violations.append("Izin telah kadaluarsa")
            
        if data.get("wrong_mineral_type"):
            violations.append("Jenis mineral tidak sesuai izin")
            
        if data.get("illegal_export"):
            violations.append("Ekspor mineral tanpa izin")
            
        return violations
