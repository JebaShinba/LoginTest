# scripts/setup_mongodb.py
import sys
import os

# Add the config file's directory to PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), '../LoginTest/configfile'))

import config  # Now it should find config.py

from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")
db = client['sampleupload']
db.users.insert_one({
    "username": config.username,
    "password": config.password,
    "baseurl": config.baseurl,
    "is_valid": config.is_valid
})
print("Inserted test user data")
