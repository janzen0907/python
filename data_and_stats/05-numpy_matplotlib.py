import numpy as np
from numpyhelpers import printnp as p
import matplotlib.pyplot as plt

my_data = np.array([33,2,3,14,61,22])
plt.plot(my_data)

# getting every 20 numbers from 50 to 1000
evenly_spaced_numbers = np.linspace(50,1000,20)
more_numbers = np.linspace(0,100,20)
plt.plot(evenly_spaced_numbers)

# clear it with plt.clf
#plt.clf()
plt.plot(evenly_spaced_numbers, more_numbers)
plt.show()