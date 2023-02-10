import instaloader
from datetime import datetime
from instagrapi import Client
L = instaloader.Instaloader()

profile = instaloader.Profile.from_username(L.context, "_kunaladwani_")
L.login("imop690", "#imop690")

followers = profile.get_followers()
followers_list = []
for follower in followers:
    followers_list.append(follower.username)

following_list = []
followings = profile.get_followees()
for following in followings:
    following_list.append(following.username)


cl = Client()
cl.login("imop690", '#imop690')



#====================================================================================================================
#====================================================================================================================
#====================================================================================================================



real_followers = []
faked_followers = []
percent = 0
for i in followers_list:
    dict=cl.user_info_by_username(i).dict()
    if (dict["is_verified"] == True):
        real_followers.append(i)
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
            if abs(duration.days) <= 1:
                percent +=  0.2               
        except:
            pass 
        try:
            if dict["is_private"] == False:
                pass
            else:
                pass


            follower_following_ratio = int(dict['following_count']) / int(dict['follower_count'])
            if (follower_following_ratio < 2):
                pass


            if int(dict["media_count"] < 15):
                pass


            if (dict["biography"] == None):
                    percent += 0.2
            

            print("\n\n\n")
        except:
            pass
    break
