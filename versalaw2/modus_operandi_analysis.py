def build_modus_operandi_database(self) -> Dict:
    """Build MO database dari study cases"""
    mo_db = {
        'financial_crimes': {
            'markup_fiktif': {
                'description': 'Markup harga dalam pengadaan',
                'indicators': ['harga tidak wajar', 'vendor terkait pejabat', 'tender tertutup'],
                'prevention': ['audit reguler', 'transparansi pengadaan', 'whistleblower protection']
            },
            'pencucian_uang_tahapan': {
                'description': 'Money laundering melalui multiple stages',
                'indicators': ['transaksi kompleks', 'multiple accounts', 'cash intensive business'],
                'prevention': ['STR monitoring', 'KYB verification', 'transaction pattern analysis']
            }
        },
        'cyber_crimes': {
            'bci_consent_manipulation': {
                'description': 'Manipulasi consent dalam neural contracts',
                'indicators': ['vague consent clauses', 'data usage ambiguity', 'asymmetric rights'],
                'prevention': ['enhanced consent protocols', 'neural data protection', 'regulatory oversight']
            }
        }
    }
    return mo_db

def identify_modus_operandi(self, crime_evidence: List[str]) -> List[Dict]:
    """Identify modus operandi dari evidence"""
    matched_mo = []
    
    for crime_category, mo_patterns in self.modus_operandi_db.items():
        for mo_name, mo_data in mo_patterns.items():
            match_score = self.calculate_mo_match_score(crime_evidence, mo_data['indicators'])
            if match_score > 0.7:
                matched_mo.append({
                    'modus_operandi': mo_name,
                    'category': crime_category,
                    'description': mo_data['description'],
                    'match_score': match_score,
                    'investigation_priority': 'high' if match_score > 0.8 else 'medium'
                })
    
    return sorted(matched_mo, key=lambda x: x['match_score'], reverse=True)
