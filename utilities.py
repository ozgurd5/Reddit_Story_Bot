from program_settings import program_settings


def debug_print(*args):
    if program_settings["has_debug"]:
        print(*args)
