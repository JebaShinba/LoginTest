from selenium import webdriver
import unittest
import sys
from homeobjects.login import LoginPage
from configfile.config import MongoClient  # Assuming MongoClient is defined in config
from selenium.webdriver.chrome.options import Options

class ValidLoginTest(unittest.TestCase):
    valid_users = []
    client = None  # Class variable to hold the MongoDB client

    @classmethod
    def setUpClass(cls):
        # Initialize the MongoDB client
        cls.client = MongoClient("mongodb://127.0.0.1:27017/")  # Update this URI as necessary
        cls.db = cls.client["sampleupload"]  # Use your actual database name
        cls_users_collection = cls.db["users"]  # Use your actual collection name

        # Fetch valid user credentials from MongoDB
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        # Configure headless Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run headless
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")

        # Instantiate headless Chrome
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(5)

        # Retrieve only valid users
        cls.valid_users = list(cls_users_collection.find({"is_valid": True}))
        
        print("Valid users fetched:", cls.valid_users)  # Debugging output

        if not cls.valid_users:
            raise Exception("No valid users found in the database!")

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

                # Print the username and password being tested
                print(f"Testing login for Username: '{username}' with Password: '{password}'")

                # Navigate to the base URL
                try:
                    self.driver.get(base_url)
                    print("Navigated to:", base_url)
                except Exception as e:
                    print("Error navigating to base URL:", e)
                    continue  # Skip to the next user if navigation fails

                # Instantiate the LoginPage object
                lg = LoginPage(self.driver)
                lg.setUsername(username)  # Enter the username
                lg.setPassword(password)  # Enter the corresponding password
                lg.clickLogin()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.client.close()  # Close the MongoDB client
        print("Browser closed and MongoDB client connection closed.")

if __name__ == '__main__':
    unittest.main()