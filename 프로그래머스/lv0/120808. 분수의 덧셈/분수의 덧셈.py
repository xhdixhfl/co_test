import fractions
def solution(numer1, denom1, numer2, denom2):
    a = (numer1 * denom2) + (numer2 * denom1)
    b = denom1 * denom2
    c = fractions.Fraction(a,b)
    answer = [c.numerator,c.denominator]
    return answer