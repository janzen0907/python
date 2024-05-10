import numpy as np
from numpyhelpers import printnp as p

# We can slice and index passing in other arrays for indices
numbers = np.arange(25).reshape(5,5)
indexes_horizontal = np.array([2,3,1])
p(numbers)
p(indexes_horizontal)
p(numbers[indexes_horizontal])
indexes_vertical = np.array([0,2,1])
p(indexes_vertical)
# If you're going to do this with mulyiple index arrays they must be the same shape or be broadcastable
p(numbers[indexes_horizontal, indexes_vertical])
indexes = (indexes_horizontal,indexes_vertical)
numbers[indexes] = 99999
p(numbers)

categories = np.array(['Alpha', "Bravo", "Delta"])

data = np.array([
    [75,30,78,50,32],
    [12,44,12,40,1],
    [99,2,12,44,29]
])
# Use the argmax method to get teh highest value along a dimension
p(data)
# This will give us the biggest argument, the index of it that is not the actual value
p(data.argmax(axis=0))
p(categories[data.argmax(axis=0)])

# We can index with boolean arrays
bools = np.array([True,False,True]) # This will only display the first and third position
p(data[bools])
# You canuse conditional operators to generate arrays of booleans
over_40 = data > 40
p(over_40)
p(data[over_40])

# What if want to not just only return teh avalues where it is true, but instead return
# Different things depending on wheter it is true or false? You can use numpy.where
# Lots of functions can take an options where parameter
multiples_of_five_are_zero = np.where(data % 5 ==0, 0 ,data)
p(multiples_of_five_are_zero)

# Only include data where it passes the test
# If removing values the shape will change. We can't have a jagged array
# Generally you will flatten it first
flat_fives_are_zeroes = multiples_of_five_are_zero.flatten()
p(flat_fives_are_zeroes)
# Take slices of it, only the values that are not 0
where_there_are_no_zeros = np.where(flat_fives_are_zeroes != 0)
print(where_there_are_no_zeros)
no_zeroes = flat_fives_are_zeroes[where_there_are_no_zeros]
p(no_zeroes)

# Structured arrays are kind of a dictionary of arrays where all teh arrays ahve thesame shape, but not
# the same data types
# This is a list of tuples not a numpy thing
my_employee_data = [
    ('Brad',23.5,11.2),
    ('Candice',40,5.6),
    ('Donald',55,22),
    ('Edgar',19.33,4),
    ('Faith', 18.50,2),
    ('Gerald',22.30,5.2)
]

employees_structured_array = np.array(my_employee_data, dtype=[
    ('name', '<U20'),
    ('wage', 'float64'),
    ('tenure', 'float32')
])

p(employees_structured_array)
p(employees_structured_array['name'])
print(employees_structured_array['wage'].sum())
# Where returns a tuple not an array, so can't use printnp method
longterm_employess = np.where(employees_structured_array['tenure'] >= 5)
print(longterm_employess)
p(employees_structured_array['name'][longterm_employess])
# Mean wage for longterm employees:
p(employees_structured_array['wage'][longterm_employess].mean())