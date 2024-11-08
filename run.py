import subprocess
import os

print("Starting Selenium Tests...")

# Get the existing environment and add PYTHONPATH
env = os.environ.copy()
env["PYTHONPATH"] = "C:/Users/jebas/LoginTest"

# Run each Selenium test script with the modified environment
subprocess.run(["python", "C:/Users/jebas/LoginTest/scripts/setup_mongodb.py"], env=env)
subprocess.run(["python", "C:/Users/jebas/LoginTest/login_testcases/valid.py"], env=env)

print("All tests completed.")
