# Hector Rivera and Emma Whalen
# LOG GRAPHS FOR REPORT

# This code analyzes the effect of length of pendulum on period for the 
# simulated data and the real-word data.

# x = pendulum length
# y = period

import matplotlib.pyplot as plt

# assign pendulum lengths
pen_len = [.1524, .2032, .254, .4064, .508] # these are the lengths of the real-world model 
# pendulums that we used to collect data


# periods (calculated using other codes)
simT = [.7831371895, .9042889343, 1.011025764, 1.278857675, 1.429806348]
realT = [.65916, .81661111111, .8960999999, .918999999, 1.1894545454]

# Real World
plt.subplot(3, 1, 3)
plt.plot(pen_len, realT)
plt.yscale('log')
plt.title('Pendulum Length vs Period (Real)')
plt.xlabel('Pendulum Length (meters)')
plt.ylabel('Period (seconds)')
plt.grid()
plt.show()

# Simulated
plt.subplot(3, 1, 1)
plt.plot(pen_len, simT)
plt.yscale('log')
plt.title('Pendulum Length vs Period (Simulated)')
plt.xlabel('Pendulum Length (meters)')
plt.ylabel('Period (seconds)')
plt.grid()
plt.show()

