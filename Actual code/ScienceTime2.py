import pandas as pd
import time

# Load the Excel file
file_path = 'YOU GUESSED IT TRADES.XLSX'
data = pd.read_excel(file_path)

# Ensure the column names are stripped of extra whitespace
data.columns = data.columns.str.strip()

# Debugging: Check the column names and the first few rows
print("Original DataFrame:")
print(data.columns.tolist())  # List of column names
print(data.head())            # First few rows of the DataFrame

# Check for NaN values in the 'Price' column
print("Number of NaN values in 'Price' column:", data['Price'].isna().sum())

# Remove '$' sign from 'Price' and convert relevant columns to numeric, coercing errors to NaN
data['Price'] = data['Price'].replace({'\$': ''}, regex=True)  # Remove dollar sign
data['Size_min'] = pd.to_numeric(data['Size_min'], errors='coerce')
data['Size_max'] = pd.to_numeric(data['Size_max'], errors='coerce')
data['Price'] = pd.to_numeric(data['Price'], errors='coerce')

# Clean the data by removing rows with missing values in the 'Price' column
df_cleaned = data.dropna(subset=['Price'])

# Debugging: Check the number of rows after cleaning
print(f"Number of rows after cleaning: {df_cleaned.shape[0]}")
print("First few rows of cleaned data:")
print(df_cleaned.head())

# Check unique values in the 'Action' column
print("Unique actions:")
print(df_cleaned['Action'].unique())

# Initialize a dictionary to hold estimated gains
performance_dict = {}

# Calculate estimated gains for each trade
for index, row in df_cleaned.iterrows():
    gain = 0  # Initialize gain for each row
    if row['Action'].lower() == 'buy':
        gain = -(row['Size_min'] * row['Price'])  # Buying results in a negative gain
    elif row['Action'].lower() == 'sell':
        gain = row['Size_max'] * row['Price']  # Selling results in a positive gain

    # Update the performance dictionary
    if row['Name'] in performance_dict:
        performance_dict[row['Name']] += gain
    else:
        performance_dict[row['Name']] = gain

# Convert the performance dictionary to a DataFrame
performance = pd.DataFrame(list(performance_dict.items()), columns=['Name', 'Estimated_Gain'])

# Fill NaN values with 0 for better summation (though there shouldn't be any NaN here)
performance['Estimated_Gain'] = performance['Estimated_Gain'].fillna(0)

# Rank individuals based on their estimated gains
performance = performance.sort_values(by='Estimated_Gain', ascending=False).reset_index(drop=True)

# Save the performance data to a new Excel file
performance.to_excel('WHERE EVER YOU WANNA SAVE THIS/Trades_Performance.xlsx', index=False)

# Display the ranked list
print(performance)

print(" ")
print(" ")
print(" ")
print("DONE! :O ")
print("I have caluclated the amount of money spent! ")
time.sleep(.5)  
print("Its fucking disgusting! ")
time.sleep(.5)  
print("All political leaders are not without fault!")
time.sleep(.5)  
print("Time to acutally see how crazy good they did!")
time.sleep(.5)  
print(" ")
print("Running ScienceTime3.py")

# Print ".  .  ." with a delay of 1.5 seconds between each "."
for _ in range(3):
    print(".", end=" ", flush=True)  # Print on the same line
    time.sleep(1)  # Wait for 1 seconds

print()  # Move to the next line after the loop
exec(open('ScienceTime3.py').read())