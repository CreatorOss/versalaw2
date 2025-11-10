#!/usr/bin/env python3
"""
VERSALAW2 Cyber Crime Analyzer
Analisis hukum kejahatan siber dan UU ITE
"""

class CyberCrimeAnalyzer:
    def __init__(self):
        self.cyber_laws = {
            "uu_11_2008": "UU No. 11 Tahun 2008 tentang Informasi dan Transaksi Elektronik",
            "uu_19_2016": "UU No. 19 Tahun 2016 tentang Perubahan atas UU No. 11 Tahun 2008",
            "uu_27_2022": "UU No. 27 Tahun 2022 tentang Perlindungan Data Pribadi"
        }
        
        self.cyber_offenses = [
            "akses_ilegal",
            "intersepsi_ilegal",
            "gangguan_data",
            "gangguan_sistem",
            "penyalahgunaan_alat",
            "pemalsuan_dokumen_elektronik",
            "penipuan_daring",
            "konten_ilegal",
            "pencemaran_nama_baik",
            "peretasan",
            "phishing",
            "ransomware"
        ]
        
        self.data_violations = [
            "pemrosesan_tanpa_konsent",
            "pengumpulan_berlebihan",
            "keamanan_data_lemah",
            "transfer_lintas_batas_ilegal",
            "pelanggaran_data_pribadi"
        ]
    
    def analyze_cyber_crime(self, case_data):
        """Analisis kasus kejahatan siber"""
        analysis = {
            "cyber_crime_detected": False,
            "cyber_offenses": [],
            "data_violations": [],
            "legal_articles": [],
            "digital_evidence": [],
            "jurisdictional_issues": [],
            "sanctions": [],
            "data_protection_issues": [],
            "compliance_violations": []
        }
        
        # Deteksi kejahatan siber
        for offense in self.cyber_offenses:
            if case_data.get(offense):
                analysis["cyber_offenses"].append(offense)
                analysis["cyber_crime_detected"] = True
        
        # Deteksi pelanggaran data
        for violation in self.data_violations:
            if case_data.get(violation):
                analysis["data_violations"].append(violation)
        
        # Identifikasi pasal hukum
        analysis["legal_articles"] = self._identify_cyber_articles(case_data)
        
        # Analisis bukti digital
        analysis["digital_evidence"] = self._analyze_digital_evidence(case_data)
        
        # Masalah yurisdiksi
        analysis["jurisdictional_issues"] = self._jurisdictional_analysis(case_data)
        
        # Sanksi
        analysis["sanctions"] = self._calculate_cyber_sanctions(case_data)
        
        # Masalah perlindungan data
        analysis["data_protection_issues"] = self._data_protection_analysis(case_data)
        
        # Pelanggaran compliance
        analysis["compliance_violations"] = self._compliance_violations(case_data)
        
        return analysis
    
    def _identify_cyber_articles(self, data):
        """Identifikasi pasal UU ITE dan PDP"""
        articles = []
        
        if data.get("akses_ilegal"):
            articles.append("Pasal 30 UU 11/2008 - Akses tanpa hak")
            
        if data.get("peretasan"):
            articles.append("Pasal 30 ayat (3) UU 11/2008 - Peretasan sistem")
            
        if data.get("penipuan_daring"):
            articles.append("Pasal 28 ayat (1) UU 11/2008 - Penipuan elektronik")
            
        if data.get("pencemaran_nama_baik"):
            articles.append("Pasal 27 ayat (3) UU 11/2008 - Pencemaran nama baik")
            
        if data.get("konten_ilegal"):
            articles.append("Pasal 28 ayat (2) UU 11/2008 - Konten melanggar kesusilaan")
            
        if data.get("pelanggaran_data_pribadi"):
            articles.append("Pasal 57 UU 27/2022 - Pelanggaran data pribadi")
            
        return articles
    
    def _analyze_digital_evidence(self, data):
        """Analisis bukti digital"""
        evidence_analysis = []
        
        if data.get("log_files"):
            evidence_analysis.append("Log files - perlu analisis forensik")
            
        if data.get("network_traffic"):
            evidence_analysis.append("Network traffic capture")
            
        if data.get("malware_analysis"):
            evidence_analysis.append("Malware specimen analysis")
            
        if data.get("social_media_evidence"):
            evidence_analysis.append("Social media posts and messages")
            
        if data.get("encryption_issues"):
            evidence_analysis.append("Encrypted data - perlu decryption")
            
        return evidence_analysis
    
    def _jurisdictional_analysis(self, data):
        """Analisis masalah yurisdiksi"""
        jurisdictional_issues = []
        
        if data.get("cross_border_attack"):
            jurisdictional_issues.extend([
                "Serangan lintas batas negara",
                "Kerjasama internasional diperlukan",
                "Mutual Legal Assistance Treaty"
            ])
            
        if data.get("server_overseas"):
            jurisdictional_issues.append("Server berada di luar yurisdiksi Indonesia")
            
        if data.get("foreign_perpetrator"):
            jurisdictional_issues.append("Pelaku berada di luar negeri")
            
        return jurisdictional_issues
    
    def _calculate_cyber_sanctions(self, data):
        """Hitung sanksi kejahatan siber"""
        sanctions = []
        
        if data.get("akses_ilegal"):
            sanctions.extend([
                "Pidana penjara maksimal 8 tahun",
                "Denda maksimal Rp 2.000.000.000"
            ])
            
        if data.get("pencemaran_nama_baik"):
            sanctions.extend([
                "Pidana penjara maksimal 4 tahun", 
                "Denda maksimal Rp 750.000.000"
            ])
            
        if data.get("pelanggaran_data_pribadi"):
            sanctions.extend([
                "Pidana penjara maksimal 6 tahun",
                "Denda maksimal Rp 6.000.000.000"
            ])
            
        if data.get("penipuan_daring"):
            sanctions.extend([
                "Pidana penjara maksimal 10 tahun",
                "Denda maksimal Rp 10.000.000.000"
            ])
            
        return sanctions
    
    def _data_protection_analysis(self, data):
        """Analisis masalah perlindungan data"""
        issues = []
        
        if data.get("data_breach"):
            issues.extend([
                "Kewajiban notifikasi breach dalam 3x24 jam",
                "Kewajiban melaporkan ke otoritas",
                "Kewajiban memberitahu subjek data"
            ])
            
        if data.get("consent_violation"):
            issues.append("Pemrosesan data tanpa persetujuan")
            
        if data.get("purpose_limitation_violation"):
            issues.append("Pemrosesan di luar tujuan yang ditetapkan")
            
        return issues
    
    def _compliance_violations(self, data):
        """Identifikasi pelanggaran compliance"""
        violations = []
        
        if not data.get("privacy_policy"):
            violations.append("Tidak memiliki kebijakan privasi")
            
        if not data.get("data_protection_officer"):
            violations.append("Tidak menunjuk Data Protection Officer")
            
        if not data.get("data_breach_protocol"):
            violations.append("Tidak memiliki protokol penanganan data breach")
            
        if not data.get("consent_mechanism"):
            violations.append("Tidak memiliki mekanisme persetujuan yang jelas")
            
        return violations
    
    def analyze_incident_response(self, incident_data):
        """Analisis respons insiden siber"""
        analysis = {
            "incident_severity": "low",
            "response_timeline": [],
            "containment_measures": [],
            "eradication_steps": [],
            "recovery_actions": [],
            "legal_obligations": [],
            "notification_requirements": []
        }
        
        # Severity assessment
        severity_factors = {
            "data_breach_scale": incident_data.get("affected_records", 0),
            "sensitive_data_exposed": incident_data.get("sensitive_data", False),
            "system_downtime": incident_data.get("downtime_hours", 0),
            "financial_impact": incident_data.get("financial_loss", 0)
        }
        
        severity_score = 0
        if severity_factors["data_breach_scale"] > 1000:
            severity_score += 2
        if severity_factors["sensitive_data_exposed"]:
            severity_score += 3
        if severity_factors["system_downtime"] > 24:
            severity_score += 2
        if severity_factors["financial_impact"] > 1000000000:
            severity_score += 2
            
        if severity_score >= 5:
            analysis["incident_severity"] = "high"
        elif severity_score >= 3:
            analysis["incident_severity"] = "medium"
        else:
            analysis["incident_severity"] = "low"
        
        # Response timeline
        analysis["response_timeline"] = [
            "Immediate containment",
            "Forensic analysis",
            "Eradication of threat",
            "System recovery",
            "Post-incident review"
        ]
        
        # Legal obligations
        if incident_data.get("data_breach"):
            analysis["legal_obligations"].extend([
                "Notifikasi kepada otoritas dalam 3x24 jam",
                "Pemberitahuan kepada subjek data",
                "Dokumentasi insiden untuk 3 tahun"
            ])
        
        # Notification requirements
        if analysis["incident_severity"] == "high":
            analysis["notification_requirements"].extend([
                "BSSN (Badan Siber dan Sandi Negara)",
                "Otoritas Perlindungan Data Pribadi",
                "Pihak berwenang terkait"
            ])
        
        return analysis
