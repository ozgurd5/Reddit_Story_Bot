from program_settings import program_settings
from datetime import datetime
import random


def debug_print(*args):
    if program_settings["has_debug"]:
        print(*args)


def init_random_seed():
    now = datetime.now()
    seed = int(f"{now.year}{now.month:02d}{now.day:02d}{now.hour:02d}{now.minute:02d}{now.second:02d}{now.microsecond:06}")
    debug_print("Setting seed for random number generator: ", seed)
    random.seed(seed)
