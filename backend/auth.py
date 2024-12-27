from instagrapi import Client

def login_instagram(username: str, password: str):
    if not username or not password:
        raise ValueError("Username and password must be provided.")
    
    cl = Client()
    try:
        cl.login(username, password)
        return cl
    except Exception as e:
        raise ValueError("Failed to login to Instagram: " + str(e))
