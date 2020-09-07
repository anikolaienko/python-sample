class Fraction(object):
    def __init__(self, numer, denom, negative = False):
        self.numer = numer
        self.denom = denom
        self.neg = negative
    
    def __abs__(self):
        return Fraction(self.numer, self.denom)

    def __eq__(self, other):
        return  self.numer == other.numer \
            and self.denom == other.denom \
            and self.neg == other.neg

    def __repr__(self):
        return "Fraction(%s, %s, %s)" % (self.numer, self.denom, self.neg)
    
    def __str__(self):
        sign = "-" if self.neg else ""
        return sign + self.numer + "/" + self.denom
