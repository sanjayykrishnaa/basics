import pandas as pd

# Read data from a CSV file and assign it to a DataFrame
df = pd.read_csv('data.csv')

# Print the DataFrame
print(df)

# Read data from a CSV file and assign it to a DataFrame, then convert it to a string and print
df = pd.read_csv('data.csv')
print(df.to_string())

# Example DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']}

# Create a DataFrame from the example data

df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
df.to_excel('example.xlsx', index=False, engine='openpyxl')

# Write the DataFrame to a CSV file
df.to_csv('example.csv', index=False)

# Write the DataFrame to a JSON file
df.to_json('example.json', orient='records')