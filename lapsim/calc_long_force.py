# 1996 Pacejka R25B_13 Longitudinal Force
# input normal load on rear track, gives longitudinal force of rear track
import math

#Cyrus
#I have no clue what's happening here, but I believe dynamics is currently working on something similar to this for us

def calc_long_force(a):

    #fz=normal load, lbs
    fz = a/2*4.448

    #k=slip ratio
    k=.25

    #coefficients

    fz0 = 663.94728
    pcx1 = 1.35
    pdx1 = 2.5507
    pdx2 = -0.23408
    pex1 = .40327
    pex2 = 1.1649
    pex3 = -1.0858
    pex4 = .8363
    pkx1 = 64.3473
    pkx2 = 0.000013
    pkx3 = 0.04864
    phx1 = 0.005464
    phx2 = -0.003318
    pvx1 = -0.15012
    pvx2 = 0.0905
        
    #pacejka equations

    dfz = (fz - fz0) / fz0
    svx = fz * (pvx1 + pvx2 * dfz)
    shx = phx1 + phx2 * dfz
    cx = pcx1
    ux = pdx1 + pdx2 * dfz
    dx = ux * fz
    kxk = fz * (pkx1 + pkx2 * dfz) * math.exp(-pkx3 * dfz)
    bx = kxk / (cx * dx)
    kx = k + shx

    if kx < 0:
        sign_kx = -1
    elif kx == 0:
        sign_kx = 0
    else:
        sign_kx = 1

    ex = (pex1 + pex2 * dfz + pex3 * dfz ** 2) * (1 - pex4 * sign_kx)
    hfx0 = dx * math.sin(cx * math.atan(bx * kx - ex * (bx * kx - math.atan(bx * kx)))) + svx
                
    long_force = 2*hfx0/4.448
    return long_force
                
print(calc_long_force(15))