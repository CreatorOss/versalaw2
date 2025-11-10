#!/usr/bin/env python3
"""
Tax Law Analyzer - Indonesian Tax Law
Analisis hukum perpajakan berdasarkan UU KUP dan turunannya
"""

class TaxLawAnalyzer:
    def __init__(self):
        self.tax_framework = {
            "uu_kup": "Undang-Undang No. 28/2007 tentang Ketentuan Umum Perpajakan",
            "pph": "Pajak Penghasilan",
            "ppn": "Pajak Pertambahan Nilai",
            "pbb": "Pajak Bumi dan Bangunan"
        }
    
    def analyze_tax_obligations(self, tax_data):
        """Analyze tax obligations for individuals/businesses"""
        analysis_result = {
            "kewajiban_pajak": [],
            "batas_wajib_pajak": [],
            "sanksi_keterlambatan": [],
            "fasilitas_perpajakan": []
        }
        
        # Tax obligations
        if tax_data.get("individual_income"):
            analysis_result["kewajiban_pajak"].append("PPh 21 atas penghasilan pegawai")
            analysis_result["batas_wajib_pajak"].append("PTKP: Rp 54 juta/tahun")
            
        if tax_data.get("business_entity"):
            analysis_result["kewajiban_pajak"].extend([
                "PPh 25 angsuran bulanan",
                "PPN untuk PKP",
                "PPh 29 akhir tahun"
            ])
            
        # Penalties for non-compliance
        analysis_result["sanksi_keterlambatan"].extend([
            "Denda 2% per bulan untuk keterlambatan SPT",
            "Bunga 2% per bulan untuk keterlambatan bayar",
            "Sanksi administratif untuk pelaporan tidak benar"
        ])
        
        # Tax facilities
        analysis_result["fasilitas_perpajakan"].extend([
            "Tax allowance untuk investasi",
            "Tax holiday untuk industri pionir",
            "VAT exemption untuk ekspor"
        ])
        
        return analysis_result

    def analyze_tax_dispute(self, dispute_data):
        """Analyze tax disputes and objections"""
        analysis_result = {
            "jenis_sengketa": [],
            "proses_keberatan": [],
            "banding_pengadilan": [],
            "strategi_penyelesaian": []
        }
        
        # Dispute types
        if dispute_data.get("tax_assessment_dispute"):
            analysis_result["jenis_sengketa"].append("Keberatan atas SKP")
            analysis_result["proses_keberatan"].append("Pengajuan keberatan dalam 3 bulan")
            
        if dispute_data.get("penalty_dispute"):
            analysis_result["jenis_sengketa"].append("Sengketa sanksi administratif")
            analysis_result["proses_keberatan"].append("Bandung ke Pengadilan Pajak")
            
        # Legal process
        analysis_result["banding_pengadilan"].extend([
            "Pengadilan Pajak untuk banding",
            "PTUN untuk sengketa keputusan",
            "MA untuk kasasi"
        ])
        
        # Resolution strategies
        analysis_result["strategi_penyelesaian"].extend([
            "Restitusi pajak untuk kelebihan bayar",
            "Pengampunan pajak (tax amnesty)",
            "Permohonan penghapusan sanksi"
        ])
        
        return analysis_result

    def analyze(self, case_data):
        """Main analysis method"""
        if case_data.get("analysis_type") == "dispute":
            return self.analyze_tax_dispute(case_data)
        else:
            return self.analyze_tax_obligations(case_data)

    def analyze_case(self, case_data):
        """Alias for analyze method"""
        return self.analyze(case_data)
