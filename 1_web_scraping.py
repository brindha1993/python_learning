from bs4 import BeautifulSoup # this module helps in web scrapping
import requests #  this module helps to download a webpage

url="http://www.ibm.com"

#getthe content of the webpage in text format and store in a variable called data
data=requests.get(url).text

soup=BeautifulSoup(data,"html.parser") # Create a soup object using the variable 'data'

# Scrape all links
for link in soup.find_all('a'):
  print(link.get('href'))

#scrape all images
for link in soup.find_all('img'):
  print(link.get('src'))

# Scrape data from html tables
URL= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

data=requests.get(URL).text

soup=BeautifulSoup(data,"html.parser")

#find a html table in the webpage
table=soup.find('table')

for row in table.find_all('tr'): # in html table row is represented by the tag <tr>:

# Get all columns in each row
  cols=row.find_all('td') # in html table, a column is represented by tag <td>
  color_name=cols[2].getText() # store the value in column 3 as color_name
  color_code=cols[3].getText() # store the value in column 4 as color_code
  print("{}--->{}".format(color_name,color_code))

from bs4 import BeautifulSoup
import requests

URL='https://en.wikipedia.org/wiki/World_population'

data=requests.get(URL).text

soup=BeautifulSoup(data,'html.parser')

for link in soup.find_all('a'):
  print(link.get('href'))

for img in soup.find_all('img'):
  print(img.get('src'))

