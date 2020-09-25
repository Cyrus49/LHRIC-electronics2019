import math
from lapsim_runner import * #Imports constants
def wheel_torque(velocity):
    #WHAT IS "PRIMARY" in f_torque?????

    RPM[0] * len(GEAR_RATIOS)#AMT GEARS

    ENGINE_TORQUE[0] * len(GEAR_RATIOS)#Amt of engine torque for each gears
    
    #Calculate wheel RPM for each gear
    """
    for cur_gear in range(len(GEAR_RATIOS)):
        RPM[cur_gear] = (velocity*60*GEAR_RATIOS[cur_gear]*FINAL_DRIVE) / (2*math.pi*TIRE_RADIUS)

    #Calculate torque for each gear
    for cur_gear in range(len(GEAR_RATIOS)):
        #Get 2 surrounding torque figures for each rmp.
        """