#!/bin/bash
echo "🚀 VERSALAW2 FINAL DEPLOYMENT"
echo "=========================================="

# Check Python version
echo "📋 System Check..."
python3 --version
pip3 --version

# Install dependencies
echo "📦 Installing Dependencies..."
pip3 install -r requirements.txt

# Run comprehensive tests
echo "🧪 Running Comprehensive Tests..."
echo "1. Testing Core Legal Modules..."
python3 test_comprehensive_scenarios.py

echo "2. Testing Specialized Crimes..."
python3 test_all_crimes_master.py

echo "3. Testing Individual Modules..."
python3 test_fixed_narcotics.py
python3 test_fixed_money_laundering.py

# Build package
echo "🏗️ Building Package..."
python3 setup.py sdist bdist_wheel

# Create deployment structure
echo "📁 Creating Deployment Structure..."
mkdir -p deployment/{config,logs,data}
cp -r versalaw2 deployment/
cp requirements.txt deployment/
cp README.md deployment/
cp setup.py deployment/

# Create production config
cat > deployment/config/production.yaml << 'CONFIG'
# VERSALAW2 Production Configuration
version: "2.0.0"
deployment: "production"

modules:
  enabled:
    - constitutional_law
    - statutory_law
    - criminal_justice
    - civil_law
    - professional_ethics
    - specialized_crimes:
        - anti_corruption
        - money_laundering
        - human_trafficking
        - illegal_mining
        - illegal_logging
        - narcotics
        - smuggling
        - cyber_crime

logging:
  level: "INFO"
  file: "logs/versalaw2.log"

analysis:
  max_document_size: "10MB"
  supported_formats: ["pdf", "docx", "txt"]
  timeout_seconds: 300

api:
  enabled: true
  port: 8000
  rate_limit: "100/hour"
CONFIG

echo "✅ Deployment Package Created!"
echo "📊 MODULES DEPLOYED:"
echo "   🏛️  Constitutional Law"
echo "   ⚖️  Statutory Law" 
echo "   👮 Criminal Justice"
echo "   📝 Civil Law"
echo "   👨‍⚖️ Professional Ethics"
echo "   🎯 SPECIALIZED CRIMES (8 Modules):"
echo "      • TIPIKOR (Korupsi)"
echo "      • Money Laundering"
echo "      • Human Trafficking" 
echo "      • Illegal Mining"
echo "      • Illegal Logging"
echo "      • Narcotics"
echo "      • Smuggling"
echo "      • Cyber Crime"

echo ""
echo "🎉 VERSALAW2 READY FOR PRODUCTION!"
echo "📍 Deployment Directory: ./deployment"
echo "📚 Documentation: ./deployment/README.md"
echo "⚙️  Config: ./deployment/config/production.yaml"
