import os
from instagrapi import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve credentials from .env
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

def login_instagram():
    if not INSTAGRAM_USERNAME or not INSTAGRAM_PASSWORD:
        raise ValueError("Instagram credentials are missing in the .env file.")

    cl = Client()
    try:
        cl.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
        return cl
    except Exception as e:
        raise ValueError("Failed to login to Instagram: " + str(e))
