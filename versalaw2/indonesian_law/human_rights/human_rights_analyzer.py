#!/usr/bin/env python3
"""
Human Rights Analyzer - Indonesian Law
Analisis Hak Asasi Manusia berdasarkan UU No. 39/1999 tentang HAM dan instrumen internasional
"""

class HumanRightsAnalyzer:
    def __init__(self):
        self.human_rights_framework = {
            "uu_ham": "Undang-Undang No. 39/1999 tentang Hak Asasi Manusia",
            "komnas_ham": "Komisi Nasional Hak Asasi Manusia",
            "duham": "Deklarasi Universal Hak Asasi Manusia 1948",
            "iccpr": "Kovenan Internasional tentang Hak-Hak Sipil dan Politik",
            "icescr": "Kovenan Internasional tentang Hak-Hak Ekonomi, Sosial, dan Budaya"
        }
        
        self.human_rights_categories = {
            "hak_sipil_politik": [
                "Hak Hidup",
                "Hak Bebas dari Penyiksaan",
                "Hak Kebebasan Berpendapat",
                "Hak Berkumpul dan Berserikat",
                "Hak Berpartisipasi dalam Pemerintahan"
            ],
            "hak_ekonomi_sosial_budaya": [
                "Hak atas Pekerjaan",
                "Hak atas Kesehatan", 
                "Hak atas Pendidikan",
                "Hak atas Perumahan yang Layak",
                "Hak atas Jaminan Sosial"
            ],
            "hak_kelompok_rentan": [
                "Hak Perempuan",
                "Hak Anak",
                "Hak Penyandang Disabilitas",
                "Hak Masyarakat Adat",
                "Hak Pengungsi"
            ]
        }

    def analyze_human_rights_violation(self, case_data):
        """Analyze potential human rights violations"""
        analysis_result = {
            "violated_rights": [],
            "violation_severity": "low",
            "accountability_mechanisms": [],
            "remedial_measures": [],
            "international_mechanisms": []
        }
        
        # Check for civil-political rights violations
        if case_data.get("extrajudicial_killing"):
            analysis_result["violated_rights"].append("Hak Hidup (Pasal 9 UU HAM)")
            analysis_result["violation_severity"] = "very_high"
            analysis_result["accountability_mechanisms"].append("Pelaporan ke Komnas HAM")
            
        if case_data.get("torture_cruel_treatment"):
            analysis_result["violated_rights"].append("Hak Bebas dari Penyiksaan (Pasal 33 UU HAM)")
            analysis_result["violation_severity"] = "high"
            analysis_result["remedial_measures"].append("Rehabilitasi medis dan psikologis")
            
        if case_data.get("arbitrary_detention"):
            analysis_result["violated_rights"].append("Hak Kebebasan dan Keamanan Pribadi (Pasal 28D UUD 1945)")
            analysis_result["violation_severity"] = "medium"
            analysis_result["remedial_measures"].append("Gugatan ganti rugi")
            
        if case_data.get("freedom_of_expression_violation"):
            analysis_result["violated_rights"].append("Hak Kebebasan Mengeluarkan Pendapat (Pasal 23-28 UU HAM)")
            analysis_result["violation_severity"] = "medium"
            
        # Check for economic-social-cultural rights violations
        if case_data.get("forced_eviction"):
            analysis_result["violated_rights"].append("Hak atas Perumahan yang Layak (Pasal 40 UU HAM)")
            analysis_result["violation_severity"] = "high"
            analysis_result["remedial_measures"].append("Pemulihan tempat tinggal dan ganti rugi")
            
        if case_data.get("discrimination_employment"):
            analysis_result["violated_rights"].append("Hak atas Pekerjaan (Pasal 38 UU HAM)")
            analysis_result["violation_severity"] = "medium"
            
        # Determine international mechanisms for severe violations
        if analysis_result["violation_severity"] in ["high", "very_high"]:
            analysis_result["international_mechanisms"].extend([
                "Pelaporan ke Pelapor Khusus PBB",
                "Komunikasi ke Mekanisme HAM PBB",
                "Universal Periodic Review (UPR)"
            ])
            
        return analysis_result

    def analyze_business_human_rights(self, business_data):
        """Analyze business and human rights impacts (UN Guiding Principles)"""
        analysis_result = {
            "human_rights_impacts": [],
            "due_diligence_requirements": [],
            "remediation_obligations": [],
            "stakeholder_engagement": []
        }
        
        # Analyze business impacts on human rights
        if business_data.get("environmental_pollution"):
            analysis_result["human_rights_impacts"].append("Hak atas Kesehatan dan Lingkungan Hidup yang Sehat")
            analysis_result["due_diligence_requirements"].append("Assessmen dampak HAM wajib")
            
        if business_data.get("land_conflict"):
            analysis_result["human_rights_impacts"].append("Hak atas Tanah dan Sumber Daya Alam Masyarakat Adat")
            analysis_result["stakeholder_engagement"].append("Konsultasi bermakna dengan masyarakat terdampak")
            
        if business_data.get("labor_rights_violation"):
            analysis_result["human_rights_impacts"].append("Hak atas Kondisi Kerja yang Layak")
            analysis_result["remediation_obligations"].append("Ganti rugi dan pemulihan hak pekerja")
            
        return analysis_result

    def analyze_transitional_justice(self, transitional_data):
        """Analyze transitional justice mechanisms for past human rights violations"""
        analysis_result = {
            "truth_seeking": [],
            "criminal_accountability": [],
            "reparations": [],
            "institutional_reform": [],
            "guarantees_non_recurrence": []
        }
        
        if transitional_data.get("gross_human_rights_violations"):
            analysis_result["truth_seeking"].append("Pembentukan Komisi Kebenaran dan Rekonsiliasi")
            analysis_result["criminal_accountability"].append("Pengadilan HAM untuk kejahatan berat")
            analysis_result["reparations"].append("Program reparasi untuk korban dan keluarga")
            analysis_result["institutional_reform"].append("Reformasi sektor keamanan dan peradilan")
            
        return analysis_result

    def analyze(self, case_data):
        """Main analysis method"""
        if case_data.get("analysis_type") == "business_human_rights":
            return self.analyze_business_human_rights(case_data)
        elif case_data.get("analysis_type") == "transitional_justice":
            return self.analyze_transitional_justice(case_data)
        else:
            return self.analyze_human_rights_violation(case_data)

    def analyze_case(self, case_data):
        """Alias for analyze method"""
        return self.analyze(case_data)
