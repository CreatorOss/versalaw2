#!/bin/bash
cd ~/dragon/global/versalaw2

echo "=== Cleaning previous builds ==="
rm -rf build/ dist/ *.egg-info/

echo "=== Building package ==="
python setup_correct.py sdist bdist_wheel

echo "=== Checking package ==="
twine check dist/*

if [ $? -eq 0 ]; then
    echo "=== Package check passed! Uploading to PyPI ==="
    twine upload dist/*
else
    echo "=== Package check failed! Fixing... ==="
    
    # Alternative build method
    pip install build
    python -m build
    twine check dist/*
    twine upload dist/*
fi

echo "=== Done! ==="
