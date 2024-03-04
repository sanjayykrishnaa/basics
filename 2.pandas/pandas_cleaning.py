"""
This script demonstrates data cleaning techniques using pandas library.
"""

# Data Cleaning
    # Data cleaning means fixing bad data in your data set

import pandas as pd

df = pd.read_csv('data.csv')

print(df.dropna())  # Drop rows with missing values
print(df.fillna(130, inplace=True))  # Fill missing values with 130
print(df["Calories"].fillna(130, inplace=True))  # Fill missing values in "Calories" column with 130
x = df["Calories"].mean()
print(df["Calories"].fillna(x, inplace=True))  # Fill missing values in "Calories" column with the mean value
