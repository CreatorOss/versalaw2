#!/usr/bin/env python3
"""
Individual Module Tests from Root
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_specific_module(module_path, class_name):
    """Test specific module"""
    try:
        # Import the specific class
        exec(f"from {module_path} import {class_name}")
        analyzer = eval(f"{class_name}()")
        
        # Simple test
        if hasattr(analyzer, 'analyze_compliance'):
            result = analyzer.analyze_compliance("test")
        elif hasattr(analyzer, 'analyze_procedures'):
            result = analyzer.analyze_procedures("test")
        elif hasattr(analyzer, 'analyze_conduct'):
            result = analyzer.analyze_conduct("test")
        elif hasattr(analyzer, 'analyze_civil_issues'):
            result = analyzer.analyze_civil_issues("test")
        else:
            result = {"status": "no_analysis_method"}
        
        print(f"✅ {class_name}: SUCCESS")
        return True
        
    except Exception as e:
        print(f"❌ {class_name}: {e}")
        return False

# Test semua modules
modules = [
    ("versalaw2.indonesian_law.hierarchy.constitutional_law", "ConstitutionalLawAnalyzer"),
    ("versalaw2.indonesian_law.hierarchy.statutory_law", "StatutoryLawAnalyzer"),
    ("versalaw2.indonesian_law.criminal_justice.police_regulations", "PoliceRegulationsAnalyzer"),
    ("versalaw2.indonesian_law.professional_ethics.legal_ethics", "LegalEthicsAnalyzer"),
    ("versalaw2.indonesian_law.specialized_law.civil_law", "CivilLawAnalyzer"),
    ("versalaw2.indonesian_law", "IndonesianLawAnalyzer"),
]

print("🧪 INDIVIDUAL MODULE TESTS")
print("=" * 50)

passed = 0
for module_path, class_name in modules:
    if test_specific_module(module_path, class_name):
        passed += 1

print(f"\n📊 RESULTS: {passed}/{len(modules)} modules working")
