import pandas as pd

# Load the two Excel files
roi_df = pd.read_excel('Trades_ROI.xlsx')  # Replace with the path to your ROI file
networth_df = pd.read_excel('Trades_Performance.xlsx')  # Replace with the path to your net worth file

# Display the first few rows to check the structure (optional)
print(roi_df.head())
print(networth_df.head())

# Merge the dataframes on the 'Name' column (adjust the column name if it's different)
combined_df = pd.merge(roi_df, networth_df, on='Name', how='outer')

# Display the combined dataframe (optional)
print(combined_df)

# Save the combined data to a new Excel file
combined_df.to_excel('combined_data.xlsx', index=False)
