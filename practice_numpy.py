'''''

# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])

# '''
# print("Shape:", arr.shape)  
# print("Dimensions:", arr.ndim)  
# print("Size:", arr.size) 
# print("Data type:", arr.dtype)  
# print("Item size:", arr.itemsize)  

# '''

# # print(arr[1][3])        


#2d array
# import numpy as np


# arr=np.array([[1,2,3], 
#              [4,5,6]])

# print(arr[1,1:3])

'''import numpy as np

matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

# Slicing with step
 # Skip every other row and column
sliced_matrix = matrix[::2, ::2] 
# print(sliced_matrix)



print(matrix[:4,2])

print(matrix[1:3,1:3])

'''



# #3d array

# import numpy as np
# arr=np.array([[[1,2,3],
#               [4,5,6],
#               [7,8,9],
#                [10,11,22]]])

# print(arr.ndim)
# print(arr)

# print(arr[1,1:2])

'''

import numpy as np

# Create a 3-D NumPy array
array = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
])


'''

# print(array.shape)

# print(array[0:3])
# print(array[1:2,0:3,1:3])
# print(array[1:4,1:4])

# print(array[0:4,1:4,1:3])



# array[start_depth:end_depth, start_row:end_row, start_column:end_column]


# Creation of array's


'''import numpy as np 

#create an array 
arr= np.arange(5 , 10)
print(arr)
'''

'''

import numpy as np
import pandas as pd
sex = pd.Series(['Male','Male','Female'])

np.array(sex)
'''



'''# linespace in numpy 


import numpy as np

# array=np.linspace(10,100,10)
# print(array)

array=np.arange(5,50,5)
print(array)

'''

# copy vs view

'''
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)
'''
'''
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)



'''
# difference between copy and view 

# copy :After copying array if we can change anything in array it will not change in copied array 
# view: After viewing array if we can change anything in array it will change both the array's

'''
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)

# output

[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
'''
'''



output : (array([3, 5, 6]),)
'''''''''
''
''


# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 4, 4])

# x = np.where(arr == 4)

# print(x)



# import numpy as np

# # Creating a 3x5 rectangular matrix
# rectangular_matrix = np.eye(3, 5)
# print(rectangular_matrix)


# data = np.eye((1))


# Python Programming illustrating 
# numpy.full method 

import numpy as geek 

a = geek.full([2, 2], 67, dtype = int) 
print("\nMatrix a : \n", a) 

c = geek.full([3, 3], 10.1) 
print("\nMatrix c : \n", c) 
