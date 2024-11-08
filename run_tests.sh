#!/bin/bash

echo "Starting Selenium Tests..."

# Define the Windows path
script_path="C:/Users/jebas/LoginTest"

# Convert Windows path to Unix path for WSL/Git Bash
script_path_unix=$(echo "$script_path" | sed 's|C:|/mnt/c|')

# Debugging: Print the converted path
echo "Converted path: $script_path_unix"

# Check if the files exist
echo "Running MongoDB script at: $script_path_unix/scripts/setup_mongodb.py"
echo "Running Valid Test script at: $script_path_unix/login_testcases/valid.py"

# Run each Selenium test script using Python
python "$script_path_unix/scripts/setup_mongodb.py"
python "$script_path_unix/login_testcases/valid.py"

echo "All tests completed."




