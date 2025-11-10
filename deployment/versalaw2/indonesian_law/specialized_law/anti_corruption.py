#!/usr/bin/env python3
"""
VERSALAW2 Anti-Corruption Law Analyzer (Tipikor)
Analisis hukum korupsi berdasarkan UU Tipikor
"""

class AntiCorruptionAnalyzer:
    def __init__(self):
        self.tipikor_laws = {
            "uu_31_1999": "UU No. 31 Tahun 1999 tentang Pemberantasan Tindak Pidana Korupsi",
            "uu_20_2001": "UU No. 20 Tahun 2001 tentang Perubahan atas UU No. 31 Tahun 1999",
            "uu_30_2002": "UU No. 30 Tahun 2002 tentang Komisi Pemberantasan Tindak Pidana Korupsi"
        }
        
        self.corruption_elements = [
            "melawan_hukum",
            "merugikan_keuangan_negara", 
            "memperkaya_diri_sendiri",
            "penyalahgunaan_wewenang"
        ]
    
    def analyze_corruption_case(self, case_data):
        """Analisis kasus korupsi komprehensif"""
        analysis = {
            "legal_basis": [],
            "corruption_elements": [],
            "potential_articles": [],
            "sanctions": [],
            "kpk_jurisdiction": False,
            "issues_detected": []
        }
        
        # Analisis unsur korupsi
        for element in self.corruption_elements:
            if case_data.get(element):
                analysis["corruption_elements"].append(element)
        
        # Deteksi yurisdiksi KPK
        if self._is_kpk_jurisdiction(case_data):
            analysis["kpk_jurisdiction"] = True
            analysis["legal_basis"].append(self.tipikor_laws["uu_30_2002"])
        
        # Tentukan pasal yang dilanggar
        analysis["potential_articles"] = self._identify_violated_articles(case_data)
        
        # Analisis sanksi
        analysis["sanctions"] = self._calculate_sanctions(case_data)
        
        return analysis
    
    def _is_kpk_jurisdiction(self, case_data):
        """Cek apakah masuk yurisdiksi KPK"""
        criteria = [
            case_data.get("kerugian_negara", 0) >= 1000000000,  # 1 Miliar
            case_data.get("melibatkan_aparatur_negara", False),
            case_data.get("terlibat_petinggi", False),
            case_data.get("perhatian_umum", False)
        ]
        return any(criteria)
    
    def _identify_violated_articles(self, case_data):
        """Identifikasi pasal UU Tipikor yang dilanggar"""
        articles = []
        
        if case_data.get("merugikan_keuangan_negara"):
            articles.append("Pasal 2 UU 31/1999 jo UU 20/2001")
        
        if case_data.get("penyalahgunaan_wewenang"):
            articles.append("Pasal 3 UU 31/1999 jo UU 20/2001")
            
        if case_data.get("gratifikasi"):
            articles.append("Pasal 12B UU 20/2001")
            
        if case_data.get("pencucian_uang"):
            articles.append("Pasal 3 UU 8/2010 tentang TPPU")
        
        return articles
    
    def _calculate_sanctions(self, case_data):
        """Hitung potensi sanksi"""
        sanctions = []
        kerugian = case_data.get("kerugian_negara", 0)
        
        if kerugian > 0:
            sanctions.append(f"Pidana penjara minimal 4 tahun")
            sanctions.append(f"Denda minimal 200 juta rupiah")
            sanctions.append(f"Penggantian kerugian negara: {kerugian:,}")
            
        if case_data.get("perberatan"):
            sanctions.append("Pidana penjara seumur hidup atau mati")
            
        return sanctions
    
    def analyze_gratification(self, gratification_data):
        """Analisis khusus gratifikasi"""
        return {
            "obligation": "Lapor ke KPK dalam 30 hari kerja",
            "consequence": "Menjadi uang negara jika tidak dilaporkan",
            "sanction": "Pidana penjara dan denda"
        }
