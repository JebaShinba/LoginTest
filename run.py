import subprocess
import os

print("Starting Selenium Tests...")
print("Current working directory:", os.getcwd())

env = os.environ.copy()
env["PYTHONPATH"] = os.path.abspath(".")

try:
    subprocess.run(["python", "./scripts/setup_mongodb.py"], env=env, check=True)
    subprocess.run(["python", "./login_testcases/valid.py"], env=env, check=True)
except FileNotFoundError as e:
    print(f"File not found: {e}")
except subprocess.CalledProcessError as e:
    print(f"Error during script execution: {e}")

print("All tests completed.")

