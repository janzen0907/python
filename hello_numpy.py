import numpy as np

digits = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

for digit in digits:
    for i in digit:
        print("in Digit ", i )

print(digits.shape)