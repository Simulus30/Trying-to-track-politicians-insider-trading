#enter python by putting ".\\AppData\Local\Programs\Python\Python313\python.exe" in the cmd terminal
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime
import pytz
import time

# Set the timezone to a named timezone (e.g., 'Pacific/Auckland')
nz_timezone = pytz.timezone('Pacific/Auckland')

# Get the current time in that timezone
current_time_nz = datetime.now(nz_timezone)
print("Current Time in Auckland (UTC+13):", current_time_nz) #idk wtf this is for but im scared to delete it


# Initialize the base URL
CT_base_url = 'https://www.capitoltrades.com/trades?page={}'

# Create a new workbook and select the active sheet
wb = Workbook()
ws = wb.active
ws.append(["Name", "Day_Month", "Year", "Action", "Size_min", "Size_max", "Ticker", "Day", "Month", "Price"])

# Iterate through pages 1 to 1000
for page_number in range(1, 3063):
    CT_url = CT_base_url.format(page_number)
    response = requests.get(CT_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <tr> tags with the specified class: "q-tr"
    row_elements = soup.select('tbody tr')

    # Extract and append data for each row
    for element in row_elements:
        name = element.select_one('td div h2 a')
        day_month = element.select_one('td:nth-child(4) div.text-size-3')
        year = element.select_one('td:nth-child(4) div.text-size-2')
        action = element.select_one('td:nth-child(7) div span')
        Volume_ = element.select_one('td:nth-child(8) span')
        ticker = element.select_one('td div h3 a')
        price = element.select_one('td:nth-child(9) div span')

        # Extract the "Size_min" and "Size_max" values
        size_text = Volume_.get_text() if Volume_ else ""
        size_min, size_max = size_text.split("–") if "–" in size_text else ("", "")

        # Extract the "Day" and "Month" values
        date_text = day_month.get_text() if day_month else ""
        date_day, date_month = date_text.split(" ") if " " in date_text else ("", "")
        # Check if each element is not None before calling get_text()
        row_data = [
            name.get_text() if name else "",
            day_month.get_text() if day_month else "",
            year.get_text() if year else "",
            action.get_text() if action else "",
            size_min.strip()if size_min else ",",
            size_max.strip()if size_max else ",",
            ticker.get_text() if ticker else "",
            date_day.strip() if date_day else "",
            date_month.strip() if date_month else "",
            price.get_text() if price else "",
        ]

        # Append the row to the sheet
        ws.append(row_data)
        # Display the current page number
    print(f"Scraping data from page {page_number}")

# Save the workbook
wb.save(f"Trades.xlsx")
print(" ")
print(" ")
print(" ")
print("DONE! ^u^")
print(" ")
print(" ")
print(" ")
print("Time for cleaning!")
print(" ")
print("Running CapitolTradesCleaned.py")

# Print ".  .  ." with a delay of 1.5 seconds between each "."
for _ in range(3):
    print(".", end=" ", flush=True)  # Print on the same line
    time.sleep(1)  # Wait for 1 seconds

print()  # Move to the next line after the loop

exec(open('CapitolTradesCleaned2.py').read())