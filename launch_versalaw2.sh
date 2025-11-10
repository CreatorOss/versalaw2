#!/bin/bash
# VERSALAW2 Simple Launcher

echo "🚀 Starting VERSALAW2..."
export PYTHONPATH="/root/dragon/global/versalaw2:$PYTHONPATH"

cd /root/dragon/global/versalaw2

# Check if running in interactive mode
if [ -t 0 ]; then
    echo "VERSALAW2 v2.1.0 - Indonesian Legal AI Platform"
    echo "Available options:"
    echo "1. Run Quick Demo"
    echo "2. Run Interactive CLI" 
    echo "3. Run Comprehensive Test"
    echo "4. Exit"
    
    read -p "Choose option (1-4): " choice
    
    case $choice in
        1) python examples/quick_demo.py ;;
        2) python versalaw2_cli.py ;;
        3) python test_all_indonesian_law.py ;;
        4) echo "Goodbye!"; exit ;;
        *) echo "Invalid option"; exit 1 ;;
    esac
else
    # Non-interactive - run quick demo
    python examples/quick_demo.py
fi
