# Trying-to-track-politicians-insider-trading
I might have to change the code for scaping as they could have changed the website structure but ill be busy till like 
the end of November so...I guess we will do that then. I think the way i calculate ROI is bad but i actually have no 
idea how to make sure because YES they could be getting absolutely stupid returns upwards of what 600%? ...

this is the actual README that i made earlier:

dont forget to use pip install and then all the packages: pretty sure its just pandas, openpyxl, bs4, pytz, datetime

Order of operations (From scraping data to combining into the final form!):
CapitolTradesScrapped (!!!!DONT FORGET TO CHANGE PAGE RANGE AS YOU DESIRE! 
took me like 30 mins to do all 3k pages)

CapitolTradesCleaned2
DeleteSheet!
ScienceTime
ScienceTime2
Combine!

Final with all useful data: combined_data.xlsx
All trade data that was scrapped: Trades.xlsx

if you wanna try and improve it

Currently its setup so you can just run whatever step you want and it will 
complete the rest of the series so if you choose to not delete the big ass 
excel file ive included you can just run starting with 
CapitolTradesCleaned2.py

# IF YOU DONT WANNA AUTO RUN THE NEXT IN THE SERIES MAKE SURE:
you comment out the last line thats like "exec(open('NextInLine.py').read())"
