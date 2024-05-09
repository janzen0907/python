import numpy as np
from numpyhelpers import printnp, time_f

# Artimetic operations are applied elementwise. A new array is created and filled with the result
a = np.array([10,20,30,40])
printnp(a)
# Applies to each element indivdually. This would subtract 1 from every element in the array
b = a -1 
printnp(b)
c =  b * a
printnp(c)
# You can do matrix multiplication with @ if you want
first = np.array([[1,1],[0,1]])
second = np.array([[2,0], [3,4]])
print(first @ second)

# Some operators like *= or += will act in place to modify an array rather than generate a new one
ones = np.ones((2,6))
printnp(ones)
one_two = np.array([1,2,1,2,1,2])
print(one_two)

ones *= one_two
printnp(ones)

# Note that this is a case of "broadcasting" - if the arrays are not of the same size,
# the smaller array is "broadcast" across the larger array. This is what happens if you use a constant
# Stretches the array across
print(ones + 10)
# When can you broadcast?
# YOu can broadcast when each dimension in both arrays are equal, or one of the dimensions is 1, matching from the *right*
# Missing dimensions are assumed to be 1
incompatable = np.array([
    [
        [1],[10],[100],[1000],[10000],[100000]
    ],
    [
        [1],[1],[1],[1],[1],[6]
    ]
])
printnp(incompatable)
# This will not work. Ones is treated as (1,2,6) because it has one less dimension, and isn't capatible with (2,6,1)
# print(ones + incompatable)

# If we operate on arrays of different types, the result is going to get upcast to the more general or precise one
int_array = np.array([1,2,3], dtype="int64")
small_int_array = np.array([4,6,7], dtype='int8')
printnp(int_array)
printnp(small_int_array)
# Would end up with a int64 
printnp(int_array + small_int_array) 
float_array = np.array([9,10,11], dtype="float")
printnp(float_array)
# Would end up with float64
printnp(int_array * float_array)

# Some functions which operate on a whole array
numbers = np.array([[1,2,3,4,5],[10, 20 , 30 , 40 , 50]])
print("Numbers:")
printnp(numbers)
print(numbers.sum())
#ndarray.sum() is actually equivalent to numpy.sum(ndarry) - it is just convience so you can do it on an array easily
# By default, these types of functions flatten the array and treat it as one big one d array
print(numbers.flatten())
# YOu can specify an azis to operate on instead
print(f"Sum on axis 0: {numbers.sum(axis=0)}")
print(f"Sum on axis 1: {numbers.sum(axis=1)}")

# There are tons of numpy functions - most of which operate elementwie , some operate on whole array
# If you're looking for a mathematical function, it's probably there

# There's a whole class of functions called "ufuncs" or universal functions which operate on ndarrays
# in an elemebt-by-element fashion, they've got common options. They are "vectorized" - they work on array
# You can write your own ufuncs if you need to
numbers = np.array([[60,-1,20], [-22,545,-292]])
print(np.abs(numbers))

# You can use astype to try and convert betwene types for an entire array
# This is differnet than sum because it is affecting ndarray and is specific to it
string_as_numbers = np.array(['232','532','3425', '22', '41'])
printnp(string_as_numbers)
numbers = string_as_numbers.astype('int32')
printnp(numbers)

# Can write our own if numpy function does not exist
# Some functions numpy can handle or vectorize pretty easily

def add_3(number):
    return number + 3

print(add_3(7))
# This will work
print(add_3(numbers))

def double_odd_numbers(number):
    if number % 2 == 0:
        return number
    else:
        return number *2
    
print(double_odd_numbers(7))
# This will not work
#print(double_odd_numbers(numbers))

# YOu can vectorize a function to change it to a functionn that when
# you pass in an array it runs the function on each elemetn in the array
vectorized_double_odd_numbers = np.vectorize(double_odd_numbers)
print(vectorized_double_odd_numbers(numbers))


thousan = np.arange(1000)
def sum_array(array):
    return array.sum()

result = time_f(sum_array, (thousan))
print(result)
