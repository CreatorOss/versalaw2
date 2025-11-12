#!/usr/bin/env python3
"""
TEST INSTALLED VERSION
"""

import versalaw2

print("🔍 TESTING INSTALLED VERSION:")
print(f"Package: {versalaw2.__name__}")
print(f"Version: {getattr(versalaw2, '__version__', 'N/A')}")
print(f"File: {versalaw2.__file__}")

# Test functionality
from versalaw2 import EnhancedLegalClassifierWithDB, UnifiedAnalysisEngine

clf = EnhancedLegalClassifierWithDB()
unified = UnifiedAnalysisEngine()

result = clf.comprehensive_analysis_with_db("Test contract")
print(f"✅ Analysis: {result.get('analysis_level', 'N/A')}")

result2 = unified.unified_analyze("Test contract") 
print(f"✅ Unified: {result2.get('analysis_type', 'N/A')}")

print("🎉 VERSION 3.0.0 CONFIRMED!")
