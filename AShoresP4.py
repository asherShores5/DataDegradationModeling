#Asher Shores
#Dr. Ricardo Citro
#This is my own work

#Differential Equations:
# x'1 = 1/50 * x1 + 3/100 * x2
# x'2 = 1/50 * x1 - 3/100 * x2


#Implementation
# Solved by hand in documentation file
# Matplotlib graphical representation


import numpy as np                  #import numpy
import matplotlib.pyplot as plt     #import matplotlib

#defining each equation for graphing
def eq1(t):
    return -1 * np.exp((-1/20) * t) #
def eq2(t):
    return np.exp((-1/20) * t) #

t = np.linspace(-10, 10)        #making t the linspace
x = eq1(t)                     #setting x values based on t
x2 = eq2(t)

#Graph from project 4
plt.title("Solution graph")                             #set the title
plt.xlabel("time")                                      #label the x-axis t
plt.ylabel("x")                                         #label the y-axis x
plt.plot(t, x, 'b-', label = "e^(-t/20)", linewidth = 2)      #plot sol 1
plt.plot(t, x2, 'r-', label = "-e^(-t/20)", linewidth = 2)    #plot sol 2
plt.legend()                               #adds the legend to the graph
plt.show()                                 #plots graphs
