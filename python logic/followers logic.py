import instaloader
from datetime import datetime
from instagrapi import Client

L = instaloader.Instaloader()
profile = instaloader.Profile.from_username(L.context, "pratt.css")

# try:
# posts = profile.get_posts()
# post1 = next(posts)
# post2 = next(posts)
# timestamp1 = datetime.fromtimestamp(post1.date_local.timestamp())
# timestamp2 = datetime.fromtimestamp(post2.date_local.timestamp())
# duration = timestamp2 - timestamp1
# print(abs(duration.days))


L.login("first_102030", "first_ig123")

followers = profile.get_followers()
followers_list = []
for follower in followers:
    followers_list.append(follower.username)
# print(len(followers_list))
real_followers = []
faked_followers = []
cl = Client()
cl.login("first_102030", 'first_ig123')
for i in followers_list:
    dict=cl.user_info_by_username(i).dict()
    if (dict["is_verified"] == True):
        real_followers.append(i)
        print(real_followers)
    else:
        try:
            profile = instaloader.Profile.from_username(L.context, "first_102030")
            posts = profile.get_posts()
            post1 = next(posts)
            post2 = next(posts)
            timestamp1 = datetime.fromtimestamp(post1.date_local.timestamp())
            timestamp2 = datetime.fromtimestamp(post2.date_local.timestamp())
            duration = timestamp2 - timestamp1
            print(abs(duration.days)," days")
        except:
            pass 
        try:
            print("private",dict["is_private"])
            print("follower count",dict["follower_count"])
            print("following count",dict["following_count"])
            print("media count",dict["media_count"])
            print("biography ",dict["biography"])
            print("\n\n\n")
        except:
            pass
    break