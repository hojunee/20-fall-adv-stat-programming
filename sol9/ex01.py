import matplotlib.pyplot as plt
import math 
import numpy as np

x = [i for i in np.arange(0, 2*math.pi, 0.001)]

y_1 = [math.sin(5*i) for i in x]
y_2 = [math.cos(4*i) for i in x]

plt.plot(x, y_1)
plt.plot(x, y_2)
plt.show()