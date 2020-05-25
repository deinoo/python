#Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)


def make_readable(value):
    print (value)
    hours = int(value/3600)
    minutes = int((value - hours * 3600)/60)
    seconds = int (value - hours*3600 - minutes *60)

    if len(str(hours))==1:
        hours = str('0'+ str(hours))

    if len(str(minutes))==1:
        minutes = str('0'+str(minutes))

    if len(str(seconds))==1:
        seconds = str('0'+str(seconds))
    return ('{}:{}:{}'.format(hours,minutes,seconds))