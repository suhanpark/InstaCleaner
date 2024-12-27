from fastapi import FastAPI, HTTPException
from schemas import LoginRequest, NonFollowerList, UnfollowRequest
from auth import login_instagram
from followers import get_non_followers
from unfollow import unfollow_accounts

app = FastAPI()

from auth import login_instagram
from schemas import LoginRequest

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
    global client
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
async def unfollow(file_path: str):
    global client
    if client is None:
        raise HTTPException(status_code=400, detail="Client not authenticated. Please log in first.")
    try:
        unfollowed = unfollow_accounts(client, file_path)
        return {
            "message": f"Processed unfollow actions from {file_path}",
            "unfollowed": unfollowed
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error during unfollow process: {str(e)}")


