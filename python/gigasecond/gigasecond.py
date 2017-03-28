import time;

def add_gigasecond(time_of_birth):
    secs = time.mktime( time_of_birth )
    sec_of_gigaversary = secs + 1000000000
    gigaversary = time.asctime(time.gmtime(sec_of_gigaversary))
    return "Your gigaversary will fall on (or fell on) %s" % gigaversary


add_gigasecond((1993, 3, 22, 12, 3, 38, 0, 81, -1))
