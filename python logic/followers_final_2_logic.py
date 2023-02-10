import instaloader
from datetime import datetime
from instagrapi import Client
L = instaloader.Instaloader()

profile = instaloader.Profile.from_username(L.context, "")
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

real_followers = []
faked_followers = []

