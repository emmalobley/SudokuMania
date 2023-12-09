__author__ = 'Gwen'


import time

# global variables to exist outside of functions
start_time = 0
stop_time = 0


# calculate the time taken and convert to readable format
# need to rework minutes as over an hour will show 61, 62, 63 etc
def calc_time_taken():
    if start_time:
        time_taken = stop_time - start_time
        minutes = int(time_taken // 60)  # result is in seconds ~ get mins by floor divide # integer to remove decimal
        seconds = int(time_taken % 60)  # get remainder of seconds by using modulo
        hours = int(minutes // 60)  # get hours by floor dividing minutes
        minutes = minutes % 60  # go over the minutes with a modulo of 60 to make sure the minutes appear over 60
        formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"  # format time :02 to pad w/ zeros and ensure 2 digits
        print(f"Time taken (hh:mm:ss): {formatted_time}")


# decorator to record the time at the start of the game
# time.time to get the current time as a float
# to be called when new board fetched
def record_start_time(func):
    def wrapper(*args, **kwargs):
        global start_time
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"Sudoku started at {time.ctime(start_time)}")
        return result
    return wrapper

# decorator to record the time the game ends and calls the calculate time function
# to be called after solution checked and games finished


def record_stop_time(func):
    def wrapper(*args, **kwargs):
        global stop_time
        stop_time = time.time()
        result = func(*args, **kwargs)
        print(f"Sudoku stopped at {time.ctime(stop_time)}")
        calc_time_taken()
        return result

    return wrapper


# functions below to simulate the game starting and the game stopping for testing

@record_start_time
def start_game():
    print("start")


@record_stop_time
def stop_game():
    print("stop")


start_game()
time.sleep(6)  # insert time in seconds here to test
stop_game()


# testtime in seconds # 3600 = 1hr # 5400 = 1h30m # 7200 = 2h
# tests the calc time function works in the hour+ ranges without waiting for hours


testtime = 5025.0000000345356
minutesTest = int(testtime // 60)
secondsTest = int(testtime % 60)
hoursTest = int(minutesTest // 60)

minutesTest = minutesTest % 60

formatted_timeTest = f"{hoursTest:02}:{minutesTest:02}:{secondsTest:02}"
print(f"Time taken (hh:mm:ss): {formatted_timeTest} (test)")
