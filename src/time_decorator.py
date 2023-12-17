import time


# calculate the time taken and convert to readable format
def calc_time_taken(start_time, stop_time):
    # time_diff is the time taken in seconds
    time_diff = stop_time - start_time
    return time_diff


# decorator to record the time before and after running the game
# time.time to get the current time as a float
# to be called when play_game is ran
def record_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()

        return calc_time_taken(start_time, stop_time)

    return wrapper


def convert_secs_to_hhmmss(seconds: int):
    hh = str(int(seconds // 3600))
    remaining_seconds = seconds % 3600
    mm = str(int(remaining_seconds // 60))
    ss = str(int(remaining_seconds % 60))

    if len(hh) == 1:
        hh = "0" + hh
    if len(mm) == 1:
        mm = "0" + mm
    if len(ss) == 1:
        ss = "0" + ss

    return f'{hh}:{mm}:{ss}'

# This function was created but not used, it is the inverse of the function convert_secs_to_hhmss
# def convert_hhmmss_to_seconds(hhmmss):
#     hh, mm, ss = hhmmss.split(':')
#     seconds = int(hh) * 3600 + int(mm) * 60 + int(ss)
#     return seconds
