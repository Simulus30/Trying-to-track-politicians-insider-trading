# Trying-to-track-politicians-insider-trading
this assumes you have python working and are able to move through it decently, I reccomend using VS code as you can 
one get it set up pretty easily and two try out several different languages with different enviorments AND switch 
between the rather easily.
### Assumptions that you have the following: 
Python 3.13.0
*this is all the packages, im sure if you just pip install pandas, openpyxl, bs4, pytz, datetime you should be fine*
  + beautifulsoup4     4.12.3
  + bs4                0.0.2
  + certifi            2024.8.30
  + charset-normalizer 3.4.0
  + DateTime           5.5
  + et-xmlfile         1.1.0
  + idna               3.10
  + numpy              2.1.2
  + openpyxl           3.1.5
  + pandas             2.2.3
  + pip                24.2
  + python-dateutil    2.9.0.post0
  + pytz               2024.2
  + requests           2.32.3
  + setuptools         75.1.0
  + six                1.16.0
  + soupsieve          2.6
  + tzdata             2024.2
  + urllib3            2.2.3
  + zope.interface     7.1.0

  
dont forget to use pip install and then all the packages: pandas, openpyxl, bs4, pytz, datetime
in the terminal (once you first start with VS code youll have to manuall install all packages you want, do this at the 
terminal in the bottom, the text should be someting like "PS C:\Users\YourName\Workspace ") fun fact if youre in this
terminal and you type "py" the part where it says "PS C:\Users\YourName\Workspace" it will change colors and go to 
">>>" and BOOM you have a python terminal.

### I strongly reccomend:
learning python on [this playlist](https://www.youtube.com/watch?v=6i3e-j3wSf0&list=PL0Zuz27SZ-6MQri81d012LwP5jvFZ_scc), helped me a lot. I think his installation tutorial isnt that great because I cannot 
stress this enough
### When installing python make sure to add it to path
IDK how or why but whenever I do it without adding to path it will not work


## Order of operations (From scraping data to combining into the final form!):
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

## IF YOU DONT WANNA AUTO RUN THE NEXT IN THE SERIES MAKE SURE:
you comment out the last line thats like "exec(open('NextInLine.py').read())"


## known issues:
### Scrapped:
It doesnt use the same kind of way to call to each of the different pieces of data...TBH I
just did several different things and made sure it worked
  For example: to get the name it calls to "'td div h2 a'" 
  but to call to day_month it uses: "'td:nth-child(4) div.text-size-2'"
  this is fine for now...until they change the site, day_month just looks at the previously
  defined " row_elements = soup.select('tbody tr') " and then using the " td:nth-child(4) " 
  it counts down the to the 4th td and then  looks for a division with text size of 2 and
  copies it...so god forbid they either reorganzise the way the columns are
It also has been adding 1 to the date? It doesnt really matter in the grand scheme especially
since we are trying to cast a wide net of who trades well and who doesnt. 
### ScienceTime3
Pretty sure the way im calculating ROI is wrong and I have no idea if python is actually doing
what I want it to
  It (in lines 23 to 46) SHOULD be deviding the bought price by the sold price, saving that value
  then (in lines 41 to 48) average all of them for each person.
* I think Ill test this by doing it by hand on certain ones? But I think I would have to add a name
filter that only scrapes data from a specific name and then hand jam it to figure out if they have
an ROI that matches...or even comes close*

### Hey thanks for bein here!
I worked pretty hard on this and am proud of it...even though it doesnt really work or at least I
think it doesnt work, at the end of the day...im just out here trying to make a stupid amount of
money with minimal effort in the long term. Also, to say my peace on this...YES insider trading is 
terrible. I fear it creates a blinding effect to our political leaders that doesnt make them actually
look out for the good of the people and rather focuses them to vote in a way that will maximize profit 
irregardless of who wins out or not. **Can you actually blame them?** Honestly...No, I dont think anyone 
could see this happening and decide "hmmm yes company A will get a fat govenment grant here next month...
I choose to put my life savings into a 5% yeild mutual fund"
The rules are made up and the points dont matter
