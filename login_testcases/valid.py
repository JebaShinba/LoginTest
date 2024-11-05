from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
from pymongo import MongoClient  # Ensure you're using pymongo
from homeobjects.login import LoginPage  # Import your LoginPage class

class ValidLoginTest(unittest.TestCase):
    valid_users = []
    client = None  # Class variable to hold the MongoDB client

    @classmethod
    def setUpClass(cls):
        # Initialize the MongoDB client
        try:
            cls.client = MongoClient("mongodb://127.0.0.1:27017/")  # Update this URI if necessary
            cls.db = cls.client["sampleupload"]  # Use your actual database name
            cls.users_collection = cls.db["users"]  # Use your actual collection name

            # Fetch valid user credentials from MongoDB
            cls.valid_users = list(cls.users_collection.find({"is_valid": True}))
            print("Valid users fetched:", cls.valid_users)  # Debugging output

            if not cls.valid_users:
                raise Exception("No valid users found in the database!")

        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            cls.tearDownClass()  # Ensure teardown even if setup fails
            raise

        # Set up Chrome in headless mode with options
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")  # Run headless
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")

            cls.driver = webdriver.Chrome(options=chrome_options)
            cls.driver.implicitly_wait(5)

        except Exception as e:
            print(f"Error initializing ChromeDriver: {e}")
            cls.tearDownClass()  # Ensure teardown even if setup fails
            raise

    def test_login_with_valid_users(self):
        # Iterate over valid users and perform login
        for index, user_details in enumerate(self.valid_users):
            with self.subTest(user_index=index):
                required_keys = ["username", "password", "baseurl"]

                # Ensure all necessary keys are present
                if not all(key in user_details for key in required_keys):
                    print("Skipping login due to missing keys:", user_details)
                    continue  # Skip to the next user if keys are missing

                username = user_details["username"]
                password = user_details["password"]
                base_url = user_details["baseurl"]

                print(f"Testing login for Username: '{username}' with Password: '{password}'")

                # Navigate to the base URL
                try:
                    self.driver.get(base_url)
                    print("Navigated to:", base_url)
                except Exception as e:
                    print("Error navigating to base URL:", e)
                    continue  # Skip to the next user if navigation fails

                # Instantiate the LoginPage object and perform login
                lg = LoginPage(self.driver)
                lg.setUsername(username)
                lg.setPassword(password)
                lg.clickLogin()

                # Add assertions here as needed to verify login success
                # e.g., self.assertTrue(lg.isLoginSuccessful(), "Login failed")

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()
            print("Browser closed.")
        if cls.client:
            cls.client.close()
            print("MongoDB client connection closed.")

if __name__ == '__main__':
    unittest.main()
