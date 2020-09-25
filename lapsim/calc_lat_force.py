import math
# 1996 Pacejka R25B_13 Lateral Force
# input normal load on tire, slip angle, camber angle, gives lateral force
# on tire y axis

#positive alpha = positive force
#negative camber = "good" camber

#Cyrus
#I have no clue what's happening here, but I believe dynamics is currently working on something similar to this for us

def calc_lat_force(f_z, a, gamma):

    #fz- normal force
    #fz0 - 
    fz = f_z*4.448 #lb to N

    fz0 = 663.94 #N
    pcy1 = 1.377528
    pdy1 = 2.4860
    pdy2 = -.150167
    pdy3 = -1.88895
    pey1 = -.000043
    pey2 = .000007
    pey3 = -3683.9043
    pey4 = -15729.78
    pky1 = -114.08707
    pky2 = -3.621914
    pky3 = 2.51886
    phy1 = .002182
    phy2 = -.001398
    phy3 = -.119546
    pvy1 = .026184
    pvy2 = -.029205
    pvy3 = .034106
    pvy4 = .424675

    dfz = (fz-fz0)/fz0
    svy = fz*(pvy1+phy2*dfz+(pvy3+pvy4*dfz)*gamma)
    shy = phy1+phy2*dfz+phy3*gamma
    cy = pcy1
    uy = (pdy1+pdy2*dfz)*(1-pdy3*gamma**2)
    dy = uy*fz
    kya = pky1*fz0*math.sin(2*math.atan(fz/(pky2*fz0)))*(1-pky3*abs(gamma))
    by = kya/(cy*dy)
    ay = a+shy

    if ay < 0:
        sign_ay = -1
    elif ay == 0:
        sign_ay = 0
    else:
        sign_ay = 1

    ey = (pey1+pey2*dfz)*(1-(pey3+pey4*gamma))*sign_ay
    fy0 = -(dy*math.sin(cy*math.atan(by*ay-ey*(by*ay-math.atan(by*ay))))+svy)

    lat_force = fy0/4.448

    return lat_force

#print(calc_lat_force(.5,.5,.5))