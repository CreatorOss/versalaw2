#!/bin/bash
echo "🧪 AUTO-TEST PYPI AVAILABILITY"
echo "=========================================="

# Test setiap 2 menit
for i in {1..10}; do
    echo "Attempt $i/10: Testing package availability..."
    
    cd /tmp
    rm -rf test-pypi-$i
    mkdir test-pypi-$i
    cd test-pypi-$i
    
    python -m venv venv
    source venv/bin/activate
    
    # Try install
    if pip install versalaw2 2>/dev/null; then
        echo ""
        echo "🎉 🎉 🎉 VERSALAW2 2.0.0 IS NOW LIVE! 🎉 🎉 🎉"
        python -c "
import versalaw2
print('✅ PACKAGE INSTALLED FROM PYPI!')
print('Version:', versalaw2.__version__)
result = versalaw2.analyze_contract('Perjanjian dengan denda 100%')
print('Risk:', result['risk_level'])
print('Jurisdiction:', result['jurisdiction'])
print('')
print('🚀 VERSALAW2 2.0.0 OFFICIALLY PUBLIC!')
print('🌍 Anyone can now: pip install versalaw2')
        "
        exit 0
    else
        echo "⏳ Package not available yet... waiting 2 minutes"
        sleep 120
    fi
done

echo "❌ Package still not available after 10 attempts"
echo "Check PyPI email for verification requirements"
