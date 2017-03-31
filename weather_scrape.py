
# Below is a link to a 10-day weather forecast at weather.com
# Use urllib and BeautifulSoup to scrape data from the weather table.
# Print a brief synopsis of the weather for the next 10 days.
# Include the day, date, high temp, low temp, and chance of rain.
# You can customize the text as you like, but it should be readable
# for the user.  You will need to target specific classes or other
# attributes to pull some parts of the data.
# (e.g.  Wednesday, March 22: the high temp will be 48 with a low of 35, and a 20% chance of rain). (25pts)
import urllib.request
from bs4 import BeautifulSoup

url = "https://weather.com/weather/tenday/l/USIL0225:1:US"
page=urllib.request.urlopen(url)
soup=BeautifulSoup(page.read(),"html.parser")

headers=[[ y.text.strip() for y in x.findAll("td")] for x in soup.find("table").findAll("tr",{"class":"clickable closed"})]

for i in range(len(headers)):
     print("On ",headers[i][1],"the weather will be",headers[i][2],"with a high of",headers[i][3][0:2],"and a low of",headers[i][3][2:],"with a precipitation chance of",headers[i][4],"and wind of",headers[i][5],"and a humidity of",headers[i][6])
