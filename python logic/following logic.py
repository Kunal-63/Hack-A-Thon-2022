import instaloader
from datetime import datetime
from instagrapi import Client
L = instaloader.Instaloader()

profile = instaloader.Profile.from_username(L.context, "jatinbachani333")
L.login("fourth12342023", "fourth_1234")

following_list = []
followings = profile.get_followees()
for following in followings:
    following_list.append(following.username)

cl = Client()
cl.login("fourth12342023", 'fourth_1234')

#====================================================================================================================
#====================================================================================================================
#====================================================================================================================

real_following = []
faked_following = []
for j in following_list:
    percent = 0
    dict=cl.user_info_by_username(j).dict()
    if (dict["is_verified"] == True):
        real_following.append(j)
    else:
        try:
            profile = instaloader.Profile.from_username(L.context, j)
            posts = profile.get_posts()
            post1 = next(posts)
            post2 = next(posts)
            timestamp1 = datetime.fromtimestamp(post1.date_local.timestamp())
            timestamp2 = datetime.fromtimestamp(post2.date_local.timestamp())
            duration = timestamp2 - timestamp1
            print(abs(duration.days)," days")
            if (abs(duration.days) == 1):
                percent +=  0.2


            likes1=[1]
            for i in posts:
                x = i.likes
                if x == 0:
                    x = 1
                    likes1.append(x)
                else: 
                    likes1.append(x)
            avg_likes = sum(likes1) / len(likes1)
            likes_followers_ration = avg_likes / int(dict["follower_count"])
            if (likes_followers_ration >= 0.33):
                percent += 0.05
            elif(likes_followers_ration >= 0.2):
                percent += 0.1
        except :
            pass
        
        try:
            if dict["is_private"] == False:
                percent += 0.1
            else:
                percent += 0.05

            follower_following_ratio = int(dict['follower_count']) / int(dict['following_count'])
            if (follower_following_ratio >= 0.5):
                percent += 0.05
            elif (follower_following_ratio < 0.5 and follower_following_ratio >= 0.33):
                percent += 0.1
            elif (follower_following_ratio < 0.33):
                percent += 0.2


            media_follower_ratio = int(dict["media_count"]) / int(dict["follower_count"])
            if (media_follower_ratio >= 0.5):
                percent += 0.05
            elif (media_follower_ratio > 0.8):
                percent += 0.1
            elif (media_follower_ratio > 1):
                percent += 0.2


            if (dict["biography"] == None) or (len(dict["biography"]) >= 125):
                    percent += 0.2

            
        except:
            pass
    print(j," : ", percent)