from schemas import LoginRequest, NonFollowerList, UnfollowRequest
from auth import login_instagram
from followers import get_non_followers
from unfollow import unfollow_accounts

cli = login_instagram()
print(cli)
non_followers = get_non_followers(cli)
print(non_followers)
# unfollowed = unfollow_accounts(cli, non_followers)
# print(unfollowed)