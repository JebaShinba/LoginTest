from selenium import webdriver
import unittest
from homeobjects.login import LoginPage
from configfile.config import MongoClient
from selenium.webdriver.chrome.options import Options

class ValidLoginTest(unittest.TestCase):
    valid_users = []
    client = None

    @classmethod
    def setUpClass(cls):
        try:
            # Initialize MongoDB client
            cls.client = MongoClient("mongodb://127.0.0.1:27017/")
            cls.db = cls.client["sampleupload"]
            cls.users_collection = cls.db["users"]

            # Retrieve valid users
            cls.valid_users = list(cls.users_collection.find({"is_valid": True}))
            if not cls.valid_users:
                # Insert a test user if none exist
                print("No valid users found. Inserting a test user...")
                cls.users_collection.insert_one({
                    "username": "testuser",
                    "password": "testpass",
                    "baseurl": "https://demo.filebrowser.org/login?redirect=/files/",
                    "is_valid": True
                })
                cls.valid_users = list(cls.users_collection.find({"is_valid": True}))

            # Configure headless Chrome options
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")

            # Start Chrome WebDriver
            cls.driver = webdriver.Chrome(options=chrome_options)
            cls.driver.implicitly_wait(5)

            print("Valid users fetched:", cls.valid_users)

        except Exception as e:
            print("Error connecting to MongoDB:", e)
            cls.tearDownClass()
            raise

    def test_login_with_valid_users(self):
        for index, user_details in enumerate(self.valid_users):
            with self.subTest(user_index=index):
                if all(key in user_details for key in ["username", "password", "baseurl"]):
                    username = user_details["username"]
                    password = user_details["password"]
                    base_url = user_details["baseurl"]

                    print(f"Testing login for Username: '{username}' with Password: '{password}'")
                    
                    try:
                        self.driver.get(base_url)
                        lg = LoginPage(self.driver)
                        lg.setUsername(username)
                        lg.setPassword(password)
                        lg.clickLogin()
                    except Exception as e:
                        print(f"Login test failed for user {username}: {e}")
                else:
                    print("Skipping user with missing details:", user_details)

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'driver') and cls.driver:
            cls.driver.quit()
        if hasattr(cls, 'client') and cls.client:
            cls.client.close()
        print("Resources cleaned up.")

if __name__ == '__main__':
    unittest.main()

