import time

from instagrapi import Client

def get_top_liked_posts(username, password, target_user, top_n=20):
    # Initialize the client
    cl = Client()

    # Login with your credentials
    cl.login(username, password)

    # Fetch the target user's posts
    user_id = cl.user_id_from_username(target_user)
    user_posts = cl.user_medias(user_id, amount=899)  # Adjust the amount as needed

    # Sort posts by the number of likes in descending order
    sorted_posts = sorted(user_posts, key=lambda post: post.like_count, reverse=True)

    # Get the top N posts
    top_posts = sorted_posts[:top_n]

    return top_posts

# Replace with your Instagram credentials and the target user
username = "username"
password = "password"
target_user = "dreamy.fantasys"

top_posts = get_top_liked_posts(username, password, target_user)

# Print the URLs of the top 20 posts
for post in top_posts:
    print(f"URL: https://www.instagram.com/p/{post.code}/, Likes: {post.like_count}")
