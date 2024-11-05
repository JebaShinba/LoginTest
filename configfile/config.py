from pymongo import MongoClient

MONGO_URI = "mongodb://127.0.0.1:27017/"
DATABASE_NAME = "sampleupload"  # Use your actual database name
USER_COLLECTION = "users"  # Corrected variable name
FILES_COLLECTION = "deletefiles"

def get_db():
    """Connect to MongoDB and return the database instance."""
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    return db, client  # Return both the database and client for later closure

def get_users_collection():
    """Get the users collection from the database."""
    db, client = get_db()  # Get both the database and client
    try:
        user_collection = db[USER_COLLECTION]  # Use a single bracket
        return user_collection  # Return the users collection
    finally:
        client.close()  # Ensure the client is closed after use

def get_files_collection():
    """Get the files collection from the database."""
    db, client = get_db()  # Get both the database and client
    try:
        files_collection = db[FILES_COLLECTION]  # Use a single bracket
        return files_collection  # Return the files collection
    finally:
        client.close()  # Ensure the client is closed after use