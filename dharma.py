import urllib
import urllib.request
from bs4 import BeautifulSoup
import re

def upperfirst(x):
	return x[0].upper() + x[1:]

hdr = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64'}
req = urllib.request.Request("http://quotes.justdharma.com/?fortune-cookie", headers = hdr)

response = urllib.request.urlopen(req)
page = response.read()
mystring = (page.decode("utf-8") )

author = re.compile('<a href="/\?fortune-cookie=.*">random quote by (.*?)</a>')
quote = re.compile('<div class="entry-content">.*<p>(.*)</p>', re.S)
m = quote.search(mystring)
if m:
	html_quote = m.group(1)
else:
	print ("no match")

cleantext = BeautifulSoup(html_quote, "lxml").text
print (cleantext)
n = author.search(mystring)
if n:
	print (upperfirst(n.group(1)))
