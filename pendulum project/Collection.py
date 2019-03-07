# Microbit Data Collection
# Hector Rivera and Emma Whalen
# collects acceleration in x and y direction from microbit

import microbit
import math
import os
import random

# global variables

filename = "Pendulum_Vals" + str(random.randint(1,999)) + ".txt"

# main script

while microbit.button_a.is_pressed():
    microbit.sleep(50)

with open(filename, "w") as file:
    start_time = (microbit.running_time())/1000
    while not microbit.button_b.is_pressed():
        acceleration_x = (microbit.accelerometer.get_x())/1000
        acceleration_y = (microbit.accelerometer.get_y())/1000
        microbit.display.show(microbit.Image.SILLY)
        time = (microbit.running_time())/1000 - 0
        values = str(acceleration_x) + "," + str(acceleration_y) + "," + str(time) + "\n"
        file.write(values)
        microbit.sleep(50)
        print(values)
file.close()