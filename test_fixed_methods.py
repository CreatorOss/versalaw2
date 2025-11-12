import sys
import os
sys.path.insert(0, 'src')

from versalaw2 import AILegalPersonhoodAnalyzer, InternationalDigitalLawAnalyzer

print("🔧 FIXING TEST METHODS...")

# Test AILegalPersonhoodAnalyzer
ai_analyzer = AILegalPersonhoodAnalyzer()

# consciousness_tests mungkin property, bukan method
if hasattr(ai_analyzer, 'consciousness_tests'):
    if callable(ai_analyzer.consciousness_tests):
        result = ai_analyzer.consciousness_tests()
        print("✅ consciousness_tests(): METHOD")
    else:
        result = ai_analyzer.consciousness_tests
        print("✅ consciousness_tests: PROPERTY")
else:
    print("❌ consciousness_tests: NOT FOUND")

# Test InternationalDigitalLawAnalyzer  
intl_analyzer = InternationalDigitalLawAnalyzer()

# digital_law_framework mungkin property, bukan method
if hasattr(intl_analyzer, 'digital_law_framework'):
    if callable(intl_analyzer.digital_law_framework):
        result = intl_analyzer.digital_law_framework()
        print("✅ digital_law_framework(): METHOD")
    else:
        result = intl_analyzer.digital_law_framework
        print("✅ digital_law_framework: PROPERTY")
else:
    print("❌ digital_law_framework: NOT FOUND")
