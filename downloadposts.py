from instagrapi import Client

# Initialize the client
cl = Client()

# Login with your credentials
cl.login("username", "password")

# Fetch liked posts
liked_posts = cl.liked_medias(amount=10)  # Adjust the amount as needed

# Print details of liked posts
for post in liked_posts:
    print(f"Post ID: {post.pk}")
    print(f"Caption: {post.caption_text}")
    print(f"URL: https://www.instagram.com/p/{post.code}/")

    cl.photo_download(post.pk, folder="folder_path")
    print("Downloaded successfully!\n")
