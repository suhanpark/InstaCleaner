import json
from datetime import datetime

def get_non_followers(cl):
    followings = cl.user_following(cl.user_id)
    followers = cl.user_followers(cl.user_id)

    non_followers = [
        {
            "username": user.username,
            "full_name": user.full_name
        }
        for user in followings.values()
        if user.pk not in followers
    ]

    # Save to JSON file with timestamp
    filename = f"non_followers.json"
    with open(filename, 'w') as file:
        json.dump(non_followers, file, indent=4)
    
    return non_followers, filename
