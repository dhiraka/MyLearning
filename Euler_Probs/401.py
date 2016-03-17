# The divisors of 6 are 1, 2, 3 and 6.
# The sum of the squares of these numbers is 1 + 4 + 9 + 36 = 50.

# Let sigma2(n) represent the sum of the squares of the divisors of n.
# Thus sigma2(6) = 50.
# Let SIGMA2 represent the summatory function of sigma2, that is
# SIGMA2(n) sigma2(i) for i = 1 to n.
# The first 6 values of SIGMA2 are:
#     1, 6, 16, 37, 63 and 113.

# 1, 5, 10,

# Find SIGMA2(1015) modulo 109.


def rwh_primes1(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n / 2)
    for i in xrange(3, int(n**0.5) + 1, 2):
        if sieve[i / 2]:
            sieve[i * i / 2::i] = [False] * ((n - i * i - 1) / (2 * i) + 1)
    return [2] + [2 * i + 1 for i in xrange(1, n / 2) if sieve[i]]


def factorize(n, primes):
    factors = []
    for p in primes:
        if p * p > n:
            break
    i = 0
    while n % p == 0:
        n //= p
        i += 1
    if i > 0:
        factors.append((p, i))
    if n > 1:
        factors.append((n, 1))

    return factors


def divisors(factors):
    div = [1]
    for (p, r) in factors:
        div = [d * p**e for d in div for e in range(r + 1)]
    return div


def sigma2(n):
    # sum of squares of all factors of n
    sum = 0
    primes = rwh_primes1(n)
    divs = divisors(factorize(n, primes))
    for divisor in divs:
        sum += divisor**2
    return sum


def SIGMA2(n):
    sum = 0
    for x in range(1, n + 1):
        sum += sigma2(x)
    return sum
    # map(lambda x: sum += sigma2())

print SIGMA2(1)
print SIGMA2(2)
print SIGMA2(3)
print SIGMA2(4)
print SIGMA2(5)
print SIGMA2(6)
