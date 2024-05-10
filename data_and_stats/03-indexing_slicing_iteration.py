import numpy as np
from numpyhelpers import printnp

# One-D arrays can be indexed, sliced and iterated just like python lists

# Multi-dimensional arrays can have one index, or slice, per dimension - pass them in a tuple (seperate by ,s)
threed_nums = np.arange(3*4*3).reshape(3,4,3)
printnp(threed_nums)
printnp(threed_nums[2,3,1])
print("Slice:")
printnp(threed_nums[:,1:3,:2])
# If you give fewer indexes than there are dimensions, the missing indices are considered complete slices
printnp(threed_nums[1:2])
# Can use negatives 
printnp(threed_nums[-1])
printnp(threed_nums[-1, -1, -1])

# If you want to flatten it out into an iterator to go over every item you can use flat
for element in threed_nums.flat:
    print(element)

# If you want a flattened array instead of an iterator you can use flatten():
printnp(threed_nums.flatten()) # returns a copy of the original array
# If you just want a view of an array that's flat not copy it, use ravel
printnp(threed_nums.ravel()) # Gives you original data in a different view

# Combining arrays
one = np.arange(15)
two = one * 3
print(one)
print(two)
# vstack takes a tuple of arrays and stacks them vertically
print("Vertical:")
printnp(np.vstack((one,two)))
print("Horizontal:")
printnp(np.stack((one,two)))
print("Column")
printnp(np.column_stack((one,two)))
# Can transpoe 
printnp(np.column_stack((one,two)).transpose())

# Assignment just returns the reference
first = np.arange(25).reshape(5,5)
second = first
printnp(second)
printnp(first)
second[2,3] = 1000
printnp(second)
printnp(first)
# Lots of operations will copy an array, sometimes you want a shallow copy
# a shalllow copy is called a view - it has teh data buffer, but can have different shape and such
second = first.view()
second = second.reshape(25)
printnp(first)
printnp(second)
second[10] - 999999
printnp(first)
printnp(second)
