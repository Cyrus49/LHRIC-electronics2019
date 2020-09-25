from configparser import SafeConfigParser

ENGINE_TORQUE = []

parser = SafeConfigParser()
parser.read('config.ini')
torque_points = int(parser.get('engine_torque', 'amt_points'))

for i in range(torque_points):
    ENGINE_TORQUE.append(float(parser.get('engine_torque', str(i+3) + 'k')))
print(ENGINE_TORQUE)
"""
for name in parser:
    vars()[name] = float(parser.get(name))
print(final_drive)
"""