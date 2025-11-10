#!/usr/bin/env python3
"""
VERSALAW2 Money Laundering Law Analyzer (TPPU)
Analisis tindak pidana pencucian uang - FIXED VERSION
"""

class MoneyLaunderingAnalyzer:
    def __init__(self):
        self.tppu_laws = {
            "uu_8_2010": "UU No. 8 Tahun 2010 tentang Tindak Pidana Pencucian Uang",
            "uu_9_2013": "UU No. 9 Tahun 2013 tentang Pencegahan dan Pemberantasan Tindak Pidana Pendanaan Terorisme"
        }
        
        self.money_laundering_stages = [
            "placement",
            "layering", 
            "integration"
        ]
        
        self.predicate_crimes = [
            "korupsi",
            "narkotika",
            "terorisme",
            "penipuan",
            "perdagangan_orang",
            "perdagangan_narkotika",
            "penyelundupan",
            "penyuapan"
        ]
    
    def analyze_money_laundering(self, financial_data):
        """Analisis pola pencucian uang - IMPROVED"""
        analysis = {
            "tppu_detected": False,
            "money_laundering_stages": [],
            "predicate_crime": None,
            "suspicious_transactions": [],
            "ppatk_reporting": [],
            "asset_forfeiture": False,
            "legal_articles": [],
            "risk_level": "low",
            "indicators_found": []
        }
        
        # Deteksi tahapan pencucian uang - FIXED LOGIC
        detected_stages = []
        for stage in self.money_laundering_stages:
            if financial_data.get(stage):
                detected_stages.append(stage)
                analysis["tppu_detected"] = True
        
        analysis["money_laundering_stages"] = detected_stages
        
        # Identifikasi predicate crime - IMPROVED
        analysis["predicate_crime"] = self._identify_predicate_crime(financial_data)
        
        # Analisis transaksi mencurigakan - ENHANCED
        analysis["suspicious_transactions"] = self._analyze_suspicious_transactions(financial_data)
        
        # Kewajiban pelaporan PPATK
        analysis["ppatk_reporting"] = self._ppatk_reporting_requirements(financial_data)
        
        # Aset yang dapat disita
        analysis["asset_forfeiture"] = self._asset_forfeiture_analysis(financial_data)
        
        # Pasal yang dilanggar
        analysis["legal_articles"] = self._identify_tppu_articles(financial_data)
        
        # Level risiko
        analysis["risk_level"] = self._calculate_risk_level(analysis)
        
        # Indicators found
        analysis["indicators_found"] = self._get_ml_indicators(financial_data)
        
        return analysis
    
    def _identify_predicate_crime(self, data):
        """Identifikasi kejahatan asal (predicate crime) - IMPROVED"""
        for crime in self.predicate_crimes:
            if data.get(crime):
                return crime
        
        # Check for transaction patterns that indicate specific crimes
        if data.get("drug_related_patterns"):
            return "narkotika"
        elif data.get("terrorism_financing_indicators"):
            return "terorisme"
        elif data.get("corruption_indicators"):
            return "korupsi"
            
        return "unknown"
    
    def _analyze_suspicious_transactions(self, data):
        """Analisis transaksi mencurigakan - IMPROVED"""
        suspicious = []
        
        # Handle both list and single transaction
        transactions = data.get("transactions", [])
        if not isinstance(transactions, list):
            transactions = [transactions] if transactions else []
        
        for transaction in transactions:
            if self._is_suspicious_transaction(transaction):
                suspicious.append({
                    "amount": transaction.get("amount", 0),
                    "pattern": transaction.get("pattern", "unknown"),
                    "reason": self._get_suspicion_reason(transaction),
                    "risk_level": self._get_transaction_risk(transaction)
                })
                
        # Also check direct suspicious indicators
        if data.get("large_cash_transactions") and not suspicious:
            suspicious.append({
                "amount": data.get("large_cash_amount", 0),
                "pattern": "large_cash",
                "reason": "Transaksi tunai besar tanpa basis ekonomi jelas",
                "risk_level": "high"
            })
                
        return suspicious
    
    def _is_suspicious_transaction(self, transaction):
        """Cek apakah transaksi mencurigakan - IMPROVED"""
        if not transaction:
            return False
            
        amount = transaction.get("amount", 0)
        patterns = transaction.get("patterns", [])
        
        # Threshold berdasarkan PERPPATK - lebih realistic
        if amount > 500000000:  # 500 juta
            return True
            
        suspicious_patterns = [
            "structuring", "rapid_movement", "offshore_flow", 
            "round_dollar", "multiple_accounts", "shell_company"
        ]
        
        if any(pattern in patterns for pattern in suspicious_patterns):
            return True
            
        # Additional checks
        if transaction.get("unusual_frequency"):
            return True
        if transaction.get("inconsistent_with_business"):
            return True
            
        return False
    
    def _get_suspicion_reason(self, transaction):
        """Dapatkan alasan kecurigaan"""
        amount = transaction.get("amount", 0)
        
        if amount > 500000000:
            return "Nilai transaksi melebihi batas wajar"
        elif "structuring" in transaction.get("patterns", []):
            return "Structuring untuk menghindari pelaporan"
        elif "offshore_flow" in transaction.get("patterns", []):
            return "Aliran dana ke yurisdiksi rahasia"
        else:
            return "Pola transaksi tidak biasa"
    
    def _get_transaction_risk(self, transaction):
        """Tentukan level risiko transaksi"""
        amount = transaction.get("amount", 0)
        
        if amount > 1000000000:  # 1 Miliar
            return "high"
        elif amount > 500000000:  # 500 Juta
            return "medium"
        else:
            return "low"
    
    def _ppatk_reporting_requirements(self, data):
        """Analisis kewajiban pelaporan PPATK - EXPANDED"""
        reporting_obligations = []
        
        if data.get("financial_institution"):
            reporting_obligations.extend([
                "Laporan Transaksi Keuangan Mencurigakan (LTKM)",
                "Laporan Transaksi Tunai (LTT) ≥ Rp 500 juta",
                "Laporan Transfer Dana (LTD) ≥ Rp 500 juta"
            ])
        
        if data.get("designated_non_financial_business"):
            reporting_obligations.extend([
                "Laporan Transaksi Tunai ≥ Rp 500 juta",
                "Laporan Transaksi Mencurigakan"
            ])
            
        return reporting_obligations
    
    def _asset_forfeiture_analysis(self, data):
        """Analisis kemungkinan perampasan aset - IMPROVED"""
        return any([
            data.get("assets_from_crime", False),
            data.get("commingled_assets", False),
            data.get("substitute_assets", False),
            data.get("instrumentalities", False),
            len(self._analyze_suspicious_transactions(data)) > 0
        ])
    
    def _identify_tppu_articles(self, data):
        """Identifikasi pasal UU TPPU yang dilanggar - EXPANDED"""
        articles = []
        
        # Check for specific money laundering activities
        if data.get("placement") or data.get("placement_activity"):
            articles.append("Pasal 3 ayat (1) UU 8/2010 - Placement")
            
        if data.get("layering") or data.get("layering_activity"):
            articles.append("Pasal 4 UU 8/2010 - Layering")
            
        if data.get("integration") or data.get("integration_activity"):
            articles.append("Pasal 5 UU 8/2010 - Integration")
        
        # Additional articles based on indicators
        if len(self._analyze_suspicious_transactions(data)) > 0:
            articles.append("Pasal 26 UU 8/2010 - Kegiatan Transaksi Keuangan Mencurigakan")
            
        if data.get("failure_to_report"):
            articles.append("Pasal 27 UU 8/2010 - Tidak menyampaikan laporan")
            
        return articles
    
    def _calculate_risk_level(self, analysis):
        """Hitung level risiko money laundering"""
        risk_score = 0
        
        # Stage-based risk
        risk_score += len(analysis["money_laundering_stages"]) * 2
        
        # Transaction risk
        for transaction in analysis["suspicious_transactions"]:
            if transaction["risk_level"] == "high":
                risk_score += 3
            elif transaction["risk_level"] == "medium":
                risk_score += 2
            else:
                risk_score += 1
        
        # Predicate crime risk
        if analysis["predicate_crime"] in ["narkotika", "terorisme"]:
            risk_score += 3
        elif analysis["predicate_crime"] in ["korupsi", "perdagangan_orang"]:
            risk_score += 2
        
        if risk_score >= 5:
            return "high"
        elif risk_score >= 3:
            return "medium"
        else:
            return "low"
    
    def _get_ml_indicators(self, data):
        """Dapatkan indikator money laundering yang terdeteksi"""
        indicators = []
        
        ml_indicators = {
            "structuring": "Structuring transactions",
            "rapid_movement": "Rapid movement of funds",
            "offshore_accounts": "Use of offshore accounts",
            "shell_companies": "Involvement of shell companies",
            "cash_intensive": "Cash-intensive business without justification",
            "third_party": "Third-party transactions without economic purpose"
        }
        
        for indicator, description in ml_indicators.items():
            if data.get(indicator):
                indicators.append(description)
                
        return indicators
    
    def analyze_ftf_regulations(self, data):
        """Analisis Funds Transfer Regulation (PP No. 43/2015)"""
        return {
            "threshold_reporting": "Transfer ≥ Rp 100.000.000",
            "information_required": [
                "Nama dan alamat pengirim",
                "Nama dan alamat penerima", 
                "Nomor rekening/identitas",
                "Jumlah dan mata uang transfer"
            ],
            "obliged_businesses": [
                "Bank",
                "Perusahaan Finansial", 
                "Penyedia Jasa Keuangan Lainnya",
                "Penyelenggara E-money"
            ],
            "sanctions": [
                "Sanksi administratif - denda hingga Rp 1 miliar",
                "Sanksi pidana - penjara hingga 5 tahun"
            ]
        }
    
    def generate_sar_report(self, analysis):
        """Generate Suspicious Activity Report template"""
        return {
            "report_type": "Suspicious Activity Report (SAR)",
            "reporting_entity": "Financial Institution/Designated Business",
            "subject_information": {
                "name": "To be filled",
                "identification": "To be filled",
                "account_numbers": "To be filled"
            },
            "suspicious_activities": analysis["suspicious_transactions"],
            "ml_indicators": analysis["indicators_found"],
            "recommended_actions": [
                "Enhanced Due Diligence",
                "Transaction Monitoring",
                "Possible Account Freeze",
                "Reporting to PPATK"
            ]
        }
