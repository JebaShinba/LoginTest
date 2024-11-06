# scripts/setup_mongodb.py
import sys
sys.path.insert(0, './LoginTest/configfile')  # Adjust the path
import config
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
