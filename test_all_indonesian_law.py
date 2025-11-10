#!/usr/bin/env python3
"""
Comprehensive Test - All Indonesian Law Modules from Root
"""
import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_module(module_name, import_path, test_function=None):
    """Test individual module"""
    print(f"\n🧪 TESTING: {module_name}")
    print("-" * 40)
    
    try:
        # Dynamic import
        module = __import__(import_path, fromlist=[''])
        print(f"✅ {module_name} - IMPORT SUCCESS")
        
        if test_function:
            test_function(module)
            
        return True
        
    except Exception as e:
        print(f"❌ {module_name} - IMPORT FAILED: {e}")
        return False

def test_constitutional_law():
    """Test Constitutional Law Module"""
    from versalaw2.indonesian_law.hierarchy.constitutional_law import ConstitutionalLawAnalyzer
    
    analyzer = ConstitutionalLawAnalyzer()
    test_text = "Pembatasan kebebasan berpendapat warga"
    result = analyzer.analyze_compliance(test_text)
    
    print(f"   Rights violations: {len(result.get('rights_violations', []))}")
    print(f"   Constitutional issues: {len(result.get('constitutional_issues', []))}")
    return True

def test_statutory_law():
    """Test Statutory Law Module"""
    from versalaw2.indonesian_law.hierarchy.statutory_law import StatutoryLawAnalyzer
    
    analyzer = StatutoryLawAnalyzer()
    test_text = "Perda ini menyimpangi UU No. 12 Tahun 2011"
    result = analyzer.analyze_compliance(test_text)
    
    print(f"   Hierarchy issues: {len(result.get('hierarchy_issues', []))}")
    print(f"   Statutory references: {len(result.get('statutory_references', []))}")
    return True

def test_police_regulations():
    """Test Police Regulations Module"""
    from versalaw2.indonesian_law.criminal_justice.police_regulations import PoliceRegulationsAnalyzer
    
    analyzer = PoliceRegulationsAnalyzer()
    test_text = "Penyidik membuat berita acara pemeriksaan"
    result = analyzer.analyze_procedures(test_text)
    
    print(f"   PERKAP references: {len(result.get('perkap_compliance', []))}")
    print(f"   Investigation issues: {len(result.get('investigation_issues', []))}")
    return True

def test_legal_ethics():
    """Test Legal Ethics Module"""
    from versalaw2.indonesian_law.professional_ethics.legal_ethics import LegalEthicsAnalyzer
    
    analyzer = LegalEthicsAnalyzer()
    test_text = "Pengacara menghindari benturan kepentingan"
    result = analyzer.analyze_conduct(test_text, "pengacara")
    
    print(f"   Conflict issues: {len(result.get('conflict_of_interest', []))}")
    print(f"   Confidentiality issues: {len(result.get('confidentiality_issues', []))}")
    return True

def test_civil_law():
    """Test Civil Law Module"""
    from versalaw2.indonesian_law.specialized_law.civil_law import CivilLawAnalyzer
    
    analyzer = CivilLawAnalyzer()
    test_text = "Perjanjian berdasarkan Pasal 1338 KUH Perdata"
    result = analyzer.analyze_civil_issues(test_text)
    
    print(f"   Civil code references: {len(result.get('civil_code_references', []))}")
    print(f"   Contract law issues: {len(result.get('contract_law_issues', []))}")
    return True

def test_integrated_analysis():
    """Test Integrated Indonesian Law Analysis"""
    from versalaw2.indonesian_law import IndonesianLawAnalyzer
    
    analyzer = IndonesianLawAnalyzer()
    test_text = """
    Peraturan daerah tentang ketertiban umum.
    Dilarang membatasi kebebasan berpendapat.
    Penyidikan dilakukan dengan berita acara.
    """
    
    result = analyzer.comprehensive_analysis(test_text)
    
    print(f"   Constitutional compliance: {result['compliance_summary']['constitutional_compliance']}")
    print(f"   Statutory compliance: {result['compliance_summary']['statutory_compliance']}")
    print(f"   Overall risk: {result['compliance_summary']['overall_risk']}")
    return True

def main():
    print("🇮🇩 COMPREHENSIVE INDO LAW MODULES TEST")
    print("=" * 60)
    
    modules_to_test = [
        ("Constitutional Law", test_constitutional_law),
        ("Statutory Law", test_statutory_law),
        ("Police Regulations", test_police_regulations),
        ("Legal Ethics", test_legal_ethics),
        ("Civil Law", test_civil_law),
        ("Integrated Analysis", test_integrated_analysis),
    ]
    
    passed = 0
    total = len(modules_to_test)
    
    for module_name, test_func in modules_to_test:
        try:
            success = test_func()
            if success:
                passed += 1
                print(f"✅ {module_name} - PASSED")
            else:
                print(f"❌ {module_name} - FAILED")
        except Exception as e:
            print(f"❌ {module_name} - ERROR: {e}")
    
    print("\n" + "=" * 60)
    print(f"📊 TEST RESULTS: {passed}/{total} modules passed")
    
    if passed == total:
        print("🎉 ALL INDONESIAN LAW MODULES WORKING PERFECTLY!")
    else:
        print(f"⚠️  {total - passed} modules need attention")
    
    # Test core VERSALAW2
    print("\n🔧 TESTING CORE VERSALAW2")
    try:
        from versalaw2 import VERSALAW2
        client = VERSALAW2()
        result = client.analyze_contract("Test contract with denda")
        print(f"✅ Core VERSALAW2: {result['risk_level']} risk")
        passed += 1
    except Exception as e:
        print(f"❌ Core VERSALAW2: {e}")
    
    print(f"\n🎯 FINAL SCORE: {passed}/{total + 1} tests passed")

if __name__ == "__main__":
    main()
