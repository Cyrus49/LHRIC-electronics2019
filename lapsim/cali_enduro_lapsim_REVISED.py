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
W = 570 #Weight (lbs)
hcg = 11/12 #Height of the CG (ft)
hcp = 36/12 #Height of the center of pressure
weight_dist = .53 #Weight distribution rearward
cp_dist = .52 #Center of pressure distribution rearward
a_brake = 1 * 32.2 #braking acceleration (ft/s2)
cl = .0 #Lift force (lbs of lift / velocity^2) (velocity is ft/s)
cd = cl/2 #Drag force as a percentage of lift force
target_cf = 1.3/2.447 #The approximate coefficient of friction of the road surface
final = 3 #final drive ratio

#The engine parameters must be changed in the ftorque function!!!

m=0

#for final = 2.5:.5:4
    
    
m=m+1

#calculate maximum corner speeds before laptime  
v_0 = 1000
v_f = 1000

R = 1.0*58.6
degrees = 50.31
T1 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 

R = 1.0*41.6
degrees = 137.82
T3 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 

R = 1.0*40.5
degrees = 135.28
T4 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 

R = 1.0*73.1
degrees = 55.13
T5 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 

R = 1.0*52.3
degrees = 80
T7 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 

R = 1.0*36.2
degrees = 151
T8 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 

R = 1.0*38.9
degrees = 129
T9 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 

R = 1.0*44.9
degrees = 57.52
T10 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

#Slalom 12
Sl = slal2turn(t_f, 30, 90)
R = 1.0*Sl[0]
degrees = Sl[1]
T12 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)


R = 1.0*39.1
degrees = 54.88
T14 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

R = 1.0*54.7
degrees = 105
T15 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

R = 1.0*32.6
degrees = 115.58
T16 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

R = 1.0*114.4
degrees = 86.3
T17 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

R = 1.0*68.1
degrees = 89.53
T18 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

R = 1.0*25.8
degrees = 134.85
T19 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

R = 1.0*51.5
degrees = 155
T21 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

R = 1.0*53.3
degrees = 155
T22 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

R = 1.0*66
degrees = 47.31
T24 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

R = 1.0*27.4
degrees = 49.81
T26 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

R = 1.0*64.4
degrees = 85.15
T27 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

R = 1.0*97.4
degrees = 35.34
T28 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

R = 1.0*18
degrees = 30
T29 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

#Slalom 30
Sl = slal2turn(t_f, 40, 240)
R = 1.0*Sl[0]
degrees = Sl[1]
T30 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

R = 1.0*32.2
degrees = 65
T32 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

R = 1.0*67.4
degrees = 93
T34 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

R = 1.0*98.7
degrees = 28.6
T35 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

R = 1.0*74.5
degrees = 31.1
T37 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

R = 1.0*104.6
degrees = 31.1
T38 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

R = 1.0*24.4
degrees = 136.6
T40 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

R = 1.0*24.1
degrees = 136.6
T41 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

R = 1.0*44.8
degrees = 112
T43 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

R = 1.0*53.6
degrees = 60
T45 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)

#Begin Component Chain
Ttotal = [0] * 1000 #ADDED WHEN TRANSLATED TO PYTHON

Ttotal[m] = 0
Dcomp = 0

#1
v_0 = T45[2]
v_f = 1000

