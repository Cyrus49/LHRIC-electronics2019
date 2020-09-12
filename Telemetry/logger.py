import can
import os
import time

CUR_DIRECTORY = os.getcwd();

bus = can.interface.Bus("can0", bustype="socketcan_native")

notifier = can.Notifier(bus,[can.Printer()])

time.sleep(5);
"""
while(True):
    test_logger = can.Logger(CUR_DIRECTORY+"/log3.log",'a+');
    msg = bus.recv()
    test_logger(msg)


    can.Logger.stop(test_logger)
    time.sleep(3)
    print("Restarting")
    """