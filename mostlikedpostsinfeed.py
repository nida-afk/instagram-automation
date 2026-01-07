import time
from instagrapi import Client

# Initialize the client
cl = Client()

# Login with your credentials
cl.login("username", "password")

# Fetch liked posts
liked_posts = cl.liked_medias(amount=3000)  # Adjust the amount as needed

# Sort posts by the number of likes in descending order
liked_posts_sorted = sorted(liked_posts, key=lambda post: post.like_count, reverse=True)

# Get the top 100 posts
top_100_posts = liked_posts_sorted[:50]

# Print the links to the top 100 posts
for post in top_100_posts:
    print(f"Post ID: {post.pk}")
    print(f"Caption: {post.caption_text}")
    print(f"Post lc: {post.like_count}")

    print(f"https://www.instagram.com/p/{post.code}/")

# Optional: Add a delay to avoid rate limiting (if needed)

