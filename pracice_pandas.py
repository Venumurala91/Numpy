'''
Pandas : It is used to work with data manipulation and data analysis

topics in pandas

-------------------------------------------------------------------------series= series is a one dimentional labeled array

Head/Tail: head(), tail()

Summaries: sum(), mean(), min(), max(), unique(), value_counts()

Handling Nulls: isnull(), notnull()

Transformation: apply(), map()

Sorting: sort_values()

Type Conversion: astype()

String Methods: str.upper(), str.contains(), etc.



---------------------------------------------------------dataFrame is a two dimentional labelled axex (rows and columns)

Summary of Key Functions for DataFrames:
Data Inspection: head(), tail(), info(), describe(), shape

Selecting Data: .loc[], .iloc[], column selection, row filtering

        loc -- labelled based indexing using names of column 
        iloc --  position based indexing 



Adding/Removing Data: Add columns, drop() rows/columns

Sorting: sort_values()

Handling Missing Data: isnull(), dropna(), fillna()

Merging/Joining: merge()

Grouping and Aggregating: groupby(), pivot_table()

File Operations: read_csv(), to_csv(), read_excel(), to_excel()


import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Access a column
print(df['Age'])

# Filter the DataFrame
print(df[df['Age'] > 25])


'''

# Creating series

'''
import pandas as pd 
import numpy as np

# Creating empty series 
ser = pd.Series() 
print("Pandas Series: ", ser) 

# simple array 
data = np.array(['g', 'e', 'e', 'k', 's']) 

print(data)  
ser = pd.Series(data) 
print("Pandas Series:\n", ser)
print(pd.DataFrame(data))


'''
'''

import pandas as pd 
  
# Calling DataFrame constructor 
df = pd.DataFrame() 
print(df)

# list of strings 
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks'] 
  
# Calling DataFrame constructor on list 
df = pd.DataFrame(lst) 
print(df)


import numpy as np
import pandas as pd

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
print(df)



import pandas as pd

# Creating a Series from a Python list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

print(series)

'''

# import pandas as pd
'''
# Creating a Series from a Python list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

print(series)



# Series with mixed data types
data = [1, 3.5, 'Hello', True,3]
series = pd.Series(data)

# print(series)



# print(series.head(2))  # First 2 elements
# print(series.tail(2))  # Last 2 elements


# print(series.dtype)
print(series.index)


data = [10, 20, 30]
series = pd.Series(data)
print(series.sum())  # Output: 60'''


'''
import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# print(df)
print(df)


print(df.iloc[1])
'''
'''
import pandas as pd

# Grouping by 'City' and calculating the average Age
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles']
}
df = pd.DataFrame(data)

grouped = df.groupby('City').mean()
print(grouped)


'''

'''

# Import pandas package
import pandas as pd

# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
		'Age':[27, 24, 22, 32],
		'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
		'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
print(df)

# select all rows 
# and second to fourth column
df[df.columns[1:4]]

print(df[df.columns[1:4]])
'''




import pandas as pd

# Read the Excel file
data = pd.read_excel("D:/Data science course_documents/test101.xlsx")

# Print the 'name' column
# print(data[['Name', 'Age']])



# filtered_data = data[data['Age'] > 35]


# print(filtered_data.describe())

# d=data.isnull()

# for i in data.isnull():
#     print(i['Name'])

# # print(d)
# null_columns = data.columns[data.isnull().any()].tolist()
# print(null_columns)

rows_with_nulls = data[data.isnull().any(axis=1)]

# Print the 'Name' column of those rows
print("Names of rows with null values:")
print(rows_with_nulls['Name'])



#print(total_salary)

d= data[data['Salary']>85000]
print(d)


print('----------------------')

print(data.head(2))
print(data.tail(5))
print(data.info)


print('----------------------')
print('----------------------')

# Drop rows with any null value


# Fill missing values in the 'Age' column with a specific value
data['Age'] = data['Age'].fillna(0)

print(data)
# # Fill missing values with the column's mean
# data['Age'] = data['Age'].fillna(data['Age'].mean())
