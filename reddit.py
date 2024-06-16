from utilities import debug_print, program_settings
from dotenv import dotenv_values
import praw
import random


def get_random_text_from_reddit():
    reddit = init_reddit()

    subreddits_to_check = get_subreddits()
    subreddit_amount = len(subreddits_to_check)

    while True:  # Loop to find a subreddit where not all posts have been selected
        subreddit_name = random.choice(subreddits_to_check)
        subreddit = reddit.subreddit(subreddit_name)

        post_find_flag = False
        indexes_to_select = list(range(1, program_settings["post_limit"] + 1))

        while True:  # Loop to find a post that is not selected before
            random_post_index = random.choice(indexes_to_select)
            top_posts = list(subreddit.top(time_filter=program_settings["time_filter"], limit=random_post_index))
            selected_post = top_posts[random_post_index - 1]  # Indexing starts from 0 in list but 1 in Reddit

            if not check_post_in_list(selected_post.url):
                post_find_flag = True
                break

            else:
                indexes_to_select.remove(random_post_index)

            if len(indexes_to_select) == 0:
                debug_print(f"All posts have been seen by given situation: r/{subreddit_name}, top {program_settings['post_limit']} posts in "
                            f"{program_settings['time_filter']}")
                break

        if post_find_flag:
            break

        subreddits_to_check.remove(subreddit_name)
        if len(subreddits_to_check) == 0:
            debug_print(f"All posts have been seen in all subreddits by given situation: top {program_settings['post_limit']} posts in "
                        f"{program_settings['time_filter']} from {subreddit_amount} subreddits")
            return

    add_post_to_list(selected_post.url)

    debug_print(f"Fetching {random_post_index}th post from r/{subreddit_name}")
    return selected_post.selftext


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


def get_subreddits():
    with open("subreddits.txt", 'r', encoding="utf-8-sig") as subreddits:
        return [line.strip() for line in subreddits.readlines()]


def add_post_to_list(selected_post):
    with open("post_list.txt", 'a', encoding="utf-8-sig") as post_list:
        post_list.write(selected_post + "\n")


def check_post_in_list(selected_post):
    with open("post_list.txt", 'r', encoding="utf-8-sig") as post_list:
        post_list = post_list.readlines()
        for post in post_list:
            if post == selected_post + "\n":
                return True
        return False
