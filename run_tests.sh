#!/bin/bash

echo "Starting Selenium Tests..."

# Run each Selenium test script
python C:/Users/jebas/LoginTest/scripts/setup_mongodb.py
python C:/Users/jebas/LoginTest/login_testcases/valid.py
# Add additional scripts as needed

echo "All tests completed."
