#!/bin/bash

# Activate virtual environment
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv venv
fi

source venv/bin/activate

# Install required packages
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "Error: requirements.txt not found!"
    exit 1
fi

# Run the app
echo "Starting the application..."
python app.py

# Make the script executable
chmod +x build.sh

# Start the app (optional if calling this script directly)
echo "Build script executed successfully."
