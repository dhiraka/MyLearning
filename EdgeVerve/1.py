# Enter your code here. Read input from STDIN. Print output to STDOUT
# input_arr = raw_input().split()

# cache_size = input_arr[0]
# sequence = input_arr[1:]

# Enter your code here. Read input from STDIN. Print output to STDOUT
# input_arr = raw_input().split()

# n = no_of_participants = input_arr[0]
# ids = input_arr[1:]

cache_size = 5
sequence = list("ABC!DEAF!B!")
print sequence
print len(sequence)

# ABC CDEAF DEAFB

# cache_size = 3
# sequence = "WXWYZ!YZWYX!XYXY!".split()

# WYZ WYX WXY

# cache_size = 5
# sequence = "EIEIO!".split()

# EIO

import datetime

tup_list = []

print_count = 0


def add_to_cache(s):
    # find the least recently used tuple and replace its value and time
    global tup_list
    if len(tup_list) < 5:
        tup_list.append((s, datetime.datetime.now()))
    else:
        matching_tup_list = [item for item in tup_list if s == item]
        if len(matching_tup_list) == 0:
            sorted_tup_list = sorted(tup_list, key=lambda x: x[1])
            for el in tup_list:
                if el[0] == sorted_tup_list[0][0]:
                    tup_list.remove(el)
                    tup_list.append((s, datetime.datetime.now()))
                    # el[0] = s
                    # el[1] = datetime.datetime.now()
        else:
            for el in tup_list:
                if el[0] == s:
                    tup_list.remove(el)
                    tup_list.append((s, datetime.datetime.now()))
                    # el[1] = datetime.datetime.now()


def print_cache_in_order():
    global print_count
    v = ""
    if print_count != 0:
        v += " "
    for el in tup_list:
        v += str(el[0])
    print_count += 1
    print v,


for j in sequence:
    if j != "!":
        add_to_cache(j)
    else:
        print_cache_in_order()
