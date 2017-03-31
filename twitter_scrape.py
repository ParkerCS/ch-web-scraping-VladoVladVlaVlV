# Go to your favorite follow on Twitter.  (not someone who posts explicit materials please)
# Inspect their twitter feed.
# You'll notice that the tweets are stored in a ordered list <ol></ol>,
# and individual tweets are contained as list items <li></li>.
# Use BeautifulSoup and urllib to grab the text contents of the tweets
# located on the twitter page you chose.  The .text attribute will supply the content of a soup object.
# Have fun.  Again, nothing explicit. (15pts)

import urllib.request
from bs4 import BeautifulSoup


url="https://twitter.com/nietzsche?lang=en"
page = urllib.request.urlopen(url)
soup=BeautifulSoup(page.read(),"html.parser")


data_list=[[y.text.strip() for y in x.findAll("div",{"class" : "js-tweet-text-container"})] for x in soup.findAll("ol")[1].findAll("li")]

for i in range(0,len(data_list),3):
    if i==15:
        i+=3
    print(str(data_list[i]))

