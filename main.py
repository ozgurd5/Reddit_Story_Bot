from dotenv import dotenv_values
import praw

config = dotenv_values(".env")
client_id = config.get('REDDIT_CLIENT_ID')
client_secret = config.get('REDDIT_CLIENT_SECRET')
user_agent = config.get('REDDIT_USER_AGENT')

if not client_id or not client_secret or not user_agent:
    raise ValueError("Please set the environment variables for Reddit API credentials")

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

subreddit_name = 'python'
subreddit = reddit.subreddit(subreddit_name)

top_post = next(subreddit.top(limit=1))

print(f"Title: {top_post.title}")
print(f"Text: {top_post.selftext}")
