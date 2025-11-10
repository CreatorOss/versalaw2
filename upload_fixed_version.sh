#!/bin/bash
cd ~/dragon/global/versalaw2

echo "=== Step 1: Update __init__.py version ==="
cat > versalaw2/__init__.py << 'EOF'
"""
VersaLaw2 - Comprehensive Indonesian and International Law Library
"""

from . import core
from . import indonesian_law  
from . import international_law

__all__ = ['core', 'indonesian_law', 'international_law']
__version__ = '0.1.6'
__description__ = "Comprehensive Indonesian Law Library with International Law Modules"
EOF

echo "=== Step 2: Cleaning builds ==="
rm -rf build/ dist/ *.egg-info/

echo "=== Step 3: Building package ==="
python setup_final.py sdist bdist_wheel

echo "=== Step 4: Checking package ==="
twine check dist/*

echo "=== Step 5: Uploading to PyPI ==="
twine upload dist/*

echo "=== UPLOAD COMPLETE! ==="
echo "Test dengan: pip install versalaw2==0.1.6"
