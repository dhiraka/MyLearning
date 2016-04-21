# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"


def solution(E, L):
    bill = 2
    start_time = E.split(':')
    end_time = L.split(':')
    start_hr = int(start_time[0])
    start_min = int(start_time[1])
    end_hr = int(end_time[0])
    end_min = int(end_time[1])

    start_time_in_min = start_hr * 60 + start_min
    end_time_in_min = end_hr * 60 + end_min

    time_diff = end_time_in_min - start_time_in_min
    if time_diff > 60:
        time_diff -= 60
        bill += 3
        bill += (time_diff / 60) * 4
        if time_diff % 60 > 0:
            bill += 4
    else:
        bill += 3

    return bill


print solution("10:00", "13:21")
