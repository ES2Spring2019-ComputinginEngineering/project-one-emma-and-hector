import microbit
import math
import os
import random

filename = "Pendelum_Values" + str(random.randint(1,999)) + ".txt"

while microbit.button_a.is_pressed():
    microbit.sleep(50)

with open(filename, "w") as file:
    start_time = (microbit.running_time())/1000
    while microbit.button_b.is_pressed():
        acceleration_x = (microbit.accelerometer.get_x())/1000
        acceleration_y = (microbit.accelerometer.get_y())/1000
        microbit.display.show(microbit.Image.SILLY)
        time = (microbit.running_time())/1000 - start_timex
        values = str(acceleration_x) + "," + str(acceleration_y) + "," + str(time) + "\n"
        file.write(values)
        microbit.sleep(50)
        print(values)
file.close()