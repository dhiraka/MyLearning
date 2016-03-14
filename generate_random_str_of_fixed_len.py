import random
import string
# An attempt to see how long it takes for a random function to generate
# a particular string
given_str = "my name is radhika and i am a legend"
# print len(gen_str)
# ''.join(random.choice(string.ascii_uppercase + string.digits)
#         for _ in range(N))


def id_generator(size=36, chars=string.ascii_lowercase + ' '):
    return ''.join(random.choice(chars) for _ in range(size))

str_gen = ""
while str_gen != given_str:
    str_gen = id_generator()
    print str_gen

print str_gen
