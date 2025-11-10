#!/usr/bin/env python3
"""
VERSALAW2 Illegal Logging Analyzer
Analisis hukum penebangan liar dan perdagangan kayu ilegal
"""

class IllegalLoggingAnalyzer:
    def __init__(self):
        self.forestry_laws = {
            "uu_41_1999": "UU No. 41 Tahun 1999 tentang Kehutanan",
            "uu_18_2013": "UU No. 18 Tahun 2013 tentang Pencegahan dan Pemberantasan Perusakan Hutan",
            "uu_32_2009": "UU No. 32 Tahun 2009 tentang Perlindungan dan Pengelolaan Lingkungan Hidup"
        }
        
        self.logging_violations = [
            "penebangan_tanpa_izin",
            "penebangan_di_kawasan_lindung",
            "penebangan_lebihan_kuota",
            "penggunaan_izin_palsu",
            "perdagangan_kayu_ilegal",
            "transportasi_kayu_ilegal"
        ]
        
        self.protected_areas = [
            "hutan_lindung",
            "hutan_konservasi",
            "taman_nasional",
            "cagar_alam",
            "suaka_margasatwa"
        ]
    
    def analyze_illegal_logging(self, case_data):
        """Analisis kasus penebangan liar"""
        analysis = {
            "illegal_logging_detected": False,
            "logging_violations": [],
            "protected_area_violation": False,
            "environmental_damage": [],
            "legal_articles": [],
            "sanctions": [],
            "timber_tracking": [],
            "reforestation_required": False
        }
        
        # Deteksi pelanggaran kehutanan
        for violation in self.logging_violations:
            if case_data.get(violation):
                analysis["logging_violations"].append(violation)
                analysis["illegal_logging_detected"] = True
        
        # Pelanggaran kawasan lindung
        for area in self.protected_areas:
            if case_data.get(area):
                analysis["protected_area_violation"] = True
                analysis["environmental_damage"].append(f"Kerusakan {area}")
        
        # Identifikasi pasal hukum
        analysis["legal_articles"] = self._identify_forestry_articles(case_data)
        
        # Analisis sanksi
        analysis["sanctions"] = self._calculate_logging_sanctions(case_data)
        
        # Pelacakan kayu
        analysis["timber_tracking"] = self._timber_tracking_analysis(case_data)
        
        # Kewajiban reboisasi
        analysis["reforestation_required"] = self._reforestation_needed(case_data)
        
        return analysis
    
    def _identify_forestry_articles(self, data):
        """Identifikasi pasal UU Kehutanan yang dilanggar"""
        articles = []
        
        if data.get("penebangan_tanpa_izin"):
            articles.append("Pasal 78 UU 41/1999 (Pidana penjara 10 tahun + denda 5M)")
            
        if data.get("penebangan_di_kawasan_lindung"):
            articles.append("Pasal 50 UU 41/1999 (Pidana penjara 10 tahun + denda 5M)")
            
        if data.get("perdagangan_kayu_ilegal"):
            articles.append("Pasal 82 UU 18/2013 (Pidana penjara 10 tahun + denda 10M)")
            
        if data.get("penggunaan_izin_palsu"):
            articles.append("Pasal 83 UU 18/2013 (Pidana penjara 5 tahun + denda 5M)")
            
        return articles
    
    def _calculate_logging_sanctions(self, data):
        """Hitung sanksi penebangan liar"""
        sanctions = []
        
        volume = data.get("timber_volume", 0)
        area_damaged = data.get("area_damaged", 0)
        
        if volume > 0:
            sanctions.append(f"Ganti rugi kayu: {volume:,} m³")
            
        if area_damaged > 0:
            sanctions.append(f"Rehabilitasi lahan: {area_damaged:,} ha")
            
        if data.get("penebangan_tanpa_izin"):
            sanctions.extend([
                "Pidana penjara maksimal 10 tahun",
                "Denda maksimal Rp 5.000.000.000",
                "Pencabutan izin usaha kehutanan"
            ])
            
        if data.get("perdagangan_kayu_ilegal"):
            sanctions.extend([
                "Pidana penjara maksimal 10 tahun",
                "Denda maksimal Rp 10.000.000.000", 
                "Penyitaan kayu ilegal"
            ])
            
        return sanctions
    
    def _timber_tracking_analysis(self, data):
        """Analisis pelacakan kayu ilegal"""
        tracking = []
        
        if data.get("missing_documents"):
            tracking.append("Dokumen angkutan kayu tidak lengkap")
            
        if data.get("false_legality_certificate"):
            tracking.append("Sertifikat legalitas kayu palsu")
            
        if data.get("transport_violations"):
            tracking.append("Pelanggaran transportasi kayu")
            
        if data.get("export_without_license"):
            tracking.append("Ekspor tanpa izin")
            
        return tracking
    
    def _reforestation_needed(self, data):
        """Cek apakah perlu reboisasi"""
        return any([
            data.get("area_damaged", 0) > 0,
            data.get("critical_watershed", False),
            data.get("biodiversity_loss", False)
        ])
    
    def analyze_timber_supply_chain(self, supply_data):
        """Analisis rantai pasok kayu"""
        analysis = {
            "chain_vulnerabilities": [],
            "due_diligence_issues": [],
            "certification_problems": [],
            "recommendations": []
        }
        
        # Vulnerabilities dalam rantai pasok
        if supply_data.get("multiple_handlers"):
            analysis["chain_vulnerabilities"].append("Banyak pihak terlibat - sulit lacak")
            
        if supply_data.get("informal_transport"):
            analysis["chain_vulnerabilities"].append("Transportasi informal")
            
        if supply_data.get("cash_payments"):
            analysis["chain_vulnerabilities"].append("Pembayaran tunai - tidak tercatat")
        
        # Masalah due diligence
        if not supply_data.get("supplier_verification"):
            analysis["due_diligence_issues"].append("Tidak ada verifikasi supplier")
            
        if not supply_data.get("document_tracking"):
            analysis["due_diligence_issues"].append("Tidak ada pelacakan dokumen")
            
        if not supply_data.get("chain_of_custody"):
            analysis["due_diligence_issues"].append("Tidak ada chain of custody")
        
        # Masalah sertifikasi
        if supply_data.get("fake_svlk"):
            analysis["certification_problems"].append("Sertifikat SVLK palsu")
            
        if not supply_data.get("proper_certification"):
            analysis["certification_problems"].append("Tidak ada sertifikasi legalitas")
        
        # Rekomendasi
        analysis["recommendations"] = self._get_supply_chain_recommendations(analysis)
        
        return analysis
    
    def _get_supply_chain_recommendations(self, analysis):
        """Dapatkan rekomendasi perbaikan rantai pasok"""
        recommendations = []
        
        if analysis["chain_vulnerabilities"]:
            recommendations.append("Implementasi sistem traceability kayu")
            
        if analysis["due_diligence_issues"]:
            recommendations.append("Enhanced due diligence untuk semua supplier")
            
        if analysis["certification_problems"]:
            recommendations.append("Verifikasi SVLK dan sertifikat legalitas")
            
        recommendations.extend([
            "Digital documentation system",
            "Third-party auditing",
            "Supplier capacity building"
        ])
        
        return recommendations
    
    def calculate_environmental_loss(self, damage_data):
        """Hitung kerugian lingkungan"""
        losses = []
        
        # Kerugian ekonomi
        timber_value = damage_data.get("timber_value", 0)
        if timber_value > 0:
            losses.append(f"Nilai kayu: Rp {timber_value:,}")
            
        # Kerugian ekologis
        if damage_data.get("carbon_emission"):
            losses.append("Emisi karbon dari deforestasi")
            
        if damage_data.get("biodiversity_loss"):
            losses.append("Kehilangan keanekaragaman hayati")
            
        if damage_data.get("watershed_damage"):
            losses.append("Kerusakan daerah aliran sungai")
            
        if damage_data.get("soil_erosion"):
            losses.append("Erosi tanah dan sedimentasi")
            
        return losses
