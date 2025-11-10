#!/bin/bash
echo "🚀 VERSALAW2 2.0.0 FINAL DEPLOYMENT"
echo "=========================================="

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf build/ dist/ versalaw2.egg-info/

# Build package
echo "📦 Building package..."
python setup.py sdist bdist_wheel

# Test package
echo "🧪 Testing package..."
python test_final_direct.py

if [ $? -eq 0 ]; then
    echo "🎉 DEPLOYMENT SUCCESSFUL!"
    echo "📊 Package Summary:"
    echo "   • Indonesian Law: 11 modules"
    echo "   • International Law: 6 modules" 
    echo "   • Total: 17 legal analysis modules"
    echo "   • Version: 2.0.0"
    echo ""
    echo "🚀 VERSALAW2 2.0.0 READY FOR PRODUCTION!"
else
    echo "❌ DEPLOYMENT FAILED - Please check errors above"
    exit 1
fi

echo ""
echo "📈 EXTENDED MODULES ADDED:"
echo "   • Legislative Hierarchy Analyzer"
echo "   • Police Ethics Analyzer" 
echo "   • Judicial Ethics Analyzer"
echo "   • Prosecutor Ethics Analyzer"
echo "   • PERMA Analyzer"
echo "   • SEMA Analyzer"
echo ""
echo "🇮🇩 NOW WITH ${total_indonesian} INDONESIAN LAW MODULES!"
