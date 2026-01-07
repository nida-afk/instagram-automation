# Instagram Post Management Tools

A collection of Python scripts for interacting with Instagram using the `instagrapi` library. These tools allow you to download, analyze, and manage Instagram posts.

---

## Table of Contents
1. [downloadposts.py](#downloadpostspy)
2. [mostlikedpostsinfeed.py](#mostlikedpostsinfeedpy)
3. [batchbookmarking.py](#batchbookmarkingpy)
4. [sortpostsinhashtag.py](#sortpostsinhashtagpy)

---

## downloadposts.py

### Title
Instagram Liked Posts Downloader

### Description
This script logs into an Instagram account and downloads the user's liked posts to a local folder. It retrieves up to 1000 liked posts and downloads each post with its metadata (post ID, caption, and URL).

### Usage
```python
python downloadposts.py
```

### Details
- **Authentication**: Logs in using Instagram credentials
- **Functionality**:
  - Fetches up to 1000 liked posts from the authenticated user's account
  - Displays post ID, caption text, and post URL
  - Downloads each post to a specified folder
- **Output**: Downloaded photos saved to `folder_path` directory
- **Note**: The `folder_path` should be replaced with an actual directory path before running

---

## mostlikedpostsinfeed.py

### Title
Top Liked Posts Analyzer

### Description
This script fetches the authenticated user's liked posts, sorts them by engagement (number of likes), and displays information about the top 50 most-liked posts. Useful for identifying trending and popular content.

### Usage
```python
python mostlikedpostsinfeed.py
```

### Details
- **Authentication**: Logs in using Instagram credentials
- **Functionality**:
  - Fetches up to 3000 liked posts
  - Sorts all posts by like count in descending order
  - Filters and displays the top 50 posts
  - Shows post ID, caption, like count, and post URL
- **Output**: Console output with post details
- **Use Case**: Identify which posts received the most engagement from liked posts

---

## batchbookmarking.py

### Title
Bulk Liked Posts Saver

### Description
This script automates the process of saving liked posts to the user's Instagram save collection. It fetches all liked posts and adds them to saved posts while implementing rate limiting to avoid Instagram throttling.

### Usage
```python
python batchbookmarking.py
```

### Details
- **Authentication**: Logs in using Instagram credentials
- **Functionality**:
  - Fetches up to 2000 liked posts
  - Adds each post to the authenticated user's saved posts collection
  - Implements a 4-second delay between save operations to avoid rate limiting
  - Displays post ID, caption, and URL for each processed post
- **Output**: Console feedback confirming each post is added to saved posts
- **Rate Limiting**: 4-second delay between operations prevents API throttling
- **Use Case**: Bulk-save liked posts for offline access and organization

---

## sortpostsinhashtag.py

### Title
Target User Top Posts Extractor

### Description
This script fetches a specific user's posts (not your own), sorts them by popularity, and displays the top N most-liked posts from that user. Useful for analyzing other accounts' performance and most popular content.

### Usage
```python
python sortpostsinhashtag.py
```

### Details
- **Function**: `get_top_liked_posts(username, password, target_user, top_n=20)`
  - `username`: Instagram account username for authentication
  - `password`: Instagram account password
  - `target_user`: Username of the account to analyze (e.g., "dreamy.fantasys")
  - `top_n`: Number of top posts to retrieve (default: 20)

- **Functionality**:
  - Logs into Instagram with provided credentials
  - Retrieves up to 899 recent posts from the target user
  - Sorts posts by like count in descending order
  - Returns the top N posts as a list
  - Prints URLs and like counts of the top posts

- **Output**: Console display of URLs and like counts
  ```
  URL: https://www.instagram.com/p/{code}/, Likes: {count}
  ```
- **Current Configuration**:
  - Authenticating account
  - Target user: dreamy.fantasys
  - Top posts: 20
- **Use Case**: Analyze competitor accounts, identify trending content, benchmark against other creators

---

## General Requirements

All scripts require the `instagrapi` library:

```bash
pip install instagrapi
```

## Security Notes

⚠️ **Important**: These scripts contain hardcoded credentials. For production use:
- Store credentials in environment variables
- Use a `.env` file with `python-dotenv`
- Never commit credentials to version control
- Consider using Instagram's official API when available

## Rate Limiting

Instagram enforces rate limits. The `sortpostsinhashtag.py` script includes a 4-second delay between operations. For high-volume operations, consider:
- Increasing delay intervals
- Adding random delays using `random.uniform()`
- Implementing exponential backoff for retries

---

## Disclaimer

These tools interact with Instagram's unofficial API through `instagrapi`. Instagram may change its API structure or terms of service. Use responsibly and in compliance with Instagram's terms of service.

