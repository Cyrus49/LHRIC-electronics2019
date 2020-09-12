import math
from calc_lat_force import *
def calc_corner_time_2(W, hcg, hcp, cl, cd, WB, t_f, t_r, weight_dist, cp_dist, R, degrees, target_cf, v_0, v_f):


    length = 2*math.pi*R*degrees/360

    a = weight_dist * WB
    b = WB - a

    a_prime = cp_dist * WB
    b_prime = WB - a_prime

    m = 1

    Ay_converge = .0001

    Ay = 1

    Ay_diff = 1

    t = (t_f + t_r) / 2

    while Ay_diff > Ay_converge:
        
        v_calc = (Ay*32.2 * R)**(1/2)
        
        fzr = W * weight_dist + cl * v_calc**2 * cp_dist + cd * v_calc**2 * hcp / WB

        WT = (W*Ay*hcg/(t))

        fzr_o = fzr/2 + WT/2
        fzr_i = fzr/2 - WT/2

        fyr = (calc_lat_force(fzr_o,-6*math.pi/180,0) + calc_lat_force(fzr_i,-6*math.pi/180,0))*target_cf;

        A_lat = fyr/(W*(weight_dist))
            
        Ay_check = Ay
        
        Ay = A_lat
        
        Ay_diff = abs(Ay_check-A_lat)
        
        m = m+1

        if m > 10000:
            print('iterations maxed!')
            exit(10)



    m=m-1

    v_final = (Ay*32.2 * R)**(1/2)
    time_corner = length / v_final

    t_step = .001

    x=0
    x2=0
    l=0
    l2=0

    if v_0 < v_final:
        
        v = v_0
        x = 0
        l = 0
        Ax = math.sqrt((v_final**4 - v_0**4)/(R*32.2)**2)
        
        while Ax > .001:
            
            l = l+1
            Ax = math.sqrt((v_final**4 - v**4)/(R*32.2)**2)
            v = v + Ax * t_step
            x = x + v*t_step
            


    if v_f < v_final:
        
        v = v_f
        x2 = 0
        l2 = 0
        Ax = math.sqrt((v_final**4 - v_f**4)/(R*32.2)**2)
        
        while Ax > .001:
            
            l2 = l2+1
            Ax = math.sqrt((v_final**4 - v**4)/(R*32.2)**2)
            v = v + Ax * t_step
            x2 = x2 + v*t_step
            


    newlength = length - x - x2
    time_const_speed = newlength / v_final
    time_change_speed = l * t_step + l2 * t_step
    time_corner = time_const_speed + time_change_speed

    print(newlength)
    print(time_const_speed)
    print(time_change_speed)
    print(time_corner)
    answer = [Ay, time_corner, v_final]

    return answer