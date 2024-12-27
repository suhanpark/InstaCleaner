from fastapi import FastAPI, HTTPException
from schemas import LoginRequest, NonFollowerList, UnfollowRequest
from auth import login_instagram
from followers import get_non_followers
from unfollow import unfollow_accounts
from fastapi import Query

app = FastAPI()

@app.post("/login/")
async def login(request: LoginRequest):
    try:
        global client
        client = login_instagram(request.username, request.password)
        return {"message": "Login successful"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/non-followers/")
async def get_non_followers_list():
    if client is None:
        raise HTTPException(status_code=400, detail="Client not authenticated. Please log in first.")
    try:
        non_followers, filename = get_non_followers(client)
        return {
            "non_followers": non_followers,
            "file_path": filename,
            "message": f"Non-followers saved to {filename}"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving non-followers: {str(e)}")

@app.post("/unfollow/")
async def unfollow_accounts_from_json(
    file_path: str,
    delay: float = Query(1.0, description="Delay between unfollow actions in seconds")
):
    """
    Unfollow accounts listed in the given JSON file with optional delay.

    Args:
        file_path: Path to the JSON file.
        delay: Delay between unfollow actions (default 1.0s).

    Returns:
        A list of statuses for each unfollowed account.
    """
    global client
    if client is None:
        raise HTTPException(status_code=400, detail="Client not authenticated. Please log in first.")
    
    try:
        unfollowed = unfollow_accounts(client, file_path, delay)
        return {
            "message": f"Processed unfollow actions from {file_path} with a {delay}s delay",
            "unfollowed": unfollowed
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error during unfollow process: {str(e)}")



