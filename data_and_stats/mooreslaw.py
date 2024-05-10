import numpy as np
from numpyhelpers import printnp as p
import matplotlib.pyplot as plt
# Tutorial for this is linked in brightspace

# Load in some raw transistor data
raw_data = np.loadtxt('transistor_data.csv', delimiter=',', usecols=[1,2], skiprows=1)
p(raw_data)
a_years = raw_data[:,1].astype('int32') # Take all of the first dimension, but only index 1 from the second 
p(a_years)
a_trans = raw_data[:,0].astype('int64')
p(a_trans)

# Now we can plot it
# plt.plot(a_years, a_trans, 'bo')
# Convience wrapper fro matplotlib that'll plot things on a 
# semilog scale for one axis
plt.semilogy(a_years, a_trans, 'bo', label="Transistor Count",alpha=0.2)
# plt.show()

# Need to understand the data for knowing what to do via numpy
# For our example we are going to transpose the years and get all years
# Can we get the mean for each year?
year_range = np.atleast_2d(np.arange(1971,2020)).transpose()
p(year_range)
year_mask = np.where(a_years == year_range, True, False)
p(year_mask)
trans_for_each_year = np.where(year_mask, a_trans, 0)
p(trans_for_each_year)
mean_trans_for_each_year = trans_for_each_year.sum(axis=1) / np.count_nonzero(trans_for_each_year, axis=1)
p(mean_trans_for_each_year)

# Lets plot them
plt.plot(year_range, mean_trans_for_each_year, 'g+', markersize=14, mew=2, label='Average transistor count')


START_YEAR = 1971
START_TRANS = 2250

# wRITE Moores law as a lambda
moores_law = lambda year : START_TRANS * 2 ** ((year - START_YEAR) /2)
# Generate an array by pasing in a_years
a_moores_trans = moores_law(a_years)
plt.plot(a_years, a_moores_trans, label ="Moore's Law")
# plt.show()

# Assumption: Data grows exponentially as a function of the year
# Can we find teh constanst we need to make that true?

# I want to find the constants to do a linear equation to get that value we're squaring 
# Numpy has a function to find us the data for a best fit polynomial line
model = np.polynomial.Polynomial.fit(a_years, np.log(a_trans), deg=1)
# By default, it sets a domain window based on the indepentdent variable and scales
# but we can use convert to get the unscaled and unshifted model
model = model.convert()
print(model)

# Remeber the equation for a line? (y = a + x * b). This gives s our constants for a line taht fits the best we cna to the data
linear_constant, linear_coeffient = model
# Lets see what that looks like
print(f"Transistors will be multiplied every two eyars at a rate of {np.exp(linear_coeffient * 2)}")
# Graph it
a_trans_best_fit = np.exp(linear_constant) * np.exp(linear_coeffient * a_years)
plt.plot(a_years, a_trans_best_fit, label="Linear Regression")
plt.legend(loc="upper left")
plt.show()