R = 1.0*58.6
degrees = 50.31
T1 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 
Ttotal[m] = Ttotal[m] + T1[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#2
d_total = 1.0*149.5
v_0 = T1[2]
v_f = T3[2]
S2 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
Ttotal[m] += S2[0]
Dcomp = Dcomp + d_total

#3
v_0 = S2[2]
v_f = T4[2]

R = 1.0*41.6
degrees = 137.82
T3 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 
Ttotal[m] += T3[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#4
v_0 = T3[2]
v_f = T5[2]

R = 1.0*40.5
degrees = 135.28
T4 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 
Ttotal[m] += T4[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#5
v_0 = T4[2]
v_f = 1000

R = 1.0*73.1
degrees = 55.13
T5 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 
Ttotal[m] += T5[0]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#6
d_total = 1.0*31.5
v_0 = T5[2]
v_f = T7[2]
S6 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
Ttotal[m] += S6[0]
Dcomp = Dcomp + d_total

#7
v_0 = S6[2]
v_f = T8[2]

R = 1.0*52.3
degrees = 80
T7 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f) 
Ttotal[m] += T7[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#8
v_0 = T7[2]
v_f = T9[2]

R = 1.0*36.2
degrees = 151.6
T8 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T8[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#9
v_0 = T8[2]
v_f = T10[2]

R = 1.0*38.9
degrees = 129
T9 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T9[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#10
v_0 = T9[2]
v_f = 1000

R = 1.0*44.9
degrees = 57.5
T10 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T10[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#11
d_total = 1.0*204.1
v_0 = T10[2]
v_f = T12[2]
S11 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
Ttotal[m] += S11[0]
Dcomp = Dcomp + d_total

#Slalom 12
v_0 = S11[2]
v_f = 1000

Sl = slal2turn(t_f, 30, 90)
R = 1.0*Sl[0]
degrees = Sl[1]
T12 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T12[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#13
d_total = 1.0*175.7
v_0 = T12[2]
v_f = T14[2]
S13 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
Ttotal[m] += S13[0]
Dcomp = Dcomp + d_total

#14
v_0 = S13[2]
v_f = T15[2]

R = 1.0*39.1
degrees = 54.88
T14 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T14[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#15
v_0 = T14[2]
v_f = T16[2]

R = 1.0*32.6
degrees = 115.6
T15 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T15[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#16
v_0 = T15[2]
v_f = T17[2]

R = 1.0*32.6
degrees = 115.6
T16 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T16[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#17
v_0 = T16[2]
v_f = T18[2]

R = 1.0*114.4
degrees = 86.33
T17 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T17[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#18
v_0 = T17[2]
v_f = T19[2]

R = 1.0*68.1
degrees = 89.53
T18 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T18[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#19
v_0 = T18[2]
v_f = 1000

R = 1.0*25.8
degrees = 134.85
T19 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T19[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#20
d_total = 1.0*52.4
v_0 = T19[2]
v_f = T21[2]
S20 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
Ttotal[m] += S20[0]
Dcomp = Dcomp + d_total

#21
v_0 = S20[2]
v_f = T22[2]

R = 1.0*51.5
degrees = 154.84
T21 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T21[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#22
v_0 = T21[2]
v_f = 1000

R = 1.0*53.3
degrees = 154.84
T22 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T22[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#23
d_total = 1.0*75.2
v_0 = T22[2]
v_f = T24[2]
S23 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
Ttotal[m] += S23[0]
Dcomp = Dcomp + d_total

#24
v_0 = S23[2]
v_f = 1000

R = 1.0*66
degrees = 47.31
T24 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T24[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#25
d_total = 1.0*18.8
v_0 = T24[2]
v_f = T26[2]
S25 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
Ttotal[m] += S25[0]
Dcomp = Dcomp + d_total

#26
v_0 = S25[2]
v_f = T27[2]

R = 1.0*27.4
degrees = 49.8
T26 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T26[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#27
v_0 = T26[2]
v_f = T28[2]

R = 1.0*64.4
degrees = 85.15
T27 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T27[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#28
v_0 = T27[2]
v_f = 1000

R = 1.0*97.4
degrees = 35.34
T28 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T28[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#29
d_total = 1.0*74.3
v_0 = T28[2]
v_f = T30[2]
S29 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
Ttotal[m] += S29[0]
Dcomp = Dcomp + d_total

#Slalom 30
v_0 = S29[2]
v_f = 1000

Sl = slal2turn(t_f, 40, 240)
R = 1.0*Sl[0]
degrees = Sl[1]
T30 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T30[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#31
d_total = 1.0*71.5
v_0 = T30[2]
v_f = T32[2]
S31 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
Ttotal[m] += S31[0]
Dcomp = Dcomp + d_total

#32
v_0 = S31[2]
v_f = 1000

R = 1.0*32.2
degrees = 64.76
T32 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T32[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#33
d_total = 1.0*39.7
v_0 = T32[2]
v_f = T34[2]
S33 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
Ttotal[m] += S33[0]
Dcomp = Dcomp + d_total

#34
v_0 = S33[2]
v_f = T35[2]

R = 1.0*67.4
degrees = 93.36
T34 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T34[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#35
v_0 = T34[2]
v_f = 1000

R = 1.0*98.7
degrees = 28.61
T35 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T35[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#36
d_total = 1.0*73.4
v_0 = T35[2]
v_f = T37[2]
S36 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
Ttotal[m] += S36[0]
Dcomp = Dcomp + d_total

#37
v_0 = S36[2]
v_f = T38[2]

R = 1.0*74.5
degrees = 31.1
T37 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T37[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#38
v_0 = T37[2]
v_f = 1000

R = 1.0*104.6
degrees = 31.1
T38 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T38[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#39
d_total = 1.0*17.6
v_0 = T38[2]
v_f = T40[2]
S39 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
Ttotal[m] += S39[0]
Dcomp = Dcomp + d_total

#40
v_0 = S39[2]
v_f = T41[2]

R = 1.0*24.4
degrees = 136.64
T40 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T40[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#41
v_0 = T40[2]
v_f = 1000

R = 1.0*24.1
degrees = 136.64
T41 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T41[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#42
d_total = 1.0*135.9
v_0 = T41[2]
v_f = T43[2]
S42 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
Ttotal[m] += S42[0]
Dcomp = Dcomp + d_total

#43
v_0 = S42[2]
v_f = 1000

R = 1.0*44.8
degrees = 112
T43 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T43[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360

#44
d_total = 1.0*77.7
v_0 = T43[2]
v_f = T45[2]
S44 = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)
Ttotal[m] += S44[0]
Dcomp = Dcomp + d_total

#45
v_0 = S44[2]
v_f = T1[2]

R = 1.0*53.6
degrees = 60.6
T45 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f)
Ttotal[m] += T45[1]
Dcomp = Dcomp + 2*math.pi*R*degrees/360


Dcomp = Dcomp*.0001894 #convert total distance to miles

Ttotal[m] = Ttotal[m]*.5/Dcomp #normalize time wrt distance
print(Dcomp)
print(Ttotal[1])
#end

#plot(Ttotal)
