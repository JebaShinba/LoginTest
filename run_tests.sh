#!/bin/bash

echo "Starting Selenium Tests..."
# Define the path for the project (Unix-style path for CI environment)
script_path="/home/runner/work/LoginTest/LoginTest"  # GitHub Actions path
# Define the path for the project
script_path="C:/Users/jebas/LoginTest"

# Add LoginTest to PYTHONPATH
export PYTHONPATH="$script_path"

# Print the paths for debugging
echo "Using script path: $script_path"

# Run each Selenium test script using Windows-style paths
python "$script_path/scripts/setup_mongodb.py"
python "$script_path/login_testcases/valid.py"

echo "All tests completed."





