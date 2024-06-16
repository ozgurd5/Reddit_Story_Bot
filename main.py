from dotenv import dotenv_values
import praw
import random
from program_settings import program_settings


def main():
    reddit = init_reddit()
    subreddit_name = get_random_subreddit()
    subreddit = reddit.subreddit(subreddit_name)

    random_post_index = random.choice(range(1, program_settings["post_limit"]))
    top_posts = list(subreddit.top(time_filter=program_settings["time_filter"], limit=random_post_index))
    selected_post = top_posts[random_post_index - 1]  # Indexing starts from 0 in list but 1 in Reddit

    debug_print(f"Fetching {random_post_index}th post from r/{subreddit_name}")
    debug_print(f"Title: {selected_post.title}")
    debug_print(f"Text: {selected_post.selftext}")


def init_reddit():
    env = dotenv_values(".env")
    client_id = env.get('REDDIT_CLIENT_ID')
    client_secret = env.get('REDDIT_CLIENT_SECRET')
    user_agent = env.get('REDDIT_USER_AGENT')

    if not client_id or not client_secret or not user_agent:
        raise ValueError("Please set the environment variables for Reddit API credentials")

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )

    return reddit


def get_random_subreddit():
    with open("subreddits.txt") as subreddits:
        subreddits = subreddits.readlines()
        return random.choice(subreddits).strip()


def debug_print(*args):
    if program_settings["has_debug"]:
        print(*args)


main()
