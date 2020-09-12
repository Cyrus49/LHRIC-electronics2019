import math
from calc_corer_time_2 import *
from slal2turn import *
from calc_straight_time import *
from calc_long_force import *
from f_torque import *

#List of alterable parameters

WB = 63.5/12 #Wheelbase (ft)
t_f = 49/12 #front track (ft)
t_r = 47/12 #rear track (ft)
W = 560 #Weight (lbs)
hcg = 11/12 #Height of the CG (ft)
hcp = 36/12 #Height of the center of pressure
weight_dist = .53 #Weight distribution rearward
cp_dist = .52 #Center of pressure distribution rearward
a_brake = 1 * 32.2 #braking acceleration (ft/s2)
cl = .067 #Lift force (lbs of lift / velocity^2) (velocity is ft/s)
cd = cl/2 #Drag force as a percentage of lift force
target_cf = 1.4/2.447 #The approximate coefficient of friction of the road surface
final = 3 #final drive ratio

#The engine parameters must be changed in the ftorque function!!!

m=0

Ttotal = []

#xaxis = 0:.025:.1
cl = 0
while cl <= .1:
    cd = cl/2
    W = 560 + cl*300
    m=m+1

    #calculate maximum corner speeds before laptime  
    v_0 = 1000
    v_f = 1000

    R = 14
    degrees = 45
    T1 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 

    R = 14
    degrees = 45
    T3 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 

    R = 6
    degrees = 90
    T5 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 

    R = 9
    degrees = 139
    T7 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 

    R = 12
    degrees = 40
    T9 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 

    R = 6
    degrees = 90
    T10 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 

    R = 12
    degrees = 60
    T12 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 

    #Slalom 13
    Sl = slal2turn(t_f, 30, 90)
    R = Sl[0]
    degrees = Sl[1]
    T13 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 24
    degrees = 113
    T15 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 24
    degrees = 143
    T17 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 24
    degrees = 143
    T18 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 6
    degrees = 90
    T20 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 6
    degrees = 90
    T21 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 6
    degrees = 90
    T23 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 6
    degrees = 90
    T24 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 54
    degrees = 57
    T26 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 54
    degrees = 57
    T27 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    #Slalom 28
    Sl = slal2turn(t_f, 40, 240)
    R = Sl[0]
    degrees = Sl[1]
    T28 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 6
    degrees = 90
    T30 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 6
    degrees = 90
    T31 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 6
    degrees = 90
    T33 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 6
    degrees = 90
    T34 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 6
    degrees = 90
    T36 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 6
    degrees = 90
    T37 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 34
    degrees = 123
    T39 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 24
    degrees = 123
    T40 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 14
    degrees = 146
    T42 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 46
    degrees = 90
    T44 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 56
    degrees = 123
    T45 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 6
    degrees = 90
    T46 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 6
    degrees = 90
    T47 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 6
    degrees = 90
    T49 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 6
    degrees = 90
    T50 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    #Slalom 52
    Sl = slal2turn(t_f, 30, 150)
    R = Sl[0]
    degrees = Sl[1]
    T52 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 6
    degrees = 90
    T54 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 6
    degrees = 90
    T55 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 14
    degrees = 68
    T57 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 34
    degrees = 118
    T58 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    R = 14
    degrees = 50
    T60 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

    #Begin Component Chain

    #61
    d_total = 80
    v_0 = T60[2]
    v_f = T1[2]
    S61 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal.append(S61[0])

    #1
    v_0 = S61[2]
    v_f = 1000

    R = 14
    degrees = 45
    T1 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 
    Ttotal[m-1]+= T1[1]

    #2
    d_total = 27
    v_0 = T1[2]
    v_f = T3[2]
    S2 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal[m-1]+= S2[0]

    #3
    v_0 = S2[2]
    v_f = 1000

    R = 14
    degrees = 45
    T3 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 
    Ttotal[m-1]+= T3[1]

    #4
    d_total = 20
    v_0 = T3[2]
    v_f = T5[2]
    S4 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal[m-1]+= S4[0]

    #5
    v_0 = S4[2]
    v_f = 1000

    R = 6
    degrees = 90
    T5 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 
    Ttotal[m-1]+= T5[1]

    #6
    d_total = 21
    v_0 = T5[2]
    v_f = T7[2]
    S6 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal[m-1]+= S6[0]

    #7
    v_0 = S6[2]
    v_f = 1000

    R = 9
    degrees = 139
    T7 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 

    #8
    d_total = 64
    v_0 = T7[2]
    v_f = T9[2]
    S8 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal[m-1]+= S8[0]

    #9
    v_0 = S8[2]
    v_f = T10[2]

    R = 12
    degrees = 40
    T9 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 

    #10
    v_0 = T9[2]
    v_f = 1000

    R = 6
    degrees = 90
    T10 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T10[1]

    #11
    d_total = 25
    v_0 = T10[2]
    v_f = T12[2]
    S11 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal[m-1]+= S11[0]

    #12
    v_0 = S11[2]
    v_f = T13[2]

    R = 12
    degrees = 60
    T12 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T12[1]

    #Slalom 13
    v_0 = T12[2]
    v_f = 1000

    Sl = slal2turn(t_f, 30, 90)
    R = Sl[0]
    degrees = Sl[1]
    T13 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T13[1]

    #14
    d_total = 26
    v_0 = T13[2]
    v_f = T15[2]
    S14 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal[m-1]+= S14[0]

    #15
    v_0 = S14[2]
    v_f = 1000

    R = 24
    degrees = 13
    T15 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T15[1]

    #16
    d_total = 80
    v_0 = T15[2]
    v_f = T17[2]
    S16 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal[m-1]+= S16[0]

    #17
    v_0 = S16[2]
    v_f = T18[2]

    R = 24
    degrees = 143
    T17 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T17[1]

    #18
    v_0 = T17[2]
    v_f = 1000

    R = 24
    degrees = 143
    T18 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T18[1]

    #19
    d_total = 138
    v_0 = T18[2]
    v_f = T20[2]
    S19 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal[m-1]+= S19[0]

    #21
    v_0 = S19[2]
    v_f = 1000

    R = 6
    degrees = 90
    T21 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T21[1]

    #22
    d_total = 31
    v_0 = T21[2]
    v_f = T23[2]
    S22 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal[m-1]+= S22[0]

    #23
    v_0 = S22[2]
    v_f = T24[2]

    R = 6
    degrees = 90
    T23 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T23[1]

    #24
    v_0 = T23[2]
    v_f = 1000

    R = 6
    degrees = 90
    T24 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T24[1]

    #25
    d_total = 30
    v_0 = T24[2]
    v_f = T26[2]
    S25 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal[m-1]+= S25[0]

    #26
    v_0 = S25[2]
    v_f = T27[2]

    R = 54
    degrees = 57
    T26 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T26[1]

    #27
    v_0 = T26[2]
    v_f = T28[2]

    R = 54
    degrees = 57
    T27 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T27[1]

    #Slalom 28
    v_0 = T27[2]
    v_f = 1000

    Sl = slal2turn(t_f, 40, 240)
    R = Sl[0]
    degrees = Sl[1]
    T28 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T28[1]

    #29
    d_total = 48
    v_0 = T28[2]
    v_f = T30[2]
    S29 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal[m-1]+= S29[0]

    #30
    v_0 = S29[2]
    v_f = T31[2]

    R = 6
    degrees = 90
    T30 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T30[1]

    #31
    v_0 = T30[2]
    v_f = 1000

    R = 6
    degrees = 90
    T31 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T31[1]

    #32
    d_total = 56
    v_0 = T31[2]
    v_f = T33[2]
    S32 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal[m-1]+= S32[0]

    #33
    v_0 = S32[2]
    v_f = T34[2]

    R = 6
    degrees = 90
    T33 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T33[1]

    #34
    v_0 = T33[2]
    v_f = 1000

    R = 6
    degrees = 90
    T34 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T34[1]

    #35
    d_total = 56
    v_0 = T34[2]
    v_f = T36[2]
    S35 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal[m-1]+= S35[0]

    #36
    v_0 = S35[2]
    v_f = T37[2]

    R = 6
    degrees = 90
    T36 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T36[1]

    #37
    v_0 = T36[2]
    v_f = 1000

    R = 6
    degrees = 90
    T37 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T37[1]

    #38
    d_total = 68
    v_0 = T37[2]
    v_f = T39[2]
    S38 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal[m-1]+= S38[0]

    #39
    v_0 = S38[2]
    v_f = T40[2]

    R = 34
    degrees = 123
    T39 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T39[1]

    #40
    v_0 = T39[2]
    v_f = 1000

    R = 24
    degrees = 123
    T40 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T40[1]

    #41
    d_total = 100
    v_0 = T40[2]
    v_f = T42[2]
    S41 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal[m-1]+= S41[0]

    #42
    v_0 = S41[2]
    v_f = 1000

    R = 14
    degrees = 146
    T42 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T42[1]

    #43
    d_total = 21
    v_0 = T42[2]
    v_f = T44[2]
    S43 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal[m-1]+= S43[0]

    #44
    v_0 = S43[2]
    v_f = T45[2]

    R = 46
    degrees = 90
    T44 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T44[1]

    #45
    v_0 = T44[2]
    v_f = T46[2]

    R = 56
    degrees = 123
    T45 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T45[1]

    #46
    v_0 = T45[2]
    v_f = T47[2]

    R = 6
    degrees = 90
    T46 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T46[1]

    #47
    v_0 = T46[2]
    v_f = 1000

    R = 6
    degrees = 90
    T47 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T47[1]

    #48
    d_total = 26
    v_0 = T47[2]
    v_f = T49[2]
    S48 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal[m-1]+= S48[0]

    #49
    v_0 = S48[2]
    v_f = T50[2]

    R = 6
    degrees = 90
    T49 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T49[1]

    #50
    v_0 = T49[2]
    v_f = 1000

    R = 6
    degrees = 90
    T50 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T50[1]

    #51
    d_total = 200
    v_0 = T50[2]
    v_f = T52[2]
    S51 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal[m-1]+= S51[0]

    #Slalom 52
    v_0 = S51[2]
    v_f = 1000

    Sl = slal2turn(t_f, 30, 150)
    R = Sl[0]
    degrees = Sl[1]
    T52 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T52[1]

    #53
    d_total = 200
    v_0 = T52[2]
    v_f = T54[2]
    S53 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal[m-1]+= S53[0]

    #54
    v_0 = S53[2]
    v_f = T55[2]

    R = 6
    degrees = 90
    T54 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T54[1]

    #55
    v_0 = T54[2]
    v_f = 1000

    R = 6
    degrees = 90
    T55 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T55[1]

    #56
    d_total = 30
    v_0 = T55[2]
    v_f = T57[2]
    S56 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal[m-1]+= S56[0]

    #57
    v_0 = S56[2]
    v_f = T58[2]

    R = 14
    degrees = 68
    T57 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T57[1]

    #58
    v_0 = T57[2]
    v_f = 1000

    R = 34
    degrees = 118
    T58 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T58[1]


    #59
    d_total = 20
    v_0 = T58[2]
    v_f = T60[2]
    S59 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
    Ttotal[m-1]+= S59[0]

    #60
    v_0 = S59[2]
    v_f = 1000

    R = 14
    degrees = 50
    T60 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
    Ttotal[m-1]+= T60[1]

    #Ttotal[m-1]
    print(Ttotal)
    cl+=.025

#plot(xaxis,Ttotal)


