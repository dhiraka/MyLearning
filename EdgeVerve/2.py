# positions = [3, 2, 6, 7]
# l = 10
positions = [7, 11, 12, 7, 13, 176, 23, 191]
l = 214


# def get_min_time(positions, l):
#     return max(map(lambda x: min(x, l - x), positions))

# min_time = get_min_time(positions, l)


# def get_max_time(positions, l):
#     roach_pos_one_end = min(positions)
#     roach_pos_other_end = max(positions)
#     dif_bet_end_roaches = abs(roach_pos_one_end - roach_pos_other_end)
#     first_roach_time = roach_pos_one_end + dif_bet_end_roaches
#     second_roach_time = (l - roach_pos_other_end) + dif_bet_end_roaches
#     return max(first_roach_time, second_roach_time)


# max_time = get_max_time(positions, l)


# print str(min_time) + " " + str(max_time)


def get_min_time(positions, l):
    return max(map(lambda x: min(x, l - x), positions))

min_time = get_min_time(positions, l)
print min_time


def get_max_time(positions, l):
    roach_pos_one_end = min(positions)
    roach_pos_other_end = max(positions)
    dif_bet_end_roaches = abs(roach_pos_one_end - roach_pos_other_end)
    first_roach_time = roach_pos_one_end + dif_bet_end_roaches
    second_roach_time = (l - roach_pos_other_end) + dif_bet_end_roaches
    return max(first_roach_time, second_roach_time)

max_time = get_max_time(positions, l)


print str(min_time) + " " + str(max_time)
