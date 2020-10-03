from configparser import SafeConfigParser

ENGINE_TORQUE = []
GEAR_RATIOS = []
CAR_DIMENSIONS = {}
CAR_WEIGHT = {}
CAR_DYNAMICS = {}
LIST_OF_DICT_SECTIONS = ["CAR_DIMENSIONS","CAR_WEIGHT","CAR_DYNAMICS"] #List of sections that we want to become dictonaries
parser = SafeConfigParser()
parser.read('config.ini')
torque_points = int(parser.get('engine_torque', 'amt_points'))

#Reads engine torque values from "engine_torque" in config.ini into array "ENGINE_TORQUE"
engine_info = parser.items('engine_torque')
for i in engine_info:
    if i[0][0].isdigit():
        rpm = int(i[0])
        torque = float(i[1])
        ENGINE_TORQUE.append((rpm, torque))

print(ENGINE_TORQUE)
        


for i in parser.items("gear_ratios"):
    if "gear" in i[0]:
        GEAR_RATIOS.append(float(i[1]))
print(GEAR_RATIOS)

#Creates dict from each section that we need a dict
CAR_DIMENSIONS = dict(parser.items("car_dimensions"))
CAR_WEIGHT = dict(parser.items("car_weight"))
CAR_DYNAMICS = dict(parser.items("car_dynamics"))

#Creates int from value in dict
"""
WHEEL_BASE = int(parser.get('car_dimensions','wheel_base'))
FRONT_TRACK = int(parser.get('car_dimensions','front_track'))
REAR_TRACK = int(parser.get('car_dimensions','rear_track'))
WEIGHT = int(parser.get('car_weight','weight'))
WEIGHT_DISTRIBUTION = int(parser.get('car_weight','weight_distribution'))
HEIGHT_GRAVITY = int(parser.get('car_dynamics','height_gravity'))
COEFFICENT_DRAG = int(parser.get('car_dy'))
HEIGHT_CENTER_PRESSURE = int(parser.get('car_dynamics','height_center_pressure'))
#OCENTER_PRESSURE_REARWARD = int(parser.get('car_dycoefficent_liftmic        if "." in current_section[i]:
#            current_section[i] = float(current_section[i])
#        else:
#            current_section[i] = int(current_section[i])

#convert_strings(CAR_DIMENSIONS)
#convert_strings(CAR_WEIGHT)
#convert_strings(CAR_DYNAMICS)
    
print(CAR_DIMENSIONS)
#{'wheel_base': 420, 'front_track': 1.1, 'rear_track': 1}
CAR_DIMENSIONS["torque"] = 15
print(CAR_DIMENSIONS)
"""