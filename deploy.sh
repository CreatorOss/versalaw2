#!/bin/bash
echo "🚀 Deploy Maya Legal AI..."

# Build package
echo "📦 Building package..."
python setup.py sdist bdist_wheel

# Cek build
if [ -d "dist" ]; then
    echo "✅ Build successful"
    echo "📁 Files in dist/:"
    ls -la dist/
else
    echo "❌ Build failed"
    exit 1
fi

echo ""
echo "🎯 Untuk upload ke PyPI:"
echo "   twine upload dist/*"
echo ""
echo "🎯 Untuk upload ke Git:"
echo "   git init && git add . && git commit -m 'Deploy Maya Legal AI'"
echo "   git remote add origin [REPO_URL]"
echo "   git push -u origin main"
echo ""
echo "💫 Deploy preparation completed!"
