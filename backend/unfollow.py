import json
import time
from typing import List

def unfollow_accounts(cl, file_path: str, delay: float = 1.0) -> List[dict]:
    """
    Unfollow accounts listed in a JSON file with a 'non_followers' key.

    Args:
        cl: Instagram Client instance.
        file_path: Path to the JSON file containing non-followers.
        delay: Delay in seconds between each unfollow action.

    Returns:
        List of results with status for each username.
    """
    unfollowed = []
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Ensure 'non_followers' key exists and is a list
        non_followers = data.get("non_followers", [])
        if not isinstance(non_followers, list):
            raise ValueError("Invalid JSON structure: 'non_followers' must be a list.")

        for user in non_followers:
            username = user.get("username")
            full_name = user.get("full_name", "Unknown")
            
            if username:
                try:
                    user_id = cl.user_id_from_username(username)
                    cl.user_unfollow(user_id)
                    unfollowed.append({
                        "username": username,
                        "full_name": full_name,
                        "status": "unfollowed"
                    })
                    print(f"✅ Unfollowed: {username} ({full_name})")
                    
                    # Optional delay to prevent rate-limiting
                    time.sleep(delay)
                
                except Exception as e:
                    unfollowed.append({
                        "username": username,
                        "full_name": full_name,
                        "status": f"failed - {str(e)}"
                    })
                    print(f"❌ Failed to unfollow: {username} ({full_name}) - {str(e)}")
            else:
                unfollowed.append({
                    "username": "N/A",
                    "full_name": full_name,
                    "status": "skipped - username missing"
                })
                print(f"⚠️ Skipped an entry due to missing username.")
    
    except FileNotFoundError:
        raise ValueError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")
    
    return unfollowed
