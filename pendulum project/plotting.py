# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:03:55 2019
plotting!! (to import)
@author: Emma Whalen
"""
import matplotlib.pyplot as plt
import numpy as np

# function creation:

# plotting functions

def sim_plot(time, Angle, Velocity, Acceleration):
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
    
def filt_theta(t, y_noisy_filt, y_noisy_filt_pks):
    plt.subplot(2, 1, 1)
    plt.plot(t, y_noisy_filt,'g-', t[y_noisy_filt_pks], y_noisy_filt[y_noisy_filt_pks], 'b.')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Y Acceleration (m/s^2)')
    plt.title('Y Acceleration vs Time Filtered')
    plt.grid()
    
def filt_acc(t, theta, y_noisy_filt_pks):
    plt.subplot(2, 1, 2)
    plt.plot(t, theta,'b-', t[y_noisy_filt_pks], theta[y_noisy_filt_pks], 'g.')
    plt.title('Noisy Median Filtered')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Theta(radians)')
    plt.title('Theta vs Time Filtered')
    plt.grid()
    
# period calculation function
    
def period(t, y_noisy_filt_pks):
    peaks = t[y_noisy_filt_pks]
    time_difference = np.diff(peaks)
    period = str(np.sum(time_difference)/len(time_difference))
    print("Period: " + period + "s")