#!/usr/bin/env python3
"""
VERSALAW2 Terrorism Law Analyzer
Analisis UU Terorisme dan kejahatan terorisme di Indonesia
"""

class TerrorismLawAnalyzer:
    def __init__(self):
        self.terrorism_laws = {
            "uu_5_2018": "UU No. 5 Tahun 2018 tentang Perubahan atas UU No. 15 Tahun 2003 tentang Penetapan Perppu No. 1 Tahun 2002 tentang Pemberantasan Tindak Pidana Terorisme",
            "uu_15_2003": "UU No. 15 Tahun 2003 tentang Penetapan Perppu No. 1 Tahun 2002",
            "uu_9_2013": "UU No. 9 Tahun 2013 tentang Pencegahan dan Pemberantasan Tindak Pidana Pendanaan Terorisme"
        }
        
        self.terrorism_offenses = [
            "perencanaan_terorisme",
            "pelaksanaan_terorisme", 
            "pendanaan_terorisme",
            "pelatihan_terorisme",
            "rekrutmen_terorisme",
            "penyebaran_ideologi_terorisme"
        ]
        
        self.terrorist_organizations = [
            "jemaah_islamiyah",
            "isis_indonesia", 
            "jamaah_ansharut_daulah",
            "mitra_isis_lokal"
        ]
    
    def analyze_terrorism_case(self, case_data):
        """Analisis kasus terorisme komprehensif"""
        analysis = {
            "terrorism_detected": False,
            "terrorism_offenses": [],
            "terrorist_organization": None,
            "legal_articles": [],
            "preventive_measures": [],
            "investigation_powers": [],
            "sanctions": [],
            "deradicalization_possible": False
        }
        
        # Deteksi kejahatan terorisme
        for offense in self.terrorism_offenses:
            if case_data.get(offense):
                analysis["terrorism_offenses"].append(offense)
                analysis["terrorism_detected"] = True
        
        # Identifikasi organisasi teroris
        analysis["terrorist_organization"] = self._identify_terrorist_org(case_data)
        
        # Pasal hukum
        analysis["legal_articles"] = self._identify_terrorism_articles(case_data)
        
        # Tindakan pencegahan
        analysis["preventive_measures"] = self._preventive_measures(case_data)
        
        # Wewenang penyidikan
        analysis["investigation_powers"] = self._investigation_powers(case_data)
        
        # Sanksi
        analysis["sanctions"] = self._calculate_terrorism_sanctions(case_data)
        
        # Kemungkinan deradikalisasi
        analysis["deradicalization_possible"] = self._deradicalization_eligibility(case_data)
        
        return analysis
    
    def _identify_terrorist_org(self, data):
        """Identifikasi organisasi teroris"""
        for org in self.terrorist_organizations:
            if data.get(org):
                return org
        return "unknown_organization"
    
    def _identify_terrorism_articles(self, data):
        """Identifikasi pasal UU Terorisme"""
        articles = []
        
        if data.get("perencanaan_terorisme"):
            articles.append("Pasal 13 UU 5/2018 - Perencanaan tindak pidana terorisme")
            
        if data.get("pelaksanaan_terorisme"):
            articles.append("Pasal 14 UU 5/2018 - Melakukan tindak pidana terorisme")
            
        if data.get("pendanaan_terorisme"):
            articles.append("Pasal 12 UU 5/2018 - Pendanaan terorisme")
            
        if data.get("rekrutmen_terorisme"):
            articles.append("Pasal 15 UU 5/2018 - Rekrutmen untuk terorisme")
            
        if data.get("pelatihan_terorisme"):
            articles.append("Pasal 16 UU 5/2018 - Pelatihan untuk terorisme")
            
        return articles
    
    def _preventive_measures(self, data):
        """Tindakan pencegahan"""
        measures = []
        
        if data.get("early_detection"):
            measures.extend([
                "Pengawasan terhadap aktivitas mencurigakan",
                "Pemantauan komunikasi elektronik",
                "Koordinasi dengan komunitas"
            ])
            
        if data.get("travel_monitoring"):
            measures.append("Pemantauan perjalanan ke zona konflik")
            
        if data.get("financial_monitoring"):
            measures.append("Pemantauan transaksi keuangan mencurigakan")
            
        return measures
    
    def _investigation_powers(self, data):
        """Wewenang penyidikan khusus"""
        powers = [
            "Penahanan 7 hari + perpanjangan 180 hari",
            "Penyadapan komunikasi",
            "Akses data elektronik",
            "Kerjasama intelijen internasional"
        ]
        
        if data.get("urgent_prevention"):
            powers.append("Tindakan pencegahan darurat")
            
        return powers
    
    def _calculate_terrorism_sanctions(self, data):
        """Hitung sanksi terorisme"""
        sanctions = []
        
        if data.get("pelaksanaan_terorisme"):
            sanctions.extend([
                "Pidana mati",
                "Pidana penjara seumur hidup", 
                "Pidana penjara 4-20 tahun"
            ])
            
        if data.get("perencanaan_terorisme"):
            sanctions.append("Pidana penjara 3-12 tahun")
            
        if data.get("pendanaan_terorisme"):
            sanctions.extend([
                "Pidana penjara 3-15 tahun",
                "Denda Rp 500 juta - 1 Miliar"
            ])
            
        return sanctions
    
    def _deradicalization_eligibility(self, data):
        """Cek kelayakan program deradikalisasi"""
        return any([
            data.get("first_time_offender"),
            data.get("cooperated_with_authorities"),
            data.get("showed_remorse"),
            data.get("willing_to_reintegrate")
        ])
    
    def analyze_counter_terrorism_operations(self, operation_data):
        """Analisis operasi kontra-terorisme"""
        analysis = {
            "operation_legality": True,
            "human_rights_considerations": [],
            "intelligence_coordination": [],
            "international_cooperation": [],
            "post_operation_measures": []
        }
        
        # Legalitas operasi
        analysis["operation_legality"] = self._operation_legality_check(operation_data)
        
        # Pertimbangan HAM
        analysis["human_rights_considerations"] = self._human_rights_analysis(operation_data)
        
        # Koordinasi intelijen
        analysis["intelligence_coordination"] = self._intelligence_coordination(operation_data)
        
        # Kerjasama internasional
        analysis["international_cooperation"] = self._international_counter_terrorism(operation_data)
        
        # Tindakan pasca operasi
        analysis["post_operation_measures"] = self._post_operation_measures(operation_data)
        
        return analysis
    
    def _operation_legality_check(self, data):
        """Cek legalitas operasi kontra-terorisme"""
        return all([
            data.get("based_on_intelligence"),
            data.get("proper_authorization"),
            data.get("proportional_force"),
            not data.get("indiscriminate_targeting")
        ])
    
    def _human_rights_analysis(self, data):
        """Analisis aspek HAM"""
        considerations = [
            "Prinsip proportionality dan distinction",
            "Perlindungan penduduk sipil",
            "Penanganan tahanan sesuai standar HAM"
        ]
        
        if data.get("civilian_casualties"):
            considerations.append("Investigasi korban sipil")
            
        return considerations
    
    def _intelligence_coordination(self, data):
        """Koordinasi intelijen"""
        coordination = [
            "BNPT (Badan Nasional Penanggulangan Terorisme)",
            "Densus 88 Anti Teror",
            "BIN (Badan Intelijen Negara)",
            "Polri"
        ]
        
        return coordination
    
    def _international_counter_terrorism(self, data):
        """Kerjasama kontra-terorisme internasional"""
        cooperation = []
        
        if data.get("cross_border_threat"):
            cooperation.extend([
                "Interpol notification",
                "ASEANAPOL coordination",
                "Bilateral intelligence sharing"
            ])
            
        if data.get("foreign_fighters"):
            cooperation.append("Foreign Terrorist Fighter tracking")
            
        return cooperation
    
    def _post_operation_measures(self, data):
        """Tindakan pasca operasi"""
        measures = [
            "Forensic investigation",
            "Intelligence debriefing",
            "Community engagement",
            "Psychological support for affected communities"
        ]
        
        return measures
    
    def analyze_cyber_terrorism(self, cyber_data):
        """Analisis terorisme siber"""
        analysis = {
            "cyber_terrorism_detected": False,
            "cyber_threats": [],
            "critical_infrastructure_risk": [],
            "prevention_measures": [],
            "incident_response": []
        }
        
        # Deteksi terorisme siber
        if cyber_data.get("cyber_attacks"):
            analysis["cyber_terrorism_detected"] = True
            analysis["cyber_threats"] = self._identify_cyber_threats(cyber_data)
        
        # Risiko infrastruktur kritis
        analysis["critical_infrastructure_risk"] = self._critical_infrastructure_analysis(cyber_data)
        
        # Tindakan pencegahan
        analysis["prevention_measures"] = self._cyber_prevention_measures(cyber_data)
        
        # Respons insiden
        analysis["incident_response"] = self._cyber_incident_response(cyber_data)
        
        return analysis
    
    def _identify_cyber_threats(self, data):
        """Identifikasi ancaman siber"""
        threats = []
        
        if data.get("hacking_critical_infrastructure"):
            threats.append("Peretasan infrastruktur kritis")
            
        if data.get("disinformation_campaigns"):
            threats.append("Kampanye disinformasi dan propaganda")
            
        if data.get("radicalization_online"):
            threats.append("Rekrutmen dan radikalisasi online")
            
        if data.get("cyber_financing"):
            threats.append("Pendanaan terorisme melalui cryptocurrency")
            
        return threats
    
    def _critical_infrastructure_analysis(self, data):
        """Analisis risiko infrastruktur kritis"""
        critical_sectors = [
            "energy_sector",
            "financial_system", 
            "transportation",
            "healthcare",
            "government_services"
        ]
        
        at_risk = []
        for sector in critical_sectors:
            if data.get(sector + "_targeted"):
                at_risk.append(sector.replace("_", " ").title())
                
        return at_risk
    
    def _cyber_prevention_measures(self, data):
        """Tindakan pencegahan siber"""
        measures = [
            "Cyber security assessment for critical infrastructure",
            "Monitoring of extremist online activities",
            "Public-private partnership for cyber defense"
        ]
        
        return measures
    
    def _cyber_incident_response(self, data):
        """Respons insiden siber"""
        response = [
            "Immediate containment of cyber attack",
            "Forensic analysis of attack vectors",
            "Coordination with BSSN (Badan Siber dan Sandi Negara)",
            "Public communication strategy"
        ]
        
        return response
    
    def generate_counter_terrorism_strategy(self, threat_analysis):
        """Generate strategi kontra-terorisme"""
        return {
            "prevention_strategy": [
                "Community policing and engagement",
                "Counter-narrative campaigns",
                "Early detection of radicalization"
            ],
            "enforcement_strategy": [
                "Intelligence-led operations",
                "Financial tracking of terrorist networks",
                "Border control enhancement"
            ],
            "rehabilitation_strategy": [
                "Deradicalization programs for offenders",
                "Social reintegration support",
                "Psychological counseling"
            ],
            "international_cooperation": [
                "Information sharing with partner countries",
                "Joint training exercises",
                "Legal assistance in investigations"
            ]
        }
