import pandas as pd

# Load data from CSV (replace 'data.csv' with your file)
data = pd.read_csv('data.csv')

# Convert data to JSON and save to a new file
data.to_json('data.json', orient='records')
