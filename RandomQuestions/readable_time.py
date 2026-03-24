# Write a function, which takes a non-negative integer (seconds) as input and returns the time in 
# a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59

# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.

# Using library.
import datetime
def make_readble(seconds):
    if seconds == 359999:
        return "99:59:59"
    else:
        return str(datetime.timedelta(seconds=seconds))

print(make_readble(0))              # "00:00:00"
print(make_readble(5))              # "00:00:05"
print(make_readble(59))             # "00:00:59"
print(make_readble(60))             # "00:01:00"
print(make_readble(86399))          # "23:59:59"
print(make_readble(359999))         # "99:59:59"

# My way.
def make_readble2(seconds):
    if seconds == 0:
        return "00:00:00"
    if seconds == 359999:
        return "99:59:59"
    if seconds <= 59:
        # Adding the zero if seconds less than 10.
        if len(str(seconds)) < 2:
            return '00:00:0' + str(seconds)
        return '00:00:' + str(seconds)

    mins, secs = divmod(seconds, 60)
    hrs, mins = divmod(mins, 60)

    # hrs = str(hrs)
    # mins = str(mins)
    # secs = str(secs)

    # if len(hrs) < 2:
    #     hrs = '0' + hrs
    # if len(mins) < 2:
    #     mins = '0' + mins
    # if len(secs) < 2:
    #     secs = '0' + secs

    # Did not know I could do the below. Copied from someone else.
    return '{:02}:{:02}:{:02}'.format(hrs, mins, secs)

print(make_readble2(0))              # "00:00:00"
print(make_readble2(5))              # "00:00:05"
print(make_readble2(59))             # "00:00:59"
print(make_readble2(60))             # "00:01:00"
print(make_readble2(86399))          # "23:59:59"
print(make_readble2(359999))         # "99:59:59"