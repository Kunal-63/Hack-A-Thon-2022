import instaloader
from datetime import datetime
from instagrapi import Client

L = instaloader.Instaloader()
profile = instaloader.Profile.from_username(L.context, "fakelightning1")
real = 0

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
            profile = instaloader.Profile.from_username(L.context, i)
            posts = profile.get_posts()
            post1 = next(posts)
            post2 = next(posts)
            timestamp1 = datetime.fromtimestamp(post1.date_local.timestamp())
            timestamp2 = datetime.fromtimestamp(post2.date_local.timestamp())
            duration = timestamp2 - timestamp1
            print(abs(duration.days)," days")
            if(abs(duration.days) >= 2):
                real += 1
        except:
            pass 
        try:
            # print("private",dict["is_private"])
            if dict["is_private"] == False:
                pass
            else:
                real += 1
            follower_following_ratio = int(dict['following_count']) / int(dict['follower_count'])
            if (follower_following_ratio < 2):
                real += 1
            # print("follower count",dict["follower_count"])
            # print("following count",dict["following_count"])
            if int(dict["media_count"] < 15):
                real += 1
            # print("media count",dict["media_count"])
            if (dict["biography"] == None):
                    pass
            else:
                real +=1
            # print("biography ",dict["biography"])
            print(real/5)
            print("\n\n\n")
        except:
            pass
    break