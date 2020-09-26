import math
from lapsim_runner import ENGINE_TORQUE, GEAR_RATIOS #Imports constants
def wheel_torque(velocity, gear):
    #WHAT IS "PRIMARY" in f_torque?????
    FINAL_DRIVE = 3.5
    TIRE_RADIUS = 0.853
    PRIMARY = 2.545



    #RPM = [0] * len(GEAR_RATIOS)#AMT GEARS

    #ENGINE_TORQUE[0] * len(GEAR_RATIOS)#Amt of engine torque for each gears
    
    #Calculate wheel RPM for each gear
    
    #When we have gear and RPM 

    #Using gear and velocity, get rpm and torque then calculate final output to wheel


    #
    RPM = (velocity*60*gear*FINAL_DRIVE * PRIMARY) / (2*math.pi*TIRE_RADIUS)
    low_rpm_k = math.floor(RPM/1000)
    print (low_rpm_k)

    cur_engine_torque = 0
    #NO torque if below idle or above redline
    if low_rpm_k>=3 and low_rpm_k <11:
        cur_engine_torque = ((RPM - low_rpm_k*1000) * ENGINE_TORQUE[low_rpm_k+1 - 3] - ENGINE_TORQUE[low_rpm_k - 3] )/1000 + ENGINE_TORQUE[low_rpm_k - 3]
        print(cur_engine_torque, "cur engine torque")

    #Calculate torque at the wheels
    cur_wheel_torque = (cur_engine_torque*gear*FINAL_DRIVE*PRIMARY) / TIRE_RADIUS    

    print(cur_wheel_torque, "wheel torque")

    """
    #Calculate torque for each gear
    for cur_gear in range(len(GEAR_RATIOS)):
        #Get 2 surrounding torque figures for each rmp.
        """

wheel_torque(60, 1.533)