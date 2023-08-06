import pandas as pd

# Load the merged CSV file
merged_df = pd.read_csv('merged_stars.csv')

# List all the columns of the data
print("Columns before deleting unnecessary columns:")
print(merged_df.columns)

# Delete the unnecessary columns (Luminosity)
unnecessary_columns = ['Luminosity']
merged_df.drop(columns=unnecessary_columns, inplace=True)

# List all the columns of the data after deleting unnecessary columns
print("\nColumns after deleting unnecessary columns:")
print(merged_df.columns)

# Remove duplicate columns (if any)
merged_df = merged_df.loc[:,~merged_df.columns.duplicated()]

# Delete rows with NaN values
merged_df.dropna(inplace=True)

# Save the cleaned data to a new CSV file
cleaned_merged_csv = 'cleaned_merged_stars.csv'
merged_df.to_csv(cleaned_merged_csv, index=False)

print("\nCleaned and processed data saved to 'cleaned_merged_stars.csv'")
