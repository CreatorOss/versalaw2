# versalaw2/indonesian_law/criminal_justice/police_regulations.py
"""
Police Regulations Analysis Module
Analisis berdasarkan PERKAP dan prosedur kepolisian
"""

class PoliceRegulationsAnalyzer:
    """Analyzer for police regulations and procedures"""
    
    def __init__(self):
        self.perkap_database = self._load_perkap_database()
        self.investigation_procedures = self._load_investigation_procedures()
    
    def analyze_procedures(self, text, context=None):
        """Analyze police procedures compliance"""
        analysis = {
            "perkap_compliance": [],
            "investigation_issues": [],
            "human_rights_compliance": [],
            "procedure_violations": []
        }
        
        # Check PERKAP compliance
        perkap_issues = self._check_perkap_compliance(text)
        analysis["perkap_compliance"].extend(perkap_issues)
        
        # Check investigation procedures
        investigation_issues = self._check_investigation_procedures(text)
        analysis["investigation_issues"].extend(investigation_issues)
        
        # Check human rights compliance
        human_rights_issues = self._check_human_rights_compliance(text)
        analysis["human_rights_compliance"].extend(human_rights_issues)
        
        return analysis
    
    def _check_perkap_compliance(self, text):
        """Check compliance with PERKAP"""
        issues = []
        text_lower = text.lower()
        
        perkap_keywords = {
            "penyidikan": "PERKAP No. 14 Tahun 2011 - Management Penyidikan",
            "penyidik": "PERKAP No. 14 Tahun 2011 - Management Penyidikan",
            "berita acara": "PERKAP No. 14 Tahun 2011 - Berita Acara",
            "sppd": "PERKAP No. 10 Tahun 2010 - SPPD dan Penugasan",
            "surat perintah": "PERKAP No. 10 Tahun 2010 - Surat Perintah",
            "penangkapan": "PERKAP No. 1 Tahun 2009 - Penggunaan Kekuatan"
        }
        
        for keyword, regulation in perkap_keywords.items():
            if keyword in text_lower:
                issues.append({
                    "keyword": keyword,
                    "regulation": regulation,
                    "compliance_check": "referenced",
                    "type": "perkap_reference"
                })
        
        return issues
    
    def _check_investigation_procedures(self, text):
        """Check investigation procedure compliance"""
        issues = []
        text_lower = text.lower()
        
        procedure_requirements = {
            "surat perintah": ["penangkapan", "penggeledahan", "penyitaan"],
            "berita acara": ["pemeriksaan", "penyitaan", "penangkapan"],
            "saksi": ["pemeriksaan", "keterangan"],
            "tersangka": ["hak", "pemeriksaan", "pendampingan"]
        }
        
        for requirement, contexts in procedure_requirements.items():
            if requirement in text_lower:
                for context in contexts:
                    if context in text_lower:
                        issues.append({
                            "procedure": requirement,
                            "context": context,
                            "check": "procedure_referenced",
                            "importance": "high"
                        })
        
        return issues
    
    def _check_human_rights_compliance(self, text):
        """Check human rights compliance in police procedures"""
        violations = []
        text_lower = text.lower()
        
        human_rights_issues = {
            "penyiksaan": "Melanggar prinsip non-derogable rights",
            "penghilangan paksa": "Melanggar hak untuk tidak dihilangkan paksa",
            "diskriminasi": "Melanggar prinsip equality before the law",
            "peradilan ekstra yudisial": "Melanggar due process of law"
        }
        
        for issue, description in human_rights_issues.items():
            if issue in text_lower:
                violations.append({
                    "issue": issue,
                    "description": description,
                    "severity": "high",
                    "rights_violation": True
                })
        
        return violations
    
    def _load_perkap_database(self):
        """Load PERKAP database"""
        return {
            "PERKAP_14_2011": "Management Penyidikan",
            "PERKAP_10_2010": "SPPD dan Penugasan",
            "PERKAP_1_2009": "Penggunaan Kekuatan dalam Tindakan Kepolisian",
            "PERKAP_12_2009": "Pemolisian Masyarakat",
            "PERKAP_7_2017": "Penanganan Tindak Pidana Siber"
        }
    
    def _load_investigation_procedures(self):
        """Load investigation procedures"""
        return {
            "arrest_procedures": [
                "surat perintah penangkapan",
                "penjelasan hak tersangka", 
                "pemberitahuan keluarga"
            ],
            "search_procedures": [
                "surat izin penggeledahan",
                "berita acara penggeledahan",
                "saksi penggeledahan"
            ],
            "interrogation_procedures": [
                "hak didampingi pengacara",
                "pencatatan pemeriksaan",
                "larangan penyiksaan"
            ]
        }
