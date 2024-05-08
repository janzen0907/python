import numpy as np
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
print(my_np_array.data.tolist())

