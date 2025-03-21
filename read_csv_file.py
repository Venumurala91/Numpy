# '''
# import pandas as pd

# # Provide the file path
# file_path = r"C:\Users\Venugopal\Documents\test.csv"

# # Read the CSV file into a DataFrame
# df = pd.read_csv(file_path)

# # Display the first few rows of the DataFrame
# print(df.head())
# '''

import pandas as pd


file_path = r"C:\Users\Venugopal\Documents\test.csv"

df = pd.read_csv(file_path)

print("First few rows of the dataset:")
print(df.head())


print("\nExtracted columns (Name and Salary):")
print(df[['Name', 'Salary']])


print("\nPeople with Salary > 80,000:")
print(df[df['Salary'] > 80000])
