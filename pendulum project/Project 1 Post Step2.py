import matplotlib.pyplot as plt
import numpy as np
import math
#Project 1 Hector and Emma
#Hector and Emma

#initial conditions
Angle = [(5*math.pi/2)] #25 degrees in radians
Velocity = [0]
Acceleration = [0]

def System_Update(Angle,Acceleration,Velocity,Time_1,Time_2):
    dt = Time_2 - Time_1
    New_Position = Angle + dt * Velocity
    New_Velocity = Velocity + dt * Acceleration
    New_Acceleration = -9.8 * (math.cos(math.pi/2 - New_Position))
    return New_Position, New_Velocity, New_Acceleration

def Printing_System(Angle, Time, Velocity):
    print("Time is :   ", Time)
    print("Angle is:   ", Angle)
    print("Velocity is :   ", Velocity)

time = np.linspace(1,50,5)
Printing_System(Angle[0], time[0], Velocity [0])

i=1
while i <len(time):
    New_Position, New_Velocity, New_Acceleration = System_Update(Angle [i-1],Acceleration[i-1],Velocity [i-1],time[i-1],time[i])
    Angle.append(New_Position)
    Velocity.append(New_Velocity)
    Acceleration.append(New_Acceleration)
    Printing_System(Angle[i], time[i], Velocity [i])
    i += 1

plt.figure(figsize=(4,6))
plt.subplot(3,1,1)
plt.plot(time,Angle,'r-')

plt.xlabel('Time(Seconds)')
plt.ylabel('Angle(radians)')
plt.title('Position vs Time')
plt.grid()
plt.tight_layout()
plt.show

plt.subplot(3,1,2)
plt.plot(time,Velocity,"b-")
plt.xlabel('Time(seconds)')
plt.ylabel('Velocity(rad/s)')
plt.title('Velocity vs Time')
plt.grid()
plt.tight_layout()
plt.show

plt.subplot(3,1,3)
plt.plot(time, Acceleration, 'k-')
plt.xlabel('Time(seconds)')
plt.ylabel('Acceleration(rad/s^2)')
plt.title('Acceleration vs Time')
plt.grid()
plt.tight_layout()
plt.show