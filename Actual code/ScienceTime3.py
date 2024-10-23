import pandas as pd
import time

# Load the Excel file
file_path = 'ONE LAST TIME! TRADES.XLSX'
data = pd.read_excel(file_path)

# Ensure the column names are stripped of extra whitespace
data.columns = data.columns.str.strip()

# Remove '$' sign from 'Price' and convert relevant columns to numeric, coercing errors to NaN
data['Price'] = data['Price'].replace({'\$': ''}, regex=True)  # Remove dollar sign
data['Size_min'] = pd.to_numeric(data['Size_min'], errors='coerce')
data['Size_max'] = pd.to_numeric(data['Size_max'], errors='coerce')
data['Price'] = pd.to_numeric(data['Price'], errors='coerce')

# Clean the data by removing rows with missing values in the 'Price' column
df_cleaned = data.dropna(subset=['Price'])

# Initialize a dictionary to hold investments and returns
performance_dict = {}

# Calculate investments and returns for each trade
for index, row in df_cleaned.iterrows():
    name = row['Name']
    price = row['Price']
    
    if name not in performance_dict:
        performance_dict[name] = {'investment': 0, 'return': 0}

    if row['Action'].lower() == 'buy':
        investment = row['Size_min'] * price  # Investment when buying
        performance_dict[name]['investment'] += investment
    elif row['Action'].lower() == 'sell':
        return_value = row['Size_max'] * price  # Return when selling
        performance_dict[name]['return'] += return_value

# Initialize a list to hold ROI results
roi_results = []

# Calculate ROI for each person
for name, values in performance_dict.items():
    investment = values['investment']
    return_value = values['return']
    
    if investment > 0:  # Avoid division by zero
        roi = ((return_value - investment) / investment) * 100  # Calculate ROI
        roi_results.append({'Name': name, 'ROI': roi})

# Convert ROI results to a DataFrame
roi_df = pd.DataFrame(roi_results)

# Calculate the average ROI
average_roi = roi_df['ROI'].mean()

# Create a DataFrame for the average ROI
average_roi_df = pd.DataFrame({'Name': ['Average'], 'ROI': [average_roi]})

# Combine the ROI DataFrame with the average ROI DataFrame
roi_df = pd.concat([roi_df, average_roi_df], ignore_index=True)

# Sort the DataFrame by 'ROI' in descending order
roi_df = roi_df.sort_values(by='ROI', ascending=False).reset_index(drop=True)

# Save the performance data to a new Excel file
roi_df.to_excel('WHERE EVER YOU WANNA SAVE THIS/Trades_ROI.xlsx', index=False)

# Display the ROI results
print(roi_df)

print(" ")
print(" ")
print(" ")
print("DONE! :O ")
print("I have caluclated the ROI ")
time.sleep(.5)  
print("Its STILL ")
time.sleep(.5)  
print("FUCING")
time.sleep(.5)  
print("DISGUSTING")
time.sleep(.5)  
print(" ")
print("Running Combine!.py :) ")

# Print ".  .  ." with a delay of 1.5 seconds between each "."
for _ in range(3):
    print(".", end=" ", flush=True)  # Print on the same line
    time.sleep(1)  # Wait for 1 seconds

print()  # Move to the next line after the loop
exec(open('Combine!.py').read())