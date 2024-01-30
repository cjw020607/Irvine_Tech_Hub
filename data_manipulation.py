import pandas as pd

# Read CSV file
file_path = 'OliveYoung_Results.csv'
df = pd.read_csv(file_path)

# Remove commas (,) and convert 'Original Price' and 'Current Price' columns to numeric
df['Original Price'] = pd.to_numeric(df['Original Price'].str.replace(',', ''), errors='coerce')
df['Current Price'] = pd.to_numeric(df['Current Price'].str.replace(',', ''), errors='coerce')

# Remove '+' and convert 'Number of Reviews' column to numeric
df['Number of Reviews'] = pd.to_numeric(df['Number of Reviews'].str.replace('+', ''), errors='coerce')

# Fill NaN with 0
df['Number of Reviews'].fillna(0, inplace=True)

# Calculate 'Discount Price'
df['Discount Price']=df['Original Price']-df['Current Price']

# Calculate 'Discount Rate'
df['Discount Rate']=((df['Original Price']-df['Current Price'])/df['Original Price']*100).round(1)

# Create 'Popularity Ranking' column and assign the current row order
df['Popularity Ranking'] = df.index + 1

# Convert the result to integers
df['Number of Reviews'] = df['Number of Reviews'].astype(int)

# Save the modified DataFrame to a new CSV file
df.to_csv('OliveYoung_Results_Preprocessed.csv', index=False)

