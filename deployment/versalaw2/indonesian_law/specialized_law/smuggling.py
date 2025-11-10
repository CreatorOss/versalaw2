#!/usr/bin/env python3
"""
VERSALAW2 Smuggling Law Analyzer
Analisis hukum penyelundupan dan customs violations
"""

class SmugglingAnalyzer:
    def __init__(self):
        self.customs_laws = {
            "uu_17_2006": "UU No. 17 Tahun 2006 tentang Kepabeanan",
            "uu_7_2014": "UU No. 7 Tahun 2014 tentang Perdagangan",
            "uu_10_1995": "UU No. 10 Tahun 1995 tentang Kepabeanan"
        }
        
        self.smuggling_types = [
            "barang_terlarang",
            "barang_tertentu", 
            "barang_dilarang",
            "penyelundupan_orang",
            "penyelundupan_hewan",
            "penyelundupan_tanpa_deklarasi"
        ]
        
        self.prohibited_goods = [
            "narkotika",
            "senjata_api",
            "bahan_peledak",
            "barang_elektronik_ilegal",
            "produk_palsu",
            "hewan_lindung",
            "tumbuhan_lindung"
        ]
    
    def analyze_smuggling_case(self, case_data):
        """Analisis kasus penyelundupan"""
        analysis = {
            "smuggling_detected": False,
            "smuggling_type": None,
            "customs_violations": [],
            "prohibited_goods_detected": [],
            "legal_articles": [],
            "customs_duties": 0,
            "fines_and_penalties": [],
            "criminal_liability": False,
            "administrative_sanctions": []
        }
        
        # Deteksi jenis penyelundupan
        for smuggling_type in self.smuggling_types:
            if case_data.get(smuggling_type):
                analysis["smuggling_detected"] = True
                analysis["smuggling_type"] = smuggling_type
        
        # Deteksi barang terlarang
        for goods in self.prohibited_goods:
            if case_data.get(goods):
                analysis["prohibited_goods_detected"].append(goods)
        
        # Pelanggaran kepabeanan
        analysis["customs_violations"] = self._identify_customs_violations(case_data)
        
        # Identifikasi pasal hukum
        analysis["legal_articles"] = self._identify_smuggling_articles(case_data)
        
        # Perhitungan bea cukai
        analysis["customs_duties"] = self._calculate_customs_duties(case_data)
        
        # Denda dan sanksi
        analysis["fines_and_penalties"] = self._calculate_fines_penalties(case_data)
        
        # Pertanggungjawaban pidana
        analysis["criminal_liability"] = self._criminal_liability_check(case_data)
        
        # Sanksi administratif
        analysis["administrative_sanctions"] = self._administrative_sanctions(case_data)
        
        return analysis
    
    def _identify_customs_violations(self, data):
        """Identifikasi pelanggaran kepabeanan"""
        violations = []
        
        if data.get("false_declaration"):
            violations.append("Pernyataan palsu dalam pemberitahuan pabean")
            
        if data.get("undeclared_goods"):
            violations.append("Barang tidak diberitahukan")
            
        if data.get("wrong_tariff_classification"):
            violations.append("Klasifikasi tarif salah")
            
        if data.get("under_valuation"):
            violations.append("Nilai pabean lebih rendah")
            
        if data.get("wrong_origin_declaration"):
            violations.append("Asal barang dinyatakan salah")
            
        return violations
    
    def _identify_smuggling_articles(self, data):
        """Identifikasi pasal UU Kepabeanan"""
        articles = []
        
        if data.get("barang_terlarang"):
            articles.append("Pasal 102 UU 17/2006 - Pidana penjara 5-10 tahun + denda")
            
        if data.get("penyelundupan_orang"):
            articles.append("Pasal 120 UU 17/2006 - Pidana penjara 5-15 tahun")
            
        if data.get("false_declaration"):
            articles.append("Pasal 103 UU 17/2006 - Pidana penjara 2-6 tahun + denda")
            
        if data.get("undeclared_goods"):
            articles.append("Pasal 104 UU 17/2006 - Pidana penjara 2-8 tahun + denda")
            
        return articles
    
    def _calculate_customs_duties(self, data):
        """Hitung bea masuk yang harus dibayar"""
        value = data.get("goods_value", 0)
        duty_rate = data.get("duty_rate", 0.1)  # Default 10%
        
        return value * duty_rate
    
    def _calculate_fines_penalties(self, data):
        """Hitung denda dan sanksi"""
        penalties = []
        value = data.get("goods_value", 0)
        
        if data.get("false_declaration"):
            penalties.append(f"Denda administratif: Rp {max(50000000, value * 0.5):,}")
            
        if data.get("undeclared_goods"):
            penalties.append(f"Denda: 1000% dari bea masuk + pajak")
            
        if data.get("barang_terlarang"):
            penalties.extend([
                "Penyitaan barang",
                "Pencabutan izin usaha",
                "Blacklist importir"
            ])
            
        return penalties
    
    def _criminal_liability_check(self, data):
        """Cek pertanggungjawaban pidana"""
        return any([
            data.get("barang_terlarang"),
            data.get("penyelundupan_orang"),
            data.get("organized_smuggling"),
            data.get("large_scale_operation")
        ])
    
    def _administrative_sanctions(self, data):
        """Sanksi administratif"""
        sanctions = []
        
        if data.get("repeat_violations"):
            sanctions.append("Pencabutan izin impor/ekspor")
            
        if data.get("serious_violation"):
            sanctions.append("Penangguhan kegiatan kepabeanan")
            
        if data.get("tax_evasion"):
            sanctions.append("Kewajiban pembayaran pajak + sanksi administratif")
            
        return sanctions
    
    def analyze_customs_compliance(self, compliance_data):
        """Analisis kepatuhan kepabeanan"""
        analysis = {
            "compliance_score": 0,
            "risk_factors": [],
            "compliance_issues": [],
            "recommendations": [],
            "audit_priority": "low"
        }
        
        # Calculate compliance score (0-100)
        score = 100
        
        if compliance_data.get("late_declarations"):
            score -= 20
            analysis["compliance_issues"].append("Keterlambatan pemberitahuan pabean")
            
        if compliance_data.get("classification_errors"):
            score -= 15
            analysis["compliance_issues"].append("Kesalahan klasifikasi barang")
            
        if compliance_data.get("valuation_issues"):
            score -= 25
            analysis["compliance_issues"].append("Masalah penilaian pabean")
            
        if compliance_data.get("documentation_issues"):
            score -= 10
            analysis["compliance_issues"].append("Dokumen tidak lengkap")
        
        analysis["compliance_score"] = max(0, score)
        
        # Risk factors
        if compliance_data.get("high_value_goods"):
            analysis["risk_factors"].append("Barang bernilai tinggi")
            
        if compliance_data.get("restricted_goods"):
            analysis["risk_factors"].append("Barang dibatasi")
            
        if compliance_data.get("new_supplier"):
            analysis["risk_factors"].append("Supplier baru")
        
        # Recommendations
        if score < 70:
            analysis["recommendations"].extend([
                "Internal audit segera",
                "Training compliance untuk staff",
                "Review prosedur kepabeanan"
            ])
            analysis["audit_priority"] = "high"
        elif score < 85:
            analysis["recommendations"].append("Periodic compliance review")
            analysis["audit_priority"] = "medium"
        else:
            analysis["recommendations"].append("Maintain current practices")
            analysis["audit_priority"] = "low"
        
        return analysis
