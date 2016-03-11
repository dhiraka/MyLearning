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
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, otherfraction):

        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        gcd_nd = gcd(newnum, newden)
        return Fraction(newnum / gcd_nd, newden / gcd_nd)


x = Fraction(1, 2)
y = Fraction(2, 3)
print(x + y)
print(x == y)
