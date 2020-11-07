import guizero
from guizero import Text, App
from time import sleep
gearDisplay = App("Gear")


#f = open("Gear.txt", "r")
#cur_Gear = f.read()
#f.close()
def updateGear():
    f = open("Gear.txt", "r")
    gear.value = f.read()
    f.close()
    #gear.value = int(gear.value)+1
    #print(gear.value)

cur_Gear = 1
gear = Text(gearDisplay, text=str(cur_Gear), size = 150)


gear.repeat(10, updateGear)
gearDisplay.display()
