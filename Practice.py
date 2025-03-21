import numpy as np

'''# One dimentional array

arr1 = np.array([1,2,3,4,5])
print(arr1)

# Two dimentional array
arr2 = np.array([[1,2,3],[4,5,6]])
# Three dimentional array

print(arr2)
arr3 = np.array([[[1, 2], 
                  [3, 4]], 
                  [[5, 6], 
                   [7, 8]]])


# Syntax=numpy.array(start, stop , step)
sequene=np.arange(0,10,2)
print(sequene)



import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Integer array indexing 
indices = np.array([1, 3, 5])
print ("Integer array indexing:", arr[indices])

cond=arr>30

print("Greater than 30 ", arr[cond])




import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Addition
add = x + y  
print("Addition:",add)

# Subtraction
subtract = x - y 
print("substration:",subtract)

# Multiplication
multiply = x * y 
print("multiplication:",multiply)

# Division
divide = x / y  
print("division:", divide)




Slicing of numpy 2D


import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])
'''
'''

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], 
                [6, 7, 8, 9, 10]])


        # row   col
print(arr[0:2, 1:3])'''

# # Output

# [[2 3]
#  [7 8]]


'''

# Create a sample 2-D array (a list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


last_row = matrix[-1]
print("Last Row:", last_row)


last_element_first_row = matrix[0][-1]
print("Last Element of First Row:", last_element_first_row)


last_two_elements_second_row = matrix[1][-2:]
print("Last Two Elements of Second Row:", last_two_elements_second_row)
'''







# importing pandas module 
import pandas as pd 

# making data frame 
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 

# calling head() method 
# storing in new variable 
data_top = data.head() 

# display 
data_top 




