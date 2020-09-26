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
    current_time = 0
    d_accel = 0
    accel_1 = 0
    v_1 = v_0 #Why

    #Calculating and validating tire traction
    fz = W * weight_dist + cl * v_0**2 * cp_dist 
    fa = calc_long_force(fz) #Calculates tire force

    #This needs correcting, the logic doesn't logic
    #We're taking minimum of tire force and traction force 

    #If the torque being output by the car is less than the traction capability of the car, then the tires are producing as much traction as the car is outputting
    if fa >= f_torque(v_0, final):
        #If force of tires is less than force from car, traction is lost
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

    #Total Distance = d_total

    #d_total is an iteration count? Set to 246 for some reason.
    #   246 because 75 meters converted to feet
    while d_calc < d_total:
        
        k=k+1
        
        d_brake = (v_crit**2 - v_f**2)/(2 * a_brake) #Braking distance- final_v^2 = v_0^2+2as - acceleration = a, s = distance
        t_brake = (v_crit - v_f) / a_brake # Braking time - (Final_velocity - initial_velocity)/acceleration - assumes the above as well
        
        i=0
        
        while v_calc < v_crit: #What is vcrit??
            
            i=i+1
            
            #%fz = W * weight_dist + coefficient_lift * velocity**2 * center_of_pressure_distance + cd * v_calc**2 * hcp / WB + fa*hcg/WB
            #
            # moment over rear axle = Weight over rear axle + areodynamic forces over rear axle + Weight distribution by calculating moment on CG + areo forces over the rear axle
            # force over rear axle = moment over rear axle/ wheel base
            fz = 1/WB * (W * a + cl * v_calc**2 * a_prime + fwt * hcg + cd * v_calc**2 * hcp)
            # Downforce equation - 
            

            #acceleration_force = tire force * Target coefficient of friction
            fa = calc_long_force(fz)*target_cf
            
            #fa is set to the minimum of the limit of the tire and and amount of torque the engine is producing
            if fa >= f_torque(v_calc, final):
                fa = f_torque(v_calc, final)
            
            #force of acceleration = tire forces - drag forces
            fwt = fa - cd * v_calc**2
            
            # acceleration in terms of Gs = sum of forces acting on car /weight /acceleration due to gravity (32.2 ft/s^2)
            accel_2 = fwt / (W/32.2)
            
            #Current velocity = previous velocity + acceleration * time ???
            v_calc = v_calc + accel_1*t_step + t_step*(accel_2-accel_1)/2
            
            #Current time = current time + time_step
            current_time = current_time + t_step
            
            
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
    time_straight = t_brake + current_time


    outputs = [time_straight, dist_limit, v_1]
    return outputs

