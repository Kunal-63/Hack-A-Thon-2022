#---------------------------------------------------------------------------------------------
# for profile pic
import instaloader

# Initialize the Instaloader object
L = instaloader.Instaloader()

# Search for the profile using the username
profile = instaloader.Profile.from_username(L.context, "sukhwani_mayur_")

#L.download_profilepic(profile, "instagram_username.jpg")
#---------------------------------------------------------------------------------------------
# for post duration
from datetime import datetime
posts = profile.get_posts()

# Get the first two posts
post1 = next(posts)
post2 = next(posts)

# Get the timestamps of the two posts
timestamp1 = datetime.fromtimestamp(post1.date_local.timestamp())
timestamp2 = datetime.fromtimestamp(post2.date_local.timestamp())

# Calculate the difference between the two timestamps
duration = timestamp2 - timestamp1

print("Duration between two posts:", duration)
#---------------------------------------------------------------------------------------------
# for bio
bio = profile.biography

print(bio)

#----------------------------------------------------------------------------------------------
# user id of username 
# Get the profile ID
profile_id = profile.userid

print(profile_id)

#----------------------------------------------------------------------------------------------
# Check if the profile is private
if profile.is_private:
    print("The profile is private.")
else:
    print("The profile is public.")

#---------------------------------------------------------------------------------------------
# Check if the profile is verified
if profile.is_verified:
    print("The Instagram ID is verified")
else:
    print("The Instagram ID is not verified")

#---------------------------------------------------------------------------------------------
#count of followers and followings and no.of posts
# Get the number of followers and following from the profile object
followers = profile.followers
following = profile.followees

print("Followers: ", followers)
print("Following: ", following)

post_count = profile.mediacount

print("The number of posts is:", post_count)
#---------------------------------------------------------------------------------------------
#  for followers and followings
# Login or load session
L.login("prathamchellani4", "#prathamchellani4")

# Obtain profile metadata
print("list of followers")
followers = profile.get_followers()
for follower in followers:
    print(follower.username)

print(" list of followings")
followers = profile.get_followees()
for follower in followers:
    print(follower.username)

#------------------------------------------------------------------------------------------
# posts,caption and no.of likes
import instaloader

L = instaloader.Instaloader()

username = input("Enter the Instagram username: ")          #use bajaj3737

profile = instaloader.Profile.from_username(L.context, username)

print("\nLatest posts from", username + ":")
try:
    for post in profile.get_posts():
        print("Post link:", post.url)
        print("Caption:", post.caption)
        print("Likes:", post.likes)
        print("-----------------------------")
except:
    pass
    

