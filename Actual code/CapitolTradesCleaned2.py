import pandas as pd
import time

# Load the trading data from the Excel file
file_path = 'Location of where Scape saved the file'
data = pd.read_excel(file_path)

def convert_size(value):
    """Convert 'K' and 'M' formatted strings to integers."""
    if isinstance(value, str):
        if value.endswith('K'):
            return int(float(value[:-1]) * 1000)
        elif value.endswith('M'):
            return int(float(value[:-1]) * 1000000)
    return value  # Return the value as is if it doesn't match

# Convert Size_Min and Size_Max columns
data['Size_min'] = data['Size_min'].apply(convert_size)
data['Size_max'] = data['Size_max'].apply(convert_size)

# Create a new column for formatted date
data['Formatted_Date'] = data.apply(lambda row: f"{row['Day']:02d} {row['Month']} {str(row['Year'])[-2:]}", axis=1)

# Remove unnecessary columns
columns_to_drop = ['Day_Month', 'Year', 'Day', 'Month']
data = data.drop(columns=[col for col in columns_to_drop if col in data.columns])

# Save the cleaned data back to the same Excel file
data.to_excel(file_path, index=False)

# Notify when finishedprint(" ")
print(" ")
print(" ")
print("DONE! TIMES TWO!! ^u^")
print(" ")
print(" ")
print(" ")
print("Time to DELETE DA SHEET")
print(" ")
print("Running DeleteSheet!.py")

# Print ".  .  ." with a delay of 1.5 seconds between each "."
for _ in range(3):
    print(".", end=" ", flush=True)  # Print on the same line
    time.sleep(1)  # Wait for 1 seconds

print()  # Move to the next line after the loop

exec(open('DeleteSheet!.py').read())