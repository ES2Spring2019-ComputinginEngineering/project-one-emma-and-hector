# Project 1 Hector and Emma
# Hector and Emma

import numpy as np
import math

# initial conditions
angle = np.array([int(5*math.pi/2)])  # 25 degrees in radians
velocity = np.array([0])
acceleration = np.array([0])

def system_update(angle, acceleration, velocity, time_1, time_2):
    dt = int(time_2 - time_1)
    new_position = angle + dt * velocity
    new_velocity = velocity + dt * acceleration
    return new_position, new_velocity

def printing_system(angle, time, velocity):
    print("Time is :   ", time, " s")
    print("Angle is:   ", angle, " rads")
    print("Velocity is :   ", velocity, " m/s")

time = np.linspace(0, 15, 2500)
printing_system(angle[0], time[0], velocity[0])

i = 1
while i < len(time):
    acceleration = np.array(-9.8 * (math.cos(math.pi/2 - angle[i-1])/.30))
    new_position, new_velocity = system_update([angle[i-1]], [acceleration[i-1]], velocity, int(time[i-1]), int(time[i]))
    np.append(angle, new_position)
    np.append(velocity, new_velocity)
    printing_system(angle[i-1], time[i-1], velocity[i-1])
    i += 1/10000