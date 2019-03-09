# FILE PARSING CODE
# authors: Hector Rivera and Emma Whalen
# This code will parse the files created by Final_Collection.py and
# plot y acceleration vs time on one graph and theta vs time on another,
# then calculate the period from these graphs.

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import plotting as plot

# Global variables

s = [] # string for acceleration values
t = [] # string for time values
g = 9.81 # acceleration due to gravity

# Main script
    
with open ("Pendulum_Vals3.txt", "r") as file: # uses example file
    for line in file:
        line = line.rstrip().split(",") # splits file using commas
        y_acceleration = float(line[1])
        time = float(line[2])
        s.append(y_acceleration) # adds acc vals to s for graph
        t.append(time) # adds time vals to t for graph

t = np.asarray(t)

# apply median filter to noisy and original wave
y_noisy_filt = sig.medfilt(s) 
y_noisy_filt_pks, _ = sig.find_peaks(y_noisy_filt)

theta = np.arcsin(y_noisy_filt / g)

plot.filt_acc(t, theta, y_noisy_filt_pks) # plot filt. y acc. vs time
plot.filt_theta(t, y_noisy_filt, y_noisy_filt_pks) # plot filt. theta vs time

plt.tight_layout()
plt.show()

plot.period(t, y_noisy_filt_pks) # find period and print it

