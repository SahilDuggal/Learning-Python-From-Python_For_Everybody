# Web Scraping is a program that fakes to be a browser that visits a web page
# and extracts information.
# Also known as spidering the web or web crawling.
 
#  Beautiful Soup is used to easily get through the HTML's syntax errors.
#       We can install Beautiful Soup 2 ways:
#           1. Install it on your device globally or,
#           2. Install it in the folder in use.(I did this)
from bs4 import BeautifulSoup 
import urllib.request, urllib.parse, urllib.error
import ssl

# to access https websites:
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the url:- ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
 