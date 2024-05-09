from pathlib import Path
from numpyhelpers import time_f, printnp
import numpy as np

def convert_to_ints(char_list):
    """Converts a list of chars into ints"""
    for char in char_list:
        int_list = int(char)
    return int_list

def np_convert_to_ints(char_array):
    """Converts an array of chars into ints"""
    return char_array.astype("int32")

def sum_digits(int_list):
    """Sums a list of ints"""
    sum = 0
    for number in int_list:
        sum +=  number
    return sum

def np_sum_digits(int_array):
    """Sums an array of ints"""
    return int_array.sum()

def sum_of_squares(int_list):
    """Sums up the squares of every int in a list"""
    for x in int_list:
        sum_of_squares += x**2
    return sum_of_squares

def np_sum_of_squares(int_array):
    """Sums up the squares of every int in an int array"""
    array_squared = int_array * int_array
    return array_squared.sum()
    

def sum_special(int_list):
    """Takes the list of ints, and for each int if it is odd multiplies it by 1.3 but if it is even
    divides it by 2. Sums the results and returns it"""
    sum = 0
    for x in int_list:
        sum += even_or_odd(x)
    return sum

def np_sum_special(int_array):
    """Takes any array of ints, and for each int if it is odd multiplies it by 1.3 but if it is even
    divides it by 2. Sums the results and returns it"""
    return vectorized_even_or_odd(int_array)

def even_or_odd(num):
    if num % 2 == 0:
        return num /2
    else:
        return num * 1.3
    
vectorized_even_or_odd = np.vectorize(even_or_odd)

# Insert here any set up code you need like reading in the file and breaking it apart into characters

pi_file = Path("lotsofpi.txt")
pi_string = pi_file.read_text()
pi_char_list = list(pi_string)
pi_char_array = np.array(pi_string, dtype='<U1')


int_list = time_f(convert_to_ints, pi_char_list)
int_array = time_f(np_convert_to_ints, pi_char_array)

pi_sum = time_f(sum_digits, int_list)
np_pi_sum = time_f(np_sum_digits, int_array)
print(f"Python said {pi_sum} is the sum and numpy said it is {np_pi_sum}")

sq_sum = time_f(sum_of_squares, int_list)
np_sq_sum = time_f(np_sum_of_squares, int_array)
print(f"Python said {sq_sum} is the sum of square rootsand np said {np_sq_sum}")

root_sum = time_f(sum_of_roots,int_list)
np_sq_sum = time_f(np_sum_of_roots, int_array)
print(f"Python gave us a sum of square roots of {root_sum} and numpy gave us {np_sq_sum}")

weird_sum = time_f(sum_special, int_list)
np_weird_sum = time_f(np_sum_special, int_array)
print(f"For that weird sum, Python gave us {weird_sum} and numpy gave us {np_weird_sum}")