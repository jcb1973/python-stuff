import urllib
import urllib.request
from bs4 import BeautifulSoup
import re
from twilio.rest import Client

with open('config.txt') as f:
    conf = dict([line.split() for line in f])

TOKEN = (conf["TOKEN"])
SID = (conf["SID"])
TWILIOFROM = (conf["TWILIOFROM"])
TWILIOTO = (conf["TWILIOTO"])

account_sid = SID
auth_token = TOKEN
client = Client(account_sid, auth_token)

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
n = author.search(mystring)
if n:
	a = (upperfirst(n.group(1)))

message = cleantext + " (" + a + ")" 

client.api.account.messages.create(
    to=TWILIOTO,
    from_=TWILIOFROM,
    body=message)
