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
for i in range(torque_points):
    ENGINE_TORQUE.append(float(parser.get('engine_torque', str(i+3) + 'k')))
print(ENGINE_TORQUE)

for i in parser.items("gear_ratios"):
    if "gear" in i[0]:
        GEAR_RATIOS.append(float(i[1]))
print(GEAR_RATIOS)

#Creates dict from each section that we need a dict
CAR_DIMENSIONS = dict(parser.items("car_dimensions"))
CAR_WEIGHT = dict(parser.items("car_weight"))
CAR_DYNAMICS = dict(parser.items("car_dynamics"))

#converts the strings in the dict to floats and ints
def convert_strings(current_section):
    for i in current_section: 
        if "." in current_section[i]:
            current_section[i] = float(current_section[i])
        else:
            current_section[i] = int(current_section[i])

convert_strings(CAR_DIMENSIONS)
convert_strings(CAR_WEIGHT)
convert_strings(CAR_DYNAMICS)
    
