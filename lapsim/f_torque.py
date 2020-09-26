import math
from calc_torque import *

#Tf is f_torquektm.m for??
#The comments make calc_straight_time sus
def f_torque(v, final_drive):
    #tf are these numbers
    t3000 = 31
    t4000 = 32
    t5000 = 32.7
    t6000 = 33
    t7000 = 33
    t8000 = 32.5
    t9000 = 31.5
    t10000 = 29.5
    t11000 = 27

    tire_radius = .853
    primary = 2.545
    gear1 = 2.583
    gear2 = 1.923
    gear3 = 1.533
    gear4 = 1.263
    gear5 = 1.05


    RPM1 = (v*60*gear1*primary*final_drive) / (2*math.pi*tire_radius)
    RPM2 = (v*60*gear2*primary*final_drive) / (2*math.pi*tire_radius)
    RPM3 = (v*60*gear3*primary*final_drive) / (2*math.pi*tire_radius)
    RPM4 = (v*60*gear4*primary*final_drive) / (2*math.pi*tire_radius)
    RPM5 = (v*60*gear5*primary*final_drive) / (2*math.pi*tire_radius)

    print(RPM1, RPM2, RPM3, RPM4, RPM5)


    torque1 = calc_torque(RPM1, t3000, t4000, t5000, t6000, t7000, t8000, t9000, t10000, t11000)
    torque2 = calc_torque(RPM2, t3000, t4000, t5000, t6000, t7000, t8000, t9000, t10000, t11000)
    torque3 = calc_torque(RPM3, t3000, t4000, t5000, t6000, t7000, t8000, t9000, t10000, t11000)
    torque4 = calc_torque(RPM4, t3000, t4000, t5000, t6000, t7000, t8000, t9000, t10000, t11000)
    torque5 = calc_torque(RPM5, t3000, t4000, t5000, t6000, t7000, t8000, t9000, t10000, t11000)

    thrust_force_1 = (torque1*gear1*final_drive*primary) / tire_radius

    thrust_force_2 = (torque5*gear5*final_drive*primary) / tire_radius

    thrust_force_3 = (torque4*gear4*final_drive*primary) / tire_radius

    thrust_force_4 = (torque3*gear3*final_drive*primary) / tire_radius

    thrust_force_5 = (torque2*gear2*final_drive*primary) / tire_radius #Var name and torque/gears mismatched???

    thrust_force_0 = (t3000*gear1*final_drive*primary) / tire_radius #unused??

    print(thrust_force_1,thrust_force_2,thrust_force_3,thrust_force_4, thrust_force_5)

    TF = [thrust_force_1, thrust_force_2, thrust_force_3, thrust_force_4, thrust_force_5]

    thrust_force = max(TF)

    if RPM5 > 11000:
        thrust_force = 0

    if RPM1 < 3000:
        thrust_force = (t3000*gear1*final_drive*primary) / tire_radius

    return thrust_force

print(f_torque(60,3.5))