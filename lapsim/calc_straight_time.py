import math
from f_torque import *
from calc_long_force import *
def calc_straight_time(W, hcg, hcp, cl, cd, WB, weight_dist, cp_dist, v_0, v_f, d_total, a_brake, target_cf, final):

    #Outputs are listed at bottom of the program in an array because we can't
    #have multiple outputs for some reason.

    #Load over rear axle
    a = weight_dist * WB

    #Aero force over rear axle
    a_prime = cp_dist * WB

    #Establishing parameters for calculations
    t_step = .0001
    v_step = .0001

    #This is a Boolean for something.
    dist_limit = 0

    #What
    d_calc = 0
    t_accel = 0
    d_accel = 0
    accel_1 = 0
    v_1 = v_0 #Why

    #Calculating and validating tire traction
    fz = W * weight_dist + cl * v_0**2 * cp_dist 
    fa = calc_long_force(fz)

    #This needs correcting, the logic doesn't logic
    if fa >= f_torque(v_0, final):
        fa = f_torque(v_0, final) 


    #I think this is resultant force on car (forward traction - drag), but 
    fwt = fa - cd * v_0**2

    v_calc = v_0 #Oh come on

    #what
    if v_0 >= v_f:
        v_crit = v_0 + v_step
    else:
        v_crit = v_f + v_step


    #Something to do with a v_crit and exceeding max loop count
    k=0

    
    #Cyrus
    #What's happening here?

    #d_total is an iteration count? Set to 246 for some reason.
    while d_calc < d_total:
        
        k=k+1
        
        d_brake = (v_crit**2 - v_f**2)/(2 * a_brake)
        t_brake = (v_crit - v_f) / a_brake
        
        i=0
        
        while v_calc < v_crit:
            
            i=i+1
            
            #%fz = W * weight_dist + cl * v_calc**2 * cp_dist + cd * v_calc**2 * hcp / WB + fa*hcg/WB
            fz = 1/WB * (W * a + cl * v_calc**2 * a_prime + fwt * hcg + cd * v_calc**2 * hcp)
            
            fa = calc_long_force(fz)*target_cf
            
            if fa >= f_torque(v_calc, final):
                fa = f_torque(v_calc, final)
            
            
            fwt = fa - cd * v_calc**2
            
            accel_2 = fwt / (W/32.2)
            
            v_calc = v_calc + accel_1*t_step + t_step*(accel_2-accel_1)/2
            
            t_accel = t_accel + t_step
            
            d_accel = d_accel + v_1*t_step + t_step * (v_calc - v_1)/2
            
            v_1 = v_calc
            
            accel_1 = accel_2
            
            if i>100000:
                print('distance')
                exit(11)
            
            
            if d_accel > d_total:
                dist_limit = 1
                v_calc = v_crit
            
            
        
        
        v_crit = v_crit + v_step
        
        d_calc = d_brake + d_accel
        
        if dist_limit == 1:
            d_calc = d_accel
            t_brake = 0
        
        
        if k>10000000:
            print('v_crit')
            exit(12)
        



    #Okay t_brake isn't really needed for acceleration, may be needed for
    #urance or something.
    time_straight = t_brake + t_accel


    outputs = [time_straight, dist_limit, v_1]
    return outputs

