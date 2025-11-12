"""
Config untuk Maya Legal AI
"""

# Path ke source code
SOURCE_PATH = "/root/dragon/global/versalaw2/src"

# Daftar module yang tersedia
MODULES = [
    "MayaWisdomProcessor",
    "MayaLegalQASystem", 
    "EnhancedLegalAnalyzer",
    "DocumentProcessor",
    "ContractAnalyzer",
    "UnifiedLegalAnalyzer",
    "AILegalPersonhoodAnalyzer", 
    "InternationalDigitalLawAnalyzer"
]

# Cara penggunaan
def setup():
    import sys
    sys.path.insert(0, SOURCE_PATH)
    print("✅ Maya Legal AI siap digunakan")

def demo():
    setup()
    from versalaw2 import MayaLegalQASystem
    qa = MayaLegalQASystem()
    answer = qa.ask("Contoh pertanyaan hukum")
    print(f"Jawaban: {answer.answer[:100]}...")
    print(f"Confidence: {answer.confidence:.0%}")
