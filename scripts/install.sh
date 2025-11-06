#!/bin/bash

# Exit on any error
set -e

# Update package list
echo "INFO: Updating package list..."
sudo apt update

# Install Python 3 and pip
echo "INFO: Installing Python 3 and pip..."
sudo apt install -y python3 python3-pip

# Optional: Verify installation
echo "INFO: Verifying installations..."
python3 --version
pip3 --version

echo "INFO: Installation complete. You can now run your script with python3."
