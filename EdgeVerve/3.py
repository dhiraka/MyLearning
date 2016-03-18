# Enter your code here. Read input from STDIN. Print output to STDOUT


# input_arr = raw_input().split()

# n = no_of_participants = input_arr[0]
# ids = input_arr[1:]
# n = 2
# ids = [90980967, 84959483]

n = 3
ids = [86632431, 74363749, 92938245]


def get_divisor_with_unique_remainders(ids, n):
    no_of_ids = len(ids)
    i = 1
    while no_of_ids != len(set(map(lambda x: x % i, ids))):
        i += 1
    return i

print get_divisor_with_unique_remainders(ids, n)
