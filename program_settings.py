# Do not change the keys (left side of the colon), only change the values (right side of the colon)

reddit_settings = {
    # Paths
    "subreddits_file_path": "subreddits.txt",  # Path to the file that contains the subreddits, each line should be a subreddit name, e.g. "AskReddit"
    "post_list_file_path": "post_list.txt",  # Path to the file that contains the posts that have been selected before

    # Parameters
    "is_top_post": True,  # If True, selects a post from the top posts of the subreddit, if False, selects a post from the hot posts of the subreddit
    "post_limit": 50,  # Should not be smaller than 1
    "time_filter": "all",  # Can be one of "all", "day", "hour", "month", "week", "year"

    # Example
    # "is_top_post": True,
    # "post_limit": 50,
    # "time_filter": "all",
    # Selects a random subreddit from the subreddits.txt, then selects a random post from the top 50 posts of the subreddit in all time.
}

program_settings = {
    "has_debug": True,  # If True, prints debug messages
}
