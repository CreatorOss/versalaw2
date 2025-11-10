# versalaw2/indonesian_law/professional_ethics/legal_ethics.py
"""
Legal Professions Ethics Analysis Module
Analisis Kode Etik untuk Jaksa, Hakim, Pengacara, Notaris
"""

class LegalEthicsAnalyzer:
    """Analyzer for legal professions ethics compliance"""
    
    def __init__(self):
        self.ethics_codes = self._load_ethics_codes()
        self.common_violations = self._load_common_violations()
    
    def analyze_conduct(self, text, profession=None):
        """Analyze professional conduct against ethics codes"""
        analysis = {
            "ethics_compliance": [],
            "potential_violations": [],
            "conflict_of_interest": [],
            "confidentiality_issues": [],
            "professional_standards": []
        }
        
        # Profession-specific ethics analysis
        if profession and profession in self.ethics_codes:
            ethics_code = self.ethics_codes[profession]
            
            # Check confidentiality
            confidentiality_issues = self._check_confidentiality(text, ethics_code)
            analysis["confidentiality_issues"] = confidentiality_issues
            
            # Check conflict of interest
            conflict_issues = self._check_conflict_of_interest(text, ethics_code)
            analysis["conflict_of_interest"] = conflict_issues
            
            # Check professional standards
            standards_issues = self._check_professional_standards(text, ethics_code)
            analysis["professional_standards"] = standards_issues
        
        # General ethics compliance
        general_issues = self._check_general_ethics(text)
        analysis["ethics_compliance"] = general_issues
        
        return analysis
    
    def _check_confidentiality(self, text, ethics_code):
        """Check confidentiality compliance"""
        issues = []
        text_lower = text.lower()
        
        confidentiality_keywords = [
            "rahasia", "konfidensial", "tidak boleh diungkapkan",
            "kerahasiaan", "client confidentiality", "dokumen rahasia"
        ]
        
        for keyword in confidentiality_keywords:
            if keyword in text_lower:
                issues.append({
                    "issue": "Potential confidentiality concern",
                    "keyword": keyword,
                    "ethics_article": ethics_code.get("confidentiality", "Relevant article"),
                    "severity": "high"
                })
        
        return issues
    
    def _check_conflict_of_interest(self, text, ethics_code):
        """Check for conflict of interest"""
        issues = []
        text_lower = text.lower()
        
        conflict_keywords = [
            "benturan kepentingan", "conflict of interest",
            "mewakili kedua belah pihak", "kepentingan pribadi",
            "hubungan keluarga", "kepentingan finansial"
        ]
        
        for keyword in conflict_keywords:
            if keyword in text_lower:
                issues.append({
                    "issue": "Potential conflict of interest",
                    "keyword": keyword,
                    "ethics_article": ethics_code.get("conflict_of_interest", "Relevant article"),
                    "severity": "high"
                })
        
        return issues
    
    def _check_professional_standards(self, text, ethics_code):
        """Check professional standards compliance"""
        issues = []
        text_lower = text.lower()
        
        standards_keywords = {
            "imparsialitas": "Prinsip imparsialitas",
            "independen": "Prinsip independensi",
            "integritas": "Prinsip integritas",
            "kompetensi": "Standar kompetensi profesional",
            "kejujuran": "Prinsip kejujuran"
        }
        
        for keyword, standard in standards_keywords.items():
            if keyword in text_lower:
                issues.append({
                    "standard": standard,
                    "keyword": keyword,
                    "compliance": "referenced",
                    "importance": "high"
                })
        
        return issues
    
    def _check_general_ethics(self, text):
        """Check general ethics compliance"""
        issues = []
        text_lower = text.lower()
        
        general_ethics = {
            "suap": "Pelanggaran etik - suap",
            "gratifikasi": "Pelanggaran etik - gratifikasi",
            "pemerasan": "Pelanggaran etik - pemerasan",
            "penggelapan": "Pelanggaran etik - penggelapan"
        }
        
        for violation, description in general_ethics.items():
            if violation in text_lower:
                issues.append({
                    "violation": violation,
                    "description": description,
                    "severity": "high",
                    "action": "immediate_review"
                })
        
        return issues
    
    def _load_ethics_codes(self):
        """Load ethics codes for legal professions"""
        return {
            "jaksa": {
                "confidentiality": "Pasal 5 Kode Etik Jaksa",
                "conflict_of_interest": "Pasal 9 Kode Etik Jaksa",
                "impartiality": "Pasal 7 Kode Etik Jaksa",
                "integrity": "Pasal 3 Kode Etik Jaksa"
            },
            "hakim": {
                "confidentiality": "Pasal 6 Kode Etik Hakim", 
                "conflict_of_interest": "Pasal 5 Kode Etik Hakim",
                "impartiality": "Pasal 4 Kode Etik Hakim",
                "independence": "Pasal 3 Kode Etik Hakim"
            },
            "pengacara": {
                "confidentiality": "Pasal 4 Kode Etik Advokat",
                "conflict_of_interest": "Pasal 8 Kode Etik Advokat", 
                "loyalty": "Pasal 6 Kode Etik Advokat",
                "professional_competence": "Pasal 11 Kode Etik Advokat"
            },
            "notaris": {
                "confidentiality": "Pasal 9 Kode Etik Notaris",
                "conflict_of_interest": "Pasal 6 Kode Etik Notaris",
                "neutrality": "Pasal 3 Kode Etik Notaris",
                "document_integrity": "Pasal 5 Kode Etik Notaris"
            }
        }
    
    def _load_common_violations(self):
        """Load common ethics violations patterns"""
        return {
            "jaksa": [
                "pembocoran berkas perkara",
                "penerimaan hadiah dari pihak berperkara", 
                "tekanan tidak profesional dalam penyidikan"
            ],
            "hakim": [
                "intervensi eksternal dalam putusan",
                "diskriminasi dalam persidangan",
                "pelanggaran prosedur persidangan"
            ],
            "pengacara": [
                "mark up biaya perkara",
                "abandon client (meninggalkan klien)",
                "conflict of representation"
            ],
            "notaris": [
                "pembuatan akta palsu",
                "pelanggaran kerahasiaan akta",
                "konflik notaris dalam pembuatan akta"
            ]
        }
