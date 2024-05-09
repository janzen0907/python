import numpy as np
from numpyhelpers import printnp
# NumPy is the package for scientific computing in Python
# It's main feature is a multidimensional homogenours array object,
# assorted derived objects (like masked arrays and matrices) and
# a whole bunch of routines for fast operations on arrays including
# math, logic, sorting, basic linear alfebra, stats, simulations and more,

# the ndarray object is the heart of NumPy. It encapsulates a n-dimensioal
# array of homogenous data types
# Differences between np arrays and python lists:
# - fixed size creation - changing the size involves deleting and remaking
# - All elements must be of the same types, which means they'll be the same size
# - Note that these types could be Python objects
# - NumPy optimized for doing advanced mathematical operations on large amounts of data

# It is fast because you write vectorized code with it - that is, you avoid
# expicit looping, indexing etc and let numpy do that for you

# create an array of the range of numbers from 0 to 15 (non-inclusive), reshape them into a
# 2d 3 x 5 array
my_np_array = np.arange(15).reshape(3,5)
print(my_np_array)

# What traits do numpy arrays have>
# ndim - Number of dimensions or axes
print(my_np_array.ndim)
# shape - dimensions of the array, tuple of integers indicating the size of the array in each dimension
print(my_np_array.shape)
# dtype - the data type - an object descripting the type of the elements in the array
# You can use python types, numpys types, or write your own
print(my_np_array.dtype)
# itemsize - the size in bytes of each elemetn in the array
print(my_np_array.itemsize)
# data - a reference to a buffer containing the actual data. Normally wont access this directly
print(my_np_array.data)
# This can be used to move into normal python code as it makes it into a list. 
print(my_np_array.data.tolist())

printnp(my_np_array)

# Creating NumPy arrays
# Lots of different ways you can do it
# you can pass in a list or tuple into the array function of numpy
# numpy will figure the type and size from
# to create a numpy array
# what you pass in
# REMEMBER: numpy arrays must be homogenous in type, and not be jagged


string_list = [["hi", "how", "are", "you"], ["goodby", "see", "you", "later"]]
# Optionally you can specify the dtype
string_array = np.array(string_list,dtype="<U20")
printnp(string_array)

print(string_array[1][2])
string_array[1][2] = 'yo'
printnp(string_array)
string_array[1][2] = 'the greatest show'
print(string_array)

# Often you'll knwo the size but not the contents
# If you don't know the size you can't create it!
# Growing arrays is expensive, so if you know the final size best
# to allocate it all at once instead of copying a bunch of times
zeroes = np.zeros((3,4), dtype="int32")
printnp(zeroes)
ones = np.ones((2,2,2))
printnp(ones)
empty = np.empty((20))
printnp(empty)

# Often people will us arange, reshaping it to a specified shape
arange = np.arange(10,100,5)
printnp(arange)
reshaped = arange.reshape(2,3,3)
printnp(reshaped)

# You can make any sequence into an array
# Want to transform a string into an array of characters?
# Make the string into a list, and use that to create the array
my_greeting = "Hi how are you doing?"
my_list = list(my_greeting)
print(my_list)
char_array = np.array(my_list)
printnp(char_array)