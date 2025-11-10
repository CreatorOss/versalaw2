#!/usr/bin/env python3
"""
VERSALAW2 Human Trafficking Law Analyzer - OPTIMIZED
Analisis tindak pidana perdagangan orang
"""

class HumanTraffickingAnalyzer:
    def __init__(self):
        self.tppo_laws = {
            "uu_21_2007": "UU No. 21 Tahun 2007 tentang Pemberantasan Tindak Pidana Perdagangan Orang",
            "uu_39_2004": "UU No. 39 Tahun 2004 tentang Penempatan dan Perlindungan TKI Luar Negeri",
            "uu_13_2006": "UU No. 13 Tahun 2006 tentang Perlindungan Saksi dan Korban"
        }
        
        self.trafficking_elements = [
            "perekrutan",
            "pengangkutan", 
            "penampungan",
            "pengiriman",
            "penerimaan",
            "penjeratan_utang",
            "penipuan",
            "pemalsuan_dokumen"
        ]
        
        self.exploitation_forms = [
            "eksploitasi_seksual",
            "pekerja_rumah_tangga",
            "perbudakan", 
            "pengambilan_organ",
            "perkawinan_paksa",
            "pekerja_paksa"
        ]
    
    def analyze_trafficking_case(self, case_data):
        """Analisis kasus perdagangan orang - OPTIMIZED"""
        analysis = {
            "tppo_detected": False,
            "trafficking_elements": [],
            "exploitation_forms": [],
            "victim_protection": [],
            "witness_protection": False,
            "cross_border_issues": [],
            "legal_articles": [],
            "rehabilitation_needs": [],
            "sanctions": []
        }
        
        # Deteksi unsur TPPO - IMPROVED
        for element in self.trafficking_elements:
            if case_data.get(element):
                analysis["trafficking_elements"].append(element)
                analysis["tppo_detected"] = True
        
        # Identifikasi bentuk eksploitasi
        for exploitation in self.exploitation_forms:
            if case_data.get(exploitation):
                analysis["exploitation_forms"].append(exploitation)
        
        # Perlindungan korban
        analysis["victim_protection"] = self._victim_protection_analysis(case_data)
        
        # Perlindungan saksi
        analysis["witness_protection"] = self._witness_protection_needed(case_data)
        
        # Aspek lintas batas
        analysis["cross_border_issues"] = self._cross_border_analysis(case_data)
        
        # Pasal hukum
        analysis["legal_articles"] = self._identify_tppo_articles(case_data, analysis)
        
        # Rehabilitasi
        analysis["rehabilitation_needs"] = self._rehabilitation_assessment(case_data)
        
        # Sanksi
        analysis["sanctions"] = self._calculate_sanctions(analysis)
        
        return analysis
    
    def _victim_protection_analysis(self, data):
        """Analisis kebutuhan perlindungan korban"""
        protections = []
        
        if data.get("underage_victim"):
            protections.extend([
                "Perlindungan khusus anak",
                "Pendampingan psikologis",
                "Pendidikan alternatif"
            ])
        
        if data.get("physical_violence"):
            protections.extend([
                "Perawatan medis",
                "Rehabilitasi fisik",
                "Terapi trauma"
            ])
            
        if data.get("sexual_exploitation"):
            protections.extend([
                "Konseling khusus",
                "Testing kesehatan",
                "Reintegrasi sosial"
            ])
            
        if data.get("psychological_trauma"):
            protections.append("Dukungan kesehatan mental jangka panjang")
            
        return protections
    
    def _witness_protection_needed(self, data):
        """Cek apakah perlu perlindungan saksi"""
        return any([
            data.get("witness_intimidation", False),
            data.get("organized_crime_involvement", False),
            data.get("high_profile_case", False),
            data.get("violent_offenders", False)
        ])
    
    def _cross_border_analysis(self, data):
        """Analisis aspek lintas batas"""
        issues = []
        
        if data.get("international_trafficking"):
            issues.extend([
                "Kerjasama bilateral diperlukan",
                "Interpol notification",
                "Diplomatic channels"
            ])
            
        if data.get("false_documents"):
            issues.append("Pemalsuan dokumen perjalanan")
            
        if data.get("corrupt_officials"):
            issues.append("Keterlibatan oknum aparat")
            
        if data.get("multiple_countries"):
            issues.append("Jaringan lintas beberapa negara")
            
        return issues
    
    def _identify_tppo_articles(self, data, analysis):
        """Identifikasi pasal UU TPPO yang dilanggar - IMPROVED"""
        articles = []
        elements = analysis.get("trafficking_elements", [])
        exploitations = analysis.get("exploitation_forms", [])
        
        # Pasal berdasarkan unsur yang terpenuhi
        if any(element in elements for element in ["perekrutan", "pengangkutan", "penampungan"]):
            articles.append("Pasal 2 UU 21/2007 - Tindak pidana perdagangan orang")
            
        if "eksploitasi_seksual" in exploitations:
            articles.append("Pasal 4 UU 21/2007 - Eksploitasi seksual")
            
        if "perbudakan" in exploitations:
            articles.append("Pasal 5 UU 21/2007 - Perbudakan")
            
        if "pengambilan_organ" in exploitations:
            articles.append("Pasal 7 UU 21/2007 - Pengambilan organ")
            
        if "penjeratan_utang" in elements:
            articles.append("Pasal 10 UU 21/2007 - Penjeratan utang")
            
        # Default article if trafficking detected
        if analysis["tppo_detected"] and not articles:
            articles.append("Pasal 2 UU 21/2007 - Tindak pidana perdagangan orang")
            
        return articles
    
    def _rehabilitation_assessment(self, data):
        """Assessment kebutuhan rehabilitasi"""
        needs = []
        
        if data.get("psychological_trauma"):
            needs.append("Rehabilitasi psikologis")
            
        if data.get("physical_injury"):
            needs.append("Rehabilitasi fisik")
            
        if data.get("social_stigma"):
            needs.append("Reintegrasi sosial")
            
        if data.get("economic_deprivation"):
            needs.append("Bantuan ekonomi dan pelatihan kerja")
            
        if data.get("addiction_issues"):
            needs.append("Rehabilitasi kecanduan")
            
        return needs
    
    def _calculate_sanctions(self, analysis):
        """Hitung sanksi berdasarkan analisis"""
        sanctions = []
        
        if analysis["tppo_detected"]:
            sanctions.extend([
                "Pidana penjara 3-15 tahun",
                "Denda Rp 120.000.000 - 600.000.000"
            ])
            
        if "eksploitasi_seksual" in analysis["exploitation_forms"]:
            sanctions.append("Pidana penjara 5-15 tahun + denda hingga Rp 600.000.000")
            
        if "perbudakan" in analysis["exploitation_forms"]:
            sanctions.append("Pidana penjara 5-15 tahun")
            
        if analysis.get("underage_victim"):
            sanctions.append("Pemberatan 1/3 dari pidana pokok")
            
        return sanctions
    
    def analyze_trafficking_modus(self, modus_data):
        """Analisis modus operandi perdagangan orang"""
        common_modus = {
            "penawaran_kerja": "Janji kerja dengan gaji tinggi",
            "pernikahan_palsu": "Modus perjodohan atau nikah kontrak", 
            "penipuan_umroh": "Modus perjalanan ibadah",
            "adopsi_ilegal": "Modus pengambilan anak",
            "beasiswa_palsu": "Modus beasiswa pendidikan",
            "artis_palsu": "Modus pencarian bakat"
        }
        
        detected_modus = []
        for modus, description in common_modus.items():
            if modus_data.get(modus):
                detected_modus.append({
                    "modus": modus,
                    "description": description,
                    "prevention": self._get_prevention_measures(modus)
                })
                
        return detected_modus
    
    def _get_prevention_measures(self, modus):
        """Dapatkan langkah pencegahan berdasarkan modus"""
        prevention_measures = {
            "penawaran_kerja": [
                "Verifikasi perusahaan penempatan",
                "Cek izin PPTKIS",
                "Hindari biaya berlebihan",
                "Pastikan kontrak kerja jelas"
            ],
            "pernikahan_palsu": [
                "Verifikasi calon pasangan",
                "Konseling pra-nikah",
                "Pelaporan ke pihak berwajib",
                "Hindari pernikahan online"
            ],
            "penipuan_umroh": [
                "Pastikan biro travel berizin",
                "Verifikasi paket perjalanan",
                "Hindari penawaran harga terlalu murah"
            ]
        }
        return prevention_measures.get(modus, ["Edukasi dan kewaspadaan umum"])
    
    def generate_protection_plan(self, analysis):
        """Generate rencana perlindungan korban"""
        return {
            "immediate_needs": [
                "Tempat tinggal aman",
                "Bantuan medis",
                "Konseling psikologis",
                "Bantuan hukum"
            ],
            "medium_term": analysis["rehabilitation_needs"],
            "long_term": [
                "Reintegrasi sosial",
                "Bantuan pekerjaan",
                "Pendampingan berkelanjutan"
            ],
            "legal_assistance": [
                "Pendampingan proses hukum",
                "Bantuan restitusi",
                "Perlindungan identitas"
            ]
        }
