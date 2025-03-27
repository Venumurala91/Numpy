import pandas as pd


df = pd.read_csv("D:\data science course_documents\cricket_data_2025.csv")


# print(df.columns)
# print(list(df.columns))
# # print(df.head)())
# print(df.mean)


# print(df.describe())
# # print(df.shape) #(1008, 25)


# d=df.duplicated().sum()
# print(d)
# # print(df.shape) #(1008, 25)

# remove_duplicates=df.drop_duplicates(inplace=True)

# # print(remove_duplicates)
# print(df.shape) #(1008, 25)

#Check for missing values
# print(df.isnull().sum())

#Drop rows with missing valiues and place it in a new variable "df_cleaned"
'''df_cleaned = df.dropna()
print(df_cleaned)

print(df_cleaned.shape)


print(df_cleaned['Player_Name'].unique())
df_cleaned=df.drop_duplicates()

print(df_cleaned.shape)
'''



# print(df.iloc[1:10][['Highest_Score']])


top_scores = df.groupby('Player_Name')['Highest_Score'].sum().nlargest(10)

# Display the top 10 players with the highest total runs
print(top_scores)
