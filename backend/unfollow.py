import json

def unfollow_accounts(cl, file_path: str):
    unfollowed = []
    try:
        with open(file_path, 'r') as file:
            non_followers = json.load(file)
        
        for user in non_followers:
            username = user.get("username")
            if username:
                try:
                    user_id = cl.user_id_from_username(username)
                    cl.user_unfollow(user_id)
                    unfollowed.append({"username": username, "status": "unfollowed"})
                except Exception as e:
                    unfollowed.append({"username": username, "status": f"failed - {str(e)}"})
    
    except FileNotFoundError:
        raise ValueError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON in file: {file_path}")
    
    return unfollowed
