from calc_corer_time_2 import *
WB = 63.5/12
t_f = 49/12
t_r = 47/12
W = 570
hcg = 11/12
hcp = 36/12
weight_dist = .53
cp_dist = .52
a_brake = 1.5 * 32.2
cl = .067
cd = cl/2
target_cf = 1.3/2.447
final = 3


 
v_0 = 1000
v_f = 1000

R = 30
degrees = 360
T1 = calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f); 

time = T1[1]
print(time)