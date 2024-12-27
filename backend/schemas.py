from pydantic import BaseModel
from typing import List

class LoginRequest(BaseModel):
    pass

class NonFollowerList(BaseModel):
    non_followers: List[str]

class UnfollowRequest(BaseModel):
    accounts: List[str]
    
class Test(BaseModel):
    username: str
    password: str
