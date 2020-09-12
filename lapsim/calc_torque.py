def calc_torque(RPM, t3000, t4000, t5000, t6000, t7000, t8000, t9000, t10000, t11000):
    if RPM <= 3000:
        torque = 0
    elif RPM < 4000 and RPM > 3000: #Order of operations below?????
        torque = (RPM - 3000)*(t4000 - t3000) / 1000 + t3000
    elif RPM < 5000 and RPM > 4000:
        torque = (RPM - 4000)*(t5000 - t4000) / 1000 + t4000
    elif RPM < 6000 and RPM > 5000:
        torque = (RPM - 5000)*(t6000 - t5000) / 1000 + t5000
    elif RPM < 7000 and RPM > 6000:
        torque = (RPM - 6000)*(t7000 - t6000) / 1000 + t6000
    elif RPM < 8000 and RPM > 7000:
        torque = (RPM - 7000)*(t8000 - t7000) / 1000 + t7000
    elif RPM < 9000 and RPM > 8000:
        torque = (RPM - 8000)*(t9000 - t8000) / 1000 + t8000
    elif RPM < 10000 and RPM > 9000:
        torque = (RPM - 9000)*(t10000 - t9000) / 1000 + t9000
    elif RPM < 11000 and RPM > 10000:
        torque = (RPM - 10000)*(t11000 - t10000) / 1000 + t10000
    else:
        torque = 0
    return torque