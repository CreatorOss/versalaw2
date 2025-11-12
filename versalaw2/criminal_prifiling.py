def analyze_criminal_profiles(self) -> Dict:
    """Build criminal profiles dari case data"""
    profiles = {
        'white_collar_criminal': {
            'characteristics': ['educated', 'position of trust', 'financial motive'],
            'behavioral_patterns': ['gradual escalation', 'cover-up attempts', 'lifestyle inflation'],
            'common_crimes': ['korupsi', 'pencucian uang', 'penipuan']
        },
        'cyber_criminal': {
            'characteristics': ['tech-savvy', 'anonymous', 'international connections'],
            'behavioral_patterns': ['multiple identities', 'digital footprints', 'rapid adaptation'],
            'common_crimes': ['ghost contracts', 'data theft', 'digital fraud']
        },
        'violent_offender': {
            'characteristics': ['history of violence', 'impulse control issues', 'substance abuse'],
            'behavioral_patterns': ['escalating violence', 'specific victim selection', 'weapon use'],
            'common_crimes': ['pembunuhan', 'penganiayaan', 'penculikan']
        }
    }
    return profiles

def predict_perpetrator_profile(self, crime_data: Dict) -> Dict:
    """Predict perpetrator profile berdasarkan crime scene data"""
    crime_type = crime_data.get('crime_type', '').lower()
    evidence = crime_data.get('evidence', [])
    modus_operandi = crime_data.get('modus_operandi', '')
    
    profile_matches = []
    
    for profile_name, profile_data in self.criminal_profiles.items():
        score = self.calculate_profile_match_score(
            crime_type, evidence, modus_operandi, profile_data
        )
        if score > 0.6:  # Minimum confidence threshold
            profile_matches.append({
                'profile_type': profile_name,
                'characteristics': profile_data['characteristics'],
                'confidence': score,
                'investigation_recommendations': self.get_investigation_tips(profile_name)
            })
    
    return {
        'crime_data': crime_data,
        'profile_matches': sorted(profile_matches, key=lambda x: x['confidence'], reverse=True),
        'primary_suspect_profile': profile_matches[0] if profile_matches else None
    }
