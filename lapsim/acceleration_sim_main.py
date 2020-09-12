from calc_straight_time import *
#All dimensions in imperial units
#
#Input Wheelbase, weight, cg height, cp height, weight distribution,
#pressure distribution, initial velocity, (?)final velocity, "d_total", braking gs
#lift coeff, drag coeff, "target cf", "final"

WB = 63.5/12
W = 570
hcg = 11/12
hcp = 36/12
weight_dist = .55
cp_dist = .52
v_0 = 0
v_f = 1000
d_total = 246
a_brake = 1 * 32.2
cl = .0
cd = cl #???? I have no idea why????
target_cf = 1.4/2.447
final = 2.8
m=1
##########################################################################
#inputs complete, call accel function to get time

#for cl = 0:.067/5:.067
#m=m+1
time_accel = calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final)

print(time_accel)

#Idx out of bounds, ignoring for now time_brake = time_accel(4)

#xaxis = 0:.067/5:.067