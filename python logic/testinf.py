import instaloader
from datetime import datetime
from instagrapi import Client
L = instaloader.Instaloader()

profile = instaloader.Profile.from_username(L.context, "fakelightning1")
L.login("imop690", "#imop690")
profile = instaloader.Profile.from_username(L.context, "fakelightning1")
posts = profile.get_posts()
post1 = next(posts)
post2 = next(posts)
timestamp1 = datetime.fromtimestamp(post1.date_local.timestamp())
timestamp2 = datetime.fromtimestamp(post2.date_local.timestamp())
duration = timestamp2 - timestamp1
print(abs(duration.days)," days")
