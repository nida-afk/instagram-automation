import time
from instagrapi import Client

# Initialize the client
cl = Client()

# Login with your credentials
cl.login("username", "password")

# Fetch liked posts
liked_posts = cl.liked_medias(amount=2000)  # Adjust the amount as needed

# Add all liked posts to saved posts
for post in liked_posts:
    print(f"Post ID: {post.pk}")
    print(f"Caption: {post.caption_text}")
    print(f"URL: https://www.instagram.com/p/{post.code}/")

    cl.media_save(post.pk)
    print("Post added to saved posts.")

    time.sleep(4)  # Add a delay to avoid rate limiting
