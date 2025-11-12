from versalaw2 import EnhancedLegalClassifierWithDB, LegalDatabaseIntegrator

# Enhanced classifier with database integration
clf = EnhancedLegalClassifierWithDB()

# Direct database access
integrator = LegalDatabaseIntegrator()

# Comprehensive analysis with database insights
result = clf.comprehensive_analysis_with_db("Your legal document or contract")

# Access KUHP 2026 articles
kuhp_articles = clf.get_kuhp_2026_article("legal keyword")

# International standards analysis
international = clf.analyze_with_international_standards("international contract")
