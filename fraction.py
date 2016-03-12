def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction(object):
    """Fraction data type"""

    def __init__(self, num, den):
        super(Fraction, self).__init__()
        if not (isinstance(num, int) and isinstance(den, int)):
            raise ValueError('Num or Den is not an integer')
        gcd_in = gcd(num, den)
        self.num = num / gcd_in
        self.den = den / gcd_in

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __add__(self, otherfraction):

        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        gcd_nd = gcd(newnum, newden)
        return Fraction(newnum / gcd_nd, newden / gcd_nd)

    def __sub__(self, otherfraction):

        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        gcd_nd = gcd(newnum, newden)
        return Fraction(newnum / gcd_nd, newden / gcd_nd)

    def __mul__(self, otherfraction):

        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        gcd_nd = gcd(newnum, newden)
        return Fraction(newnum / gcd_nd, newden / gcd_nd)

    def __div__(self, otherfraction):

        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        gcd_nd = gcd(newnum, newden)
        return Fraction(newnum / gcd_nd, newden / gcd_nd)

    def __lt__(self, otherfraction):

        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        return newnum < 0

    def __le__(self, otherfraction):

        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        return newnum <= 0

    def __gt__(self, otherfraction):

        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        return newnum > 0

    def __ge__(self, otherfraction):

        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        return newnum >= 0

    def __ne__(self, otherfraction):

        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        return newnum != 0


x = Fraction(1, 2)
y = Fraction(2, 3)
print(x + y)
print(x == y)
print(x - y)
print(x * y)
print(x / y)
print(x < y)
print(x > y)
