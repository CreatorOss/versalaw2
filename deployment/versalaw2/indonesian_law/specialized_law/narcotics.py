#!/usr/bin/env python3
"""
VERSALAW2 Narcotics Law Analyzer - FIXED VERSION
Analisis hukum narkotika dan psikotropika
"""

class NarcoticsAnalyzer:
    def __init__(self):
        self.narcotics_laws = {
            "uu_35_2009": "UU No. 35 Tahun 2009 tentang Narkotika",
            "uu_5_1997": "UU No. 5 Tahun 1997 tentang Psikotropika"
        }
        
        self.narcotics_categories = {
            "category_1": ["ganja", "heroin", "kokain", "sabu", "ekstasi", "shabu", "methamphetamine"],
            "category_2": ["morfin", "petidin", "metadon"],
            "category_3": ["kodein", "difenoksilat"]
        }
        
        self.narcotics_offenses = [
            "produksi_narkotika",
            "peredaran_narkotika", 
            "kepemilikan_narkotika",
            "penggunaan_narkotika",
            "pencucian_uang_narkotika",
            "penyalahgunaan_wewenang"
        ]
    
    def analyze_narcotics_case(self, case_data):
        """Analisis kasus narkotika komprehensif - FIXED"""
        analysis = {
            "narcotics_detected": False,
            "narcotics_category": None,
            "offenses_detected": [],
            "quantity_analysis": {},
            "legal_articles": [],
            "sanctions": [],
            "aggravating_factors": [],
            "mitigating_factors": [],
            "rehabilitation_possible": False
        }
        
        # Deteksi jenis narkotika - IMPROVED
        narcotic_type = case_data.get("narcotic_type", "").lower()
        if narcotic_type:
            analysis["narcotics_detected"] = True
            analysis["narcotics_category"] = self._categorize_narcotic(narcotic_type)
        
        # Deteksi pelanggaran - FIXED LOGIC
        for offense in self.narcotics_offenses:
            if case_data.get(offense):
                analysis["offenses_detected"].append(offense)
        
        # Analisis kuantitas
        analysis["quantity_analysis"] = self._analyze_quantity(case_data)
        
        # Identifikasi pasal hukum - FIXED
        analysis["legal_articles"] = self._identify_narcotics_articles(case_data, analysis)
        
        # Analisis sanksi
        analysis["sanctions"] = self._calculate_narcotics_sanctions(case_data, analysis)
        
        # Faktor memberatkan dan meringankan
        analysis["aggravating_factors"] = self._identify_aggravating_factors(case_data)
        analysis["mitigating_factors"] = self._identify_mitigating_factors(case_data)
        
        # Kemungkinan rehabilitasi
        analysis["rehabilitation_possible"] = self._rehabilitation_eligibility(case_data, analysis)
        
        return analysis
    
    def _categorize_narcotic(self, narcotic_type):
        """Kategorikan jenis narkotika - IMPROVED"""
        narcotic_type = narcotic_type.lower()
        
        for category, substances in self.narcotics_categories.items():
            for substance in substances:
                if substance in narcotic_type:
                    return category
        return "unknown"
    
    def _analyze_quantity(self, data):
        """Analisis kuantitas narkotika"""
        quantity = data.get("quantity", 0)
        unit = data.get("unit", "gram")
        
        analysis = {
            "quantity": quantity,
            "unit": unit,
            "weight_category": self._get_weight_category(quantity, unit),
            "threshold_analysis": self._threshold_analysis(quantity, unit, data.get("narcotic_type", ""))
        }
        
        return analysis
    
    def _get_weight_category(self, quantity, unit):
        """Tentukan kategori berat untuk sanksi - IMPROVED"""
        # Convert to grams for standardization
        if unit == "gram":
            weight_grams = quantity
        elif unit == "kilogram":
            weight_grams = quantity * 1000
        else:
            weight_grams = quantity
        
        if weight_grams >= 1000:  # 1 kg
            return "berat_penjual"
        elif weight_grams >= 5:   # 5 gram
            return "berat_pengedar" 
        else:
            return "ringan_pemakai"
    
    def _threshold_analysis(self, quantity, unit, narcotic_type):
        """Analisis terhadap threshold hukum - IMPROVED"""
        narcotic_type = narcotic_type.lower()
        
        thresholds = {
            "ganja": {"pengedar": 1000, "bandar": 5000},  # gram
            "sabu": {"pengedar": 5, "bandar": 50},        # gram
            "shabu": {"pengedar": 5, "bandar": 50},       # gram
            "methamphetamine": {"pengedar": 5, "bandar": 50}, # gram
            "ekstasi": {"pengedar": 50, "bandar": 200},   # tablet
            "heroin": {"pengedar": 5, "bandar": 25}       # gram
        }
        
        # Find matching threshold
        for narc_type, thresh in thresholds.items():
            if narc_type in narcotic_type:
                if quantity >= thresh["bandar"]:
                    return "BANDAR - Sanksi maksimal"
                elif quantity >= thresh["pengedar"]:
                    return "PENGEDAR - Sanksi berat"
                else:
                    return "PEMAKAI - Rehabilitasi mungkin"
        
        return "ANALISIS BERDASARKAN BERAT DAN JENIS"
    
    def _identify_narcotics_articles(self, data, analysis):
        """Identifikasi pasal UU Narkotika - FIXED & IMPROVED"""
        articles = []
        category = analysis.get("narcotics_category")
        weight_cat = analysis["quantity_analysis"].get("weight_category")
        offenses = analysis.get("offenses_detected", [])
        
        # Check for specific offenses
        if "peredaran_narkotika" in offenses:
            if category == "category_1":
                if weight_cat == "berat_penjual":
                    articles.append("Pasal 113 ayat (2) UU 35/2009 - Pidana mati/penjara seumur hidup")
                else:
                    articles.append("Pasal 112 UU 35/2009 - Pidana penjara 5-20 tahun")
            elif category == "category_2":
                articles.append("Pasal 114 UU 35/2009 - Pidana penjara 4-12 tahun")
            else:
                articles.append("Pasal 111 UU 35/2009 - Pidana penjara 4-12 tahun")
        
        if "kepemilikan_narkotika" in offenses:
            if weight_cat == "ringan_pemakai":
                articles.append("Pasal 127 UU 35/2009 - Rehabilitasi atau pidana maksimal 4 tahun")
            else:
                articles.append("Pasal 111 UU 35/2009 - Pidana penjara 4-12 tahun")
            
        if "penggunaan_narkotika" in offenses:
            articles.append("Pasal 127 UU 35/2009 - Rehabilitasi atau pidana")
            
        if "produksi_narkotika" in offenses:
            articles.append("Pasal 113 UU 35/2009 - Pidana penjara 5-20 tahun")
            
        # Default article if no specific ones identified
        if not articles and analysis["narcotics_detected"]:
            articles.append("Pasal 111 UU 35/2009 - Kepemilikan narkotika")
            
        return articles
    
    def _calculate_narcotics_sanctions(self, data, analysis):
        """Hitung sanksi narkotika - IMPROVED"""
        sanctions = []
        weight_cat = analysis["quantity_analysis"].get("weight_category")
        category = analysis.get("narcotics_category")
        offenses = analysis.get("offenses_detected", [])
        
        if weight_cat == "berat_penjual" and category == "category_1":
            sanctions.extend([
                "Pidana mati",
                "Pidana penjara seumur hidup", 
                "Pidana penjara minimal 5 tahun",
                "Denda maksimal Rp 10.000.000.000"
            ])
        elif weight_cat == "berat_pengedar" or "peredaran_narkotika" in offenses:
            sanctions.extend([
                "Pidana penjara 5-20 tahun",
                "Denda Rp 1.000.000.000 - 10.000.000.000"
            ])
        elif weight_cat == "ringan_pemakai" and "penggunaan_narkotika" in offenses:
            sanctions.extend([
                "Rehabilitasi",
                "Pidana penjara maksimal 4 tahun",
                "Denda maksimal Rp 1.000.000.000"
            ])
        else:
            sanctions.extend([
                "Pidana penjara 4-12 tahun",
                "Denda Rp 800.000.000 - 8.000.000.000"
            ])
            
        return sanctions
    
    def _identify_aggravating_factors(self, data):
        """Identifikasi faktor memberatkan"""
        aggravating = []
        
        if data.get("involved_minors"):
            aggravating.append("Melibatkan anak di bawah umur")
            
        if data.get("international_network"):
            aggravating.append("Jaringan internasional")
            
        if data.get("violence_used"):
            aggravating.append("Penggunaan kekerasan")
            
        if data.get("repeat_offender"):
            aggravating.append("Residivis/pelaku berulang")
            
        if data.get("large_quantity"):
            aggravating.append("Kuantitas sangat besar")
            
        if data.get("near_school"):
            aggravating.append("Beroperasi dekat sekolah")
            
        return aggravating
    
    def _identify_mitigating_factors(self, data):
        """Identifikasi faktor meringankan"""
        mitigating = []
        
        if data.get("first_time_offender"):
            mitigating.append("Pelaku pertama kali")
            
        if data.get("cooperated_with_authorities"):
            mitigating.append("Kerjasama dengan penyidik")
            
        if data.get("addicted_user"):
            mitigating.append("Pengguna ketergantungan")
            
        if data.get("voluntary_surrender"):
            mitigating.append("Menyerahkan diri")
            
        if data.get("information_provided"):
            mitigating.append("Memberikan informasi berharga")
            
        return mitigating
    
    def _rehabilitation_eligibility(self, data, analysis):
        """Cek kelayakan rehabilitasi - IMPROVED"""
        offenses = analysis.get("offenses_detected", [])
        weight_cat = analysis["quantity_analysis"].get("weight_category")
        
        return any([
            data.get("addicted_user", False),
            data.get("first_time_offender", False),
            weight_cat == "ringan_pemakai",
            "penggunaan_narkotika" in offenses,
            not any(offense in offenses for offense in ["peredaran_narkotika", "produksi_narkotika"])
        ])
    
    def analyze_drug_trafficking_network(self, network_data):
        """Analisis jaringan perdagangan narkotika"""
        analysis = {
            "network_scale": "local",
            "modus_operandi": [],
            "money_laundering_risk": False,
            "international_aspects": [],
            "enforcement_recommendations": []
        }
        
        # Scale analysis
        if network_data.get("international_connections"):
            analysis["network_scale"] = "international"
        elif network_data.get("national_network"):
            analysis["network_scale"] = "national"
        elif network_data.get("regional_network"):
            analysis["network_scale"] = "regional"
        
        # Modus operandi
        modus_mapping = {
            "concealment_methods": "Metode penyembunyian",
            "transport_methods": "Metode transportasi",
            "payment_methods": "Metode pembayaran",
            "recruitment_methods": "Metode perekrutan",
            "online_distribution": "Distribusi online",
            "cryptocurrency_payments": "Pembayaran cryptocurrency"
        }
        
        for modus_key, modus_desc in modus_mapping.items():
            if network_data.get(modus_key):
                analysis["modus_operandi"].append(modus_desc)
        
        # Money laundering risk
        analysis["money_laundering_risk"] = any([
            network_data.get("large_cash_transactions"),
            network_data.get("shell_companies"),
            network_data.get("offshore_accounts"),
            network_data.get("cryptocurrency_payments")
        ])
        
        # International aspects
        if network_data.get("cross_border"):
            analysis["international_aspects"].extend([
                "Kerjasama bilateral diperlukan",
                "Interpol notification",
                "Mutual Legal Assistance"
            ])
        
        # Enforcement recommendations
        analysis["enforcement_recommendations"] = self._get_network_enforcement_recommendations(analysis)
        
        return analysis
    
    def _get_network_enforcement_recommendations(self, analysis):
        """Rekomendasi penegakan hukum untuk jaringan"""
        recommendations = []
        
        if analysis["network_scale"] == "international":
            recommendations.extend([
                "Task force lintas negara",
                "Financial investigation",
                "Undercover operations",
                "Controlled delivery"
            ])
        elif analysis["network_scale"] == "national":
            recommendations.extend([
                "Multi-agency task force",
                "Asset tracking",
                "Communications interception",
                "Surveillance operations"
            ])
        else:
            recommendations.extend([
                "Local surveillance",
                "Community intelligence",
                "Targeted arrests",
                "Buy-bust operations"
            ])
            
        if analysis["money_laundering_risk"]:
            recommendations.append("PPATK coordination for financial tracking")
            
        if analysis["modus_operandi"]:
            recommendations.append("Counter-measures for identified modus operandi")
            
        return recommendations
    
    def generate_legal_report(self, analysis):
        """Generate comprehensive legal report"""
        return {
            "case_summary": {
                "narcotics_detected": analysis["narcotics_detected"],
                "category": analysis["narcotics_category"],
                "offenses": analysis["offenses_detected"]
            },
            "legal_basis": analysis["legal_articles"],
            "sentencing_analysis": {
                "sanctions": analysis["sanctions"],
                "aggravating_factors": analysis["aggravating_factors"],
                "mitigating_factors": analysis["mitigating_factors"],
                "rehabilitation_possible": analysis["rehabilitation_possible"]
            },
            "quantity_analysis": analysis["quantity_analysis"],
            "recommendations": [
                "Forensic analysis of substances",
                "Financial investigation if applicable",
                "Rehabilitation assessment if eligible"
            ]
        }
