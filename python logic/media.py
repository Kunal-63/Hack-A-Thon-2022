from instagrapi import Client

cl = Client()
cl.login("kunal_adwani6", '#kunal_adwani6')

user_id = cl.user_id_from_username("leomessi")
medias = cl.user_medias(user_id,5)
for media in medias:
    #caption
    print(media.caption_text)
    #duration
    print(media.video_duration)
    #comment count
    print(media.comment_count)
    #like count
    print(media.like_count)
    #views
    print(media.view_count)
    break