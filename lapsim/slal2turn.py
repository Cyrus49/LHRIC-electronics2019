import math
def slal2turn(T, spacing, length):

    r = T/4 + spacing**2/(4*T)
    N = length/spacing
    d = N*(180/math.pi)*2*math.atan((spacing/2)/(r-T/2))

    result = [r,d]

    return result