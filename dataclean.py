import pandas as pd

# Load the dataset (replace 'data.csv' with your file)
data = pd.read_csv('data.csv')

# Remove rows with null values
data_cleaned = data.dropna()

# Remove duplicate rows
data_cleaned = data_cleaned.drop_duplicates()

# Save the cleaned data to a new file
data_cleaned.to_csv('cleaned_data.csv', index=False)