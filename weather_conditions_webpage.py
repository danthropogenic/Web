######################################################################
# weather_conditions_webpage.py
# Collect information on current conditions that I'm interested in 
# and output to an html file
# Written by Dan Sulak
######################################################################


import requests
from bs4 import BeautifulSoup as bs 
 
# start the string for the html file output
output = """<html lang="en">
<head>
	<meta charset = "UTF-8">
	<title>Latest Conditions</title>
</head>
<body>"""
 
# make a class for different soups
class Soup:
	def __init__(self,url):
		self.url = url
		self.html = requests.get(self.url).text
		self.soup = bs(self.html,"html.parser")
		
# get the latest snowfall at stevenspass
sp = Soup("https://www.stevenspass.com/site/mountain/reports/snow-and-weather-report/@@snow-and-weather-report")

# find the latest snow reported and the amounts
sps_updated = sp.soup.find_all(class_="snow_and_weather-report-updated-block")
sps_base_snowfall = sp.soup.find_all(class_="row_boxes row_boxes-3-boxes clearfix")[0]

# add the stevenspass info to the oupput
output = output + str(sps_updated) + str(sps_base_snowfall)


# get the latest from cliff mass

# get the website text, make the soup
cm = Soup("https://cliffmass.blogspot.com")

# get the latest post 
cm_dat = cm.soup.find_all("span")[1]
cm_tit = cm.soup.find_all(class_="post-title entry-title")[0]
cm_bod = cm.soup.find_all(class_="post-body entry-content")[0]

# add cliff mass's post to the output
output = output + str(cm_dat) + str(cm_tit) + str(cm_bod)

# finish the output and write the file
output = output + "</body>\n</html>"

with open("index.html",'w',encoding='utf-8') as f:
	f.write(output)
	


