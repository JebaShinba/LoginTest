#!/bin/bash

echo "Starting Selenium Tests..."

# Run each Selenium test script
python scripts/setup_mongodb.py
python login_testcases/valid.py
# Add additional scripts as needed

echo "All tests completed."
