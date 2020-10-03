import math
from lapsim_runner import ENGINE_TORQUE, GEAR_RATIOS#, ENGINE_REDLINE #Imports constants
def wheel_torque(velocity):
    #WHAT IS "PRIMARY" in f_torque?????
    FINAL_DRIVE = 3.5
    TIRE_RADIUS = 0.853
    PRIMARY = 2.545

    #ENGINE_TORQUE = [31,32,32.7,33,33,32.5,31.5,29.5,27]
    #GEAR_RATIOS = [2.583,1.923,1.533,1.263,1.05]
    ENGINE_REDLINE = 11000
    ENGINE_MIN_SPEED = ENGINE_TORQUE[0][0]
    print(ENGINE_MIN_SPEED)

    #RPM = [0] * len(GEAR_RATIOS)#AMT GEARS

    #ENGINE_TORQUE[0] * len(GEAR_RATIOS)#Amt of engine torque for each gears
    
    #Calculate wheel RPM for each gear
    
    #When we have gear and RPM 

    #Using gear and velocity, get rpm and torque then calculate final output to wheel

    engine_rpm_per_gear = [0] * len(GEAR_RATIOS)
    
    
    #calculates engine rpm for each gear
    for i in range(len(GEAR_RATIOS)):
        engine_rpm_per_gear[i] = (velocity*60*GEAR_RATIOS[i]*FINAL_DRIVE * PRIMARY) / (2*math.pi*TIRE_RADIUS)
        
        
    
    wheel_torque_per_gear = [0] * len(GEAR_RATIOS)
    print(engine_rpm_per_gear)
    for i in range(len(GEAR_RATIOS)):
        cur_torque_idx = 0
        if engine_rpm_per_gear[i]<ENGINE_MIN_SPEED or engine_rpm_per_gear[i]>ENGINE_REDLINE:
            cur_torque_idx = -1
        else:
            while cur_torque_idx < len(ENGINE_TORQUE)-1 and ENGINE_TORQUE[cur_torque_idx][0] <= engine_rpm_per_gear[i]:
                cur_torque_idx+=1
        print(cur_torque_idx)
        if cur_torque_idx == -1:
            wheel_torque_per_gear[i] = 0
        else:
            wheel_torque_per_gear[i] = (((engine_rpm_per_gear[i] - ENGINE_TORQUE[i-1][0]) * (ENGINE_TORQUE[i][1] - ENGINE_TORQUE[i-1][1]))/ (ENGINE_TORQUE[i][0] - ENGINE_TORQUE[i-1][0])) + ENGINE_TORQUE[i-1][1]
        
    print(wheel_torque_per_gear)
    
    #NO torque if below idle or above redline
    if low_rpm_k>=3 and low_rpm_k <11:
        #cur_engine_torque = ENGINE_TORQUE[low_rpm_k-3]
        cur_engine_torque = ((cur_engine_rpm - low_rpm_k*1000) * (ENGINE_TORQUE[low_rpm_k+1 - 3] - ENGINE_TORQUE[low_rpm_k - 3]) )/1000 + ENGINE_TORQUE[low_rpm_k - 3]
        print(cur_engine_torque, "cur engine torque")

    #Calculate torque at the wheels
    cur_wheel_torque = (cur_engine_torque*GEAR_RATIOS[cur_gear-1]*FINAL_DRIVE*PRIMARY) / TIRE_RADIUS    

    print(cur_wheel_torque, "wheel torque")

    """
    #Calculate torque for each gear
    for cur_gear in range(len(GEAR_RATIOS)):
        #Get 2 surrounding torque figures for each rmp.
        """

wheel_torque(60)