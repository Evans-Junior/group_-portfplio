#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Please install Python 3 and try again."
    exit 1
fi

# Activate virtual environment
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv venv
else
    echo "Virtual environment found. Activating..."
fi

# Activate the virtual environment
source venv/bin/activate

# Install required packages
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install --upgrade pip  # Upgrade pip to the latest version
    pip install -r requirements.txt
else
    echo "Error: requirements.txt not found!"
    exit 1
fi

# Run the app
echo "Starting the application..."
python app.py

# Make the script executable (if you want to ensure it's executable for future runs)
chmod +x build.sh

# Optional message after the script runs
echo "Build script executed successfully."
