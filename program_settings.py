import os

# Do not change the keys (left side of the colon), only change the values (right side of the colon)

program_settings = {
    "has_debug": True,  # If True, prints debug messages
    "gameplay_footage_path": "gameplay_footage",  # Path to the folder that contains the gameplay footage
}

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

youtube_downloader_settings = {
    # Paths
    "youtube_video_list_path": "youtube_videos_to_download.txt",  # Path to the file that contains the YouTube video URLs, each line should be a video URL
    "youtube_download_path": os.getcwd() + "/youtube_downloads/"  # Path to the file that the YouTube downloader program will save the video file
}

text_to_speech_settings = {
    # Paths
    "output_sound_file_path": "output_sound.mp3",  # Path to the file that the text-to-speech program will save the sound file

    # Parameters
    "is_tiktok": False,  # If True, uses TikTok text-to-speech, if False, uses Google text-to-speech
    "has_random_voice": True,  # If True, selects a random voice from the random_tiktok_voice_pool

    # Google Parameters
    "google_voice": "com",  # com for American English, co.uk for British English, com.au for Australian English, co.in for Indian English

    # Tiktok Parameters
    "tiktok_voice": "en_us_001",  # Check the available voices in the available_tiktok_voices
}

random_tiktok_voice_pool = {
    # Fill this with the voices you want to use in the random voice selection

    'en_us_001',                  # English US - Female (Int. 1)
    'en_us_002',                  # English US - Female (Int. 2)
    'en_us_006',                  # English US - Male 1
    'en_us_007',                  # English US - Male 2
    'en_us_009',                  # English US - Male 3
    'en_us_010',                  # English US - Male 4
}

random_google_voice_pool = {
    # Fill this with the voices you want to use in the random voice selection

    'com',                        # American English
    'co.uk',                      # British English
    'com.au',                     # Australian English
    'co.in',                      # Indian English
}

# Check for samples: https://github.com/oscie57/tiktok-voice/tree/main/samples
available_tiktok_voices = {
    # DISNEY VOICES
    'en_us_ghostface',            # Ghost Face
    'en_us_chewbacca',            # Chewbacca
    'en_us_c3po',                 # C3PO
    'en_us_stitch',               # Stitch
    'en_us_stormtrooper',         # Stormtrooper
    'en_us_rocket',               # Rocket

    # ENGLISH VOICES
    'en_au_001',                  # English AU - Female
    'en_au_002',                  # English AU - Male
    'en_uk_001',                  # English UK - Male 1
    'en_uk_003',                  # English UK - Male 2
    'en_us_001',                  # English US - Female (Int. 1)
    'en_us_002',                  # English US - Female (Int. 2)
    'en_us_006',                  # English US - Male 1
    'en_us_007',                  # English US - Male 2
    'en_us_009',                  # English US - Male 3
    'en_us_010',                  # English US - Male 4

    # EUROPE VOICES
    'fr_001',                     # French - Male 1
    'fr_002',                     # French - Male 2
    'de_001',                     # German - Female
    'de_002',                     # German - Male
    'es_002',                     # Spanish - Male

    # AMERICA VOICES
    'es_mx_002',                  # Spanish MX - Male
    'br_001',                     # Portuguese BR - Female 1
    'br_003',                     # Portuguese BR - Female 2
    'br_004',                     # Portuguese BR - Female 3
    'br_005',                     # Portuguese BR - Male

    # ASIA VOICES
    'id_001',                     # Indonesian - Female
    'jp_001',                     # Japanese - Female 1
    'jp_003',                     # Japanese - Female 2
    'jp_005',                     # Japanese - Female 3
    'jp_006',                     # Japanese - Male
    'kr_002',                     # Korean - Male 1
    'kr_003',                     # Korean - Female
    'kr_004',                     # Korean - Male 2

    # SINGING VOICES
    'en_female_f08_salut_damour'  # Alto
    'en_male_m03_lobby'           # Tenor
    'en_female_f08_warmy_breeze'  # Warmy Breeze
    'en_male_m03_sunshine_soon'   # Sunshine Soon

    # OTHER
    'en_male_narration'           # narrator
    'en_male_funny'               # wacky
    'en_female_emotional'         # peaceful
}