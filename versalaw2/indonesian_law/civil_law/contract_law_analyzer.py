#!/usr/bin/env python3
"""
Contract Law Analyzer - Indonesian Civil Law
Analisis hukum perjanjian berdasarkan KUH Perdata Buku III
"""

class ContractLawAnalyzer:
    def __init__(self):
        self.contract_framework = {
            "sumber_hukum": "KUH Perdata Buku III tentang Perikatan",
            "syarat_sah": "Pasal 1320 KUH Perdata",
            "jenis_perjanjian": ["Bernama", "Tidak Bernama", "Konsensuil", "Riil", "Formil"]
        }
    
    def analyze_contract_validity(self, contract_data):
        """Analyze contract validity based on Pasal 1320 KUH Perdata"""
        analysis_result = {
            "syarat_1320": [],
            "keabsahan": "belum_dianalisis",
            "rekomendasi": [],
            "potensi_masalah": []
        }
        
        # Check each requirement of Pasal 1320
        if contract_data.get("kesepakatan"):
            analysis_result["syarat_1320"].append("Kesepakatan para pihak: TERPENUHI")
        else:
            analysis_result["syarat_1320"].append("Kesepakatan para pihak: TIDAK TERPENUHI")
            analysis_result["potensi_masalah"].append("Kesepakatan tidak sah - paksaan/penipuan")
            
        if contract_data.get("kecakapan"):
            analysis_result["syarat_1320"].append("Kecakapan bertindak: TERPENUHI")
        else:
            analysis_result["syarat_1320"].append("Kecakapan bertindak: TIDAK TERPENUHI")
            analysis_result["potensi_masalah"].append("Pihak tidak cakap hukum")
            
        if contract_data.get("objek_tentu"):
            analysis_result["syarat_1320"].append("Objek tertentu: TERPENUHI")
        else:
            analysis_result["syarat_1320"].append("Objek tertentu: TIDAK TERPENUHI")
            analysis_result["potensi_masalah"].append("Objek perjanjian tidak jelas")
            
        if contract_data.get("sebab_halal"):
            analysis_result["syarat_1320"].append("Sebab yang halal: TERPENUHI")
        else:
            analysis_result["syarat_1320"].append("Sebab yang halal: TIDAK TERPENUHI")
            analysis_result["potensi_masalah"].append("Tujuan perjanjian melanggar hukum")
        
        # Determine overall validity
        terpenuhi = len([s for s in analysis_result["syarat_1320"] if "TERPENUHI" in s])
        if terpenuhi == 4:
            analysis_result["keabsahan"] = "SAH"
            analysis_result["rekomendasi"].append("Perjanjian memenuhi semua syarat sah")
        elif terpenuhi >= 2:
            analysis_result["keabsahan"] = "DAPAT DIBATALKAN"
            analysis_result["rekomendasi"].append("Perjanjian dapat dibatalkan oleh pihak tertentu")
        else:
            analysis_result["keabsahan"] = "BATAL DEMI HUKUM"
            analysis_result["rekomendasi"].append("Perjanjian batal demi hukum")
            
        return analysis_result

    def analyze_breach_of_contract(self, breach_data):
        """Analyze breach of contract and remedies"""
        analysis_result = {
            "jenis_wanprestasi": [],
            "konsekuensi_hukum": [],
            "ganti_rugi": [],
            "upaya_hukum": []
        }
        
        if breach_data.get("tidak_penuhi_kewajiban"):
            analysis_result["jenis_wanprestasi"].append("Tidak memenuhi kewajiban")
            analysis_result["konsekuensi_hukum"].append("Wajib ganti rugi (Pasal 1243 KUH Perdata)")
            
        if breach_data.get("terlambat_penuhi"):
            analysis_result["jenis_wanprestasi"].append("Terlambat memenuhi kewajiban")
            analysis_result["konsekuensi_hukum"].append("Bunga moratorium")
            
        if breach_data.get("lakukan_yang_dilarang"):
            analysis_result["jenis_wanprestasi"].append("Melakukan yang dilarang")
            analysis_result["konsekuensi_hukum"].append("Pembatalan perjanjian + ganti rugi")
        
        # Remedies available
        analysis_result["upaya_hukum"].extend([
            "Gugatan ganti rugi ke Pengadilan Negeri",
            "Pembatalan perjanjian",
            "Pemenuhan perjanjian paksa",
            "Ganti rugi immateriil"
        ])
        
        # Calculate damages
        if breach_data.get("kerugian_dokumentasi"):
            analysis_result["ganti_rugi"].append("Ganti rugi materiil: nilai kerugian + bunga")
            analysis_result["ganti_rugi"].append("Biaya perkara dan honorarium pengacara")
            
        return analysis_result

    def analyze(self, case_data):
        """Main analysis method"""
        if case_data.get("analysis_type") == "validity":
            return self.analyze_contract_validity(case_data)
        elif case_data.get("analysis_type") == "breach":
            return self.analyze_breach_of_contract(case_data)
        else:
            return self.analyze_contract_validity(case_data)

    def analyze_case(self, case_data):
        """Alias for analyze method"""
        return self.analyze(case_data)
