# Project 1
Emma and Hector, created by GitHub Classroom

## Instructions:
How to use code: 
- use [Collection.py](https://github.com/ES2Spring2019-ComputinginEngineering/project-one-emma-and-hector/blob/master/Collection.py) in Mu to collect data from the microbit:
  - flash the file onto the microbit, then press the B button to start recording data
  - once you have finished, drag the file from the microbit (which should be labeled Pendulum_Vals + 3 random integers) to your computer
- use [Parsingnew.py]https://github.com/ES2Spring2019-ComputinginEngineering/project-one-emma-and-hector/blob/master/pendulum%20project/parsingnew.py) to read the files created by running Collection.py and graph y acceleration vs time filtered, and theta vs time filtered. 
```
filename = 'Pendulum_Vals123' # replace this with name of file created from data collection
```
We have included Pendulum_Vals3.txt in our project as a test file to parse and analyze - use this to test the code. 

- use [Project 1 Post Step2.py](https://github.com/ES2Spring2019-ComputinginEngineering/project-one-emma-and-hector/blob/master/pendulum%20project/Project%201%20Post%20Step2.py) to run a simulation for a pendulum swinging
- The code required to calculate the period can be found at the bottom of [plotting.py](https://github.com/ES2Spring2019-ComputinginEngineering/project-one-emma-and-hector/blob/master/Plotting.py). It is also shown below:
```
peaks = t[y_noisy_filt_pks]
time_difference = np.diff(peaks)
period = str(np.sum(time_difference)/len(time_difference))
```

- use [LogGraphs.py](https://github.com/ES2Spring2019-ComputinginEngineering/project-one-emma-and-hector/blob/master/pendulum%20project/LogGraphs.py) to analyze the effect of pendulum length on period.
- [plotting.py](link.com) is the file where we defined most of the big functions, mainly plotting functions in addition to period calculation. Functions from this code are called by importing plotting.py as plot.


