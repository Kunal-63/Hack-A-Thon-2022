from instagrapi import Client
import instaloader
cl = Client()
cl.login("pawankewlani6", '#pawankewlani6')
try:
    dict=cl.user_info_by_username("_kunaladwani_").dict()
    print(dict["is_verified"])
    print(dict["is_private"])
    print(dict["follower_count"])
    print(dict["following_count"])
    print(dict["media_count"])
    print(dict["biography"])
except:
    pass