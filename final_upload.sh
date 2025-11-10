#!/bin/bash
cd ~/dragon/global/versalaw2

echo "=== Step 1: Fixing __init__.py ==="
cat > versalaw2/__init__.py << 'EOF'
"""
VersaLaw2 - Comprehensive Indonesian and International Law Library
"""

from . import core
from . import indonesian_law  
from . import international_law

__all__ = ['core', 'indonesian_law', 'international_law']
__version__ = '0.1.5'
__description__ = "Comprehensive Indonesian Law Library with International Law Modules"
EOF

echo "=== Step 2: Cleaning builds ==="
rm -rf build/ dist/ *.egg-info/

echo "=== Step 3: Building package ==="
python setup_final_fixed.py sdist bdist_wheel

echo "=== Step 4: Testing package locally ==="
pip install -e .

echo "=== Step 5: Final import test ==="
python -c "
import versalaw2
print('✓ Final import test passed!')
print('Available modules:', [x for x in dir(versalaw2) if not x.startswith('_')])
"

echo "=== Step 6: Checking package ==="
twine check dist/*

echo "=== Step 7: Uploading to PyPI ==="
twine upload dist/*

echo "=== UPLOAD COMPLETE! ==="
