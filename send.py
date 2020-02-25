import can

bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
msg= can.Message(arbitration_id=0x7de, data=[0, 25, 0, 1, 3, 1, 4, 1], extended_id=False)
msg2= can.Message(arbitration_id=0x9de, data=[0, 7, 0, 1, 3, 1, 4, 1], extended_id=False)
bus.send(msg)
bus.send(msg2)
