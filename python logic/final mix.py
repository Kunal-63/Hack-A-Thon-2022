import instaloader
from datetime import datetime
from instagrapi import Client

L = instaloader.Instaloader()
profile = instaloader.Profile.from_username(L.context, "_kunaladwani_")

posts = profile.get_posts()
try:
    post1 = next(posts)
    post2 = next(posts)
    timestamp1 = datetime.fromtimestamp(post1.date_local.timestamp())
    timestamp2 = datetime.fromtimestamp(post2.date_local.timestamp())
    duration = timestamp2 - timestamp1
    print("Duration between two posts:", duration)
except:
    pass 

L.login("prathamchellani4", "#prathamchellani4")

# print("list of followers")
followers = profile.get_followers()
followers_list = []
for follower in followers:
    followers_list.append(follower.username)
    
# print(" list of followings")
following_list = []
followers = profile.get_followees()
for follower in followers:
    # print(follower.username)
    following_list.append(follower.username)

print(followers_list)
print(following_list)

for i in range(followers_list):
    if ( followers_list[i] in following_list ):
        del followers_list[i]

cl = Client()
cl.login("prathamchellani4", '#prathamchellani4')
for i in followers_list:
    try:
        print(i)
        dict=cl.user_info_by_username(i).dict()
        print("verified",dict["is_verified"])
        print("private",dict["is_private"])
        print("follower count",dict["follower_count"])
        print("following count",dict["following_count"])
        print("media count",dict["media_count"])
        print("biography ",dict["biography"])
        print("\n\n\n")
    except:
        pass

for j in following_list:
    try:
        print(j)
        dict=cl.user_info_by_username(j).dict()
        print("verified",dict["is_verified"])
        print("private",dict["is_private"])
        print("follower count",dict["follower_count"])
        print("following count",dict["following_count"])
        print("media count",dict["media_count"])
        print("biography ",dict["biography"])
        print("\n\n\n")
    except:
        pass