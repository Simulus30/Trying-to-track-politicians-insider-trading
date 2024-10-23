"""
I had a bug where it would add one to the day number which was weird, I
couldn't figure it out but luckily it didnt actually effec the data, the
date was used more or less as a serial number to verify a duplicate trade
in conjunction with ticker name, politician name, and action
This existed to try and see if maybe my pc's time was timezone was wrong 
I tried changing it and it didnt do anything...but now if you wanna know
what time zone a website runs on...you can!
"""

import requests
import time
# Send a GET request to the website
response = requests.get('https://www.capitoltrades.com/trades?page=1')

# Print the response headers
print(response.headers)

# Check if a 'Date' or similar timestamp is present in the headers
if 'Date' in response.headers:
    print(f"Website Timestamp: {response.headers['Date']}")
else:
    print("No Date header found")