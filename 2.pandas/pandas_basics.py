import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)   
print(df.loc[0])

df = pd.DataFrame(data, index = ["day1", "day2", "day3"]) #Named Indexes

print(df) 

print(df.loc["day2"]) # Locate Named Indexes


df = pd.read_csv('data.csv')

print(df.head(10))

print(df.info()) 