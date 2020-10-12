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

    
    #Calculate wheel RPM for each gear
    
    #When we have gear and RPM 

    #Using gear and velocity, get rpm and torque then calculate final output to wheel

    engine_rpm_per_gear = [0] * len(GEAR_RATIOS)
    
    
    #calculates engine rpm for each gear
    for i in range(len(GEAR_RATIOS)):
        engine_rpm_per_gear[i] = (velocity*60*GEAR_RATIOS[i]*FINAL_DRIVE * PRIMARY) / (2*math.pi*TIRE_RADIUS)
        
        
    
    engine_torque = [0] * len(GEAR_RATIOS) # Engine torque per gear

    #print(engine_rpm_per_gear)
    for i in range(len(GEAR_RATIOS)):
        cur_torque_idx = 0

        #Find points in the torque curve that surround current RPM to preform linear regression
        if engine_rpm_per_gear[i]<ENGINE_MIN_SPEED or engine_rpm_per_gear[i]>ENGINE_REDLINE:
            cur_torque_idx = -1
        else:
            while  ENGINE_TORQUE[cur_torque_idx][0] <= engine_rpm_per_gear[i]:
                cur_torque_idx+=1

        #Preform linear regression if rpm is within rev range
        #print(cur_torque_idx)
        if cur_torque_idx == -1:
            engine_torque[i] = 0
           # print("NO REGRESSION - OUT OF REV RANGE")
        else:
            rpm_diff = engine_rpm_per_gear[i] - ENGINE_TORQUE[cur_torque_idx-1][0] #This will show how many RPM away we are from the lower rpm value we're in between
            torque_range = ENGINE_TORQUE[cur_torque_idx][1] - ENGINE_TORQUE[cur_torque_idx-1][1] #This is the difference in torque between the 2 points that surround our current RPM value
            rpm_range = ENGINE_TORQUE[cur_torque_idx][0] - ENGINE_TORQUE[cur_torque_idx-1][0] #The difference in RPM between the 2 points we're using to preform the regression
            #print("RPM diff", rpm_diff, "\t Torque_range", torque_range, "\t RPM range", rpm_range, "\tTorque curve upper index",cur_torque_idx)
            engine_torque[i] = ((rpm_diff * torque_range)/ rpm_range) + ENGINE_TORQUE[cur_torque_idx-1][1]
        
   # print(engine_torque)
    
    
    #Calculate torque at the wheels
    wheel_torque = [0] * len(GEAR_RATIOS)
    for i in range(len(GEAR_RATIOS)):
        if engine_torque[i] > 0:
            wheel_torque[i] = (engine_torque[i]*GEAR_RATIOS[i]*FINAL_DRIVE*PRIMARY) / TIRE_RADIUS    

    print(wheel_torque, "wheel torque")




wheel_torque(60)