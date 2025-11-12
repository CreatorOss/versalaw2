"""
Maya Legal AI - Simple Configuration
"""

MAYA_AI_CONFIG = {
    "package_path": "/root/dragon/global/versalaw2/src",
    "core_modules": [
        "MayaLegalQASystem",
        "MayaWisdomProcessor", 
        "EnhancedLegalAnalyzer",
        "DocumentProcessor",
        "ContractAnalyzer",
        "UnifiedLegalAnalyzer"
    ],
    "status": "production_ready",
    "version": "1.0.0"
}

def setup_maya_ai():
    """Setup Maya Legal AI system"""
    import sys
    sys.path.insert(0, MAYA_AI_CONFIG["package_path"])
    print("✅ Maya Legal AI system configured")
    
def get_qa_system():
    """Get Q&A system instance"""
    from versalaw2 import MayaLegalQASystem
    return MayaLegalQASystem()

def get_wisdom_system():
    """Get wisdom system instance""" 
    from versalaw2 import MayaWisdomProcessor
    return MayaWisdomProcessor()
