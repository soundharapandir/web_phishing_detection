
import ipaddress
import re
import urllib.request from bs4 import BeautifulSoup
import socket import requests
from googlesearch import search
import whois
from datetime import datetime
import time
from dateutil.parser import parse as date_parse
#Calculates number of months
def diff month(d1, d2): return (d1.year - d2.year)
#Generate data set by extracting the features from the URL
def generate_data_set(url):
data_set = []
# Converts the given URL into standard format if not re.match(r""https?", url):
url = "http://" + url
# Stores the response of the given URL
try:
response requests.get(url) soup BeautifulSoup (response.text, 'html.parser')
except:
response
soup-999
* Extracts domain from the given URL
domain- re.findall(e"://([^/]+)/?", url)[0] if re.match(".", domain):
domain- domain.replace("Mr.","")
Requests all the information about the domain whois_response whois.whois
(domain)
rank_checker response
requests.post("https://www.checkpagerank.net/index.php", { "name":
domain)
#Extracts global rank of the website
try:
global_rank = int(re.findall(r"Global Rank: ([0-9]+)",
rank_checkerresponse.text)[0])
ipaddress.ip_address(url)
data_set.append(-1)
except:
data set.append(1)
2.URL Length
if len(url) < 54:
data set.append(1)
elif len(url)
54 and len(url) < 75:
data set.append(0)
else:
data set.append(-1)
3.Shortining Service
matchere.search("bit.ly/goo.gl/shortel.st/go21\.ink|x\,colou\.ly/t.co/tinyurl|tr
\.in/is.gd/cli\.pyfrog.com/igre\.selff\.in/tiny.cc/ur14\.eu/twit\,ac/sul.pr|tuur1.
nl/snipurl.com/
short\.to/BudURL.com/ping\.fm/post\.ly/Just\.es/bkite\.com/snipr\.com/fic\.k
r|loopt\.usdoiop\.com/short\.ie/kl\.|up\.ae/rubyurl.com/on\.ly/tal.ly/bit.do/t.
co/Inkd\.in]db\.tt/gr\.ae/adf.ly/goo.gl/bitly.com/cur\.Iv/tinyurl.com/ow.ly/bit.l
y|ity\.im|generate dataset)
elif
lentre.findall())...gs/is.gd/po.st/bc.vc/twitthis\.com/ul.to/j.mp/buzurl\.c
om/cutt\.us/u\.bblyourls\.org/
x.co/prettylinkpro\.com/scrnch\.ne|filoops\.info/vzturl\.com/qr\.net|1u
rl.com/tweez\.me/v\.gd/tr\.in|Link\.zip\.net", url)
if match:
data_set.append(-1)
else:
data_set.append(1)
#4. having At Symbol if re.findall("@", url):
data_set.append(-1)
else:
data set.append(1)
#5.double slosh_redirecting
list [x.start(0) for x in re.finditer('//', url)]
if list[len(list)-1]>6: data_set.append(-1)
else:
data_set.append(1)
6. Prefix Suffix
if re.findall(r"https?://[^\-]+[^\-]+/", url): data set.append(-1)
else:
data_set.append(1)
#7, having Sub Domain
if len(re.findall("\.", url)) = 1: data set.append(1) elif len(re.findall(".", url)) - 21
data set.append(e)
else:
data set.append(-1)
# 8final State
try:
if response.text:
data set.append(1)
except:
data set.append(-1)
#9.Domain_registeration Length
expiration_date whois_response.expiration_date registration_length - 8
try:
expiration date- min(expiration_date)
today time.strftime("%Y-%m-%d')
today datetime.strptime(today, "Y-%m-%d') registration_length
abs((expiration_datetoday).days)
if registration_length / 365 <- 1:
data set.append(-1)
else:
data set.append(1)
except:
data set.append(-1)
10. Favicon
if soup -999: data set.append(-1)
else:
try:
for head in soup.find_all("head"):
for head.link in soup.find_all('link", href=True):
dots [x.start(e) for x in re.finditer("\.,head.link['href'])]
if url in head.link['href'] or len(dots) 1 or domain in head. link["href"]:
data set.append(1)
raise StopIteration
else:
data set.append(-1)
raise StopIteration
except :
StopIteration: pass
#11. Port
try:
port domain.split(":")[1]
if port:
data_set.append(-1)
else:
data set.append(1)
except:
data set.append(1)
#12. HTTPS_token
if re.findall(r""https://", url):
data set.append(1)
else:
data set.append(-1)
#13. Request URL
success
if soup-999:
data set.append(-1)
else:
for ing in soup.find_all('Ing', srce True): dots- [x.start(8) for x in
re.finditer("\.,ing['src'])]
if url in ing['src'] or domain in ['src'] or len(dots)==1:
success - success + 1
for audio in soup.find_all("audio", srce True): dets [x.start(0) for x in
re.finditer(".", audio["src"]}]
if url in audio['src'] or domain in audie['src'] or len(dots)-l
success success + 1
for embed in soup.find_all("embed", srce True): dots-[x.start() for x in
re.finditer(".", embed["src"])]
if url in embed["src"] or domain in embed['src'] or len(dots)==11
success success + 2
i=i+1
for iframe in soup.find_all('iframe', src= True):
dots [x.start(0) for x in re.finditer('\., iframe['src'])] if url in iframe['src'] or
domain in iframe['src'] or len(dots)==1:
success success + 1
i=i+1
try:
percentage = success/float(i)
if percentage < 22.0 :
dataset.append(1)
elif((percentage >= 22.0) and (percentage < 61.0)) :
else:
data_set.append(e)
data_set.append(-1)
except:
data_set.append(1)
#14. URL of Anchor
percentage=0
i-0
unsafe=0
if soup-999:
data_set.append(-1)
else:
for a in soup.find_all('a', href=True):
# 2nd condition was "JavaScript ::void(0)' but we put JavaScript because the
space between javascript and might not bethere in the actual of 'href']
if "a" in a["href"] or "javascript" in[a['href'].lower() or "mailto" in
a['href'].lower() or not (url in a['href'] or domain in a['hre unsafe unsafe + 1]
i=i+1
try:
percentage = unsafe / float(i) -100
phishing detection.py
forest.py
except:
data set.append(1)
if percentage < 31.0:
data set.append(1)
elif ((percentage > 31.0) and (percentage < 67.0)):
data_set.append(0)
else:
data set.append(-1)
#13. Request URL
i = 0
success
if soup-999:
data_set.append(-1)
else:
for ing in soup.find_all('img src= True):
dots [x.start(e) for x in re. finditer(\., img['src'])] if url in img['src'] or
domain in img['src'] or len (dots)==1: success = success + 1
i=i+1
for audio in soup.find_all('audio, src- True):
dots [x.start(e) for x in re.finditer('\., audio['src'])] if url in audio['src'] or
domain in audio['src'] or len(dots)==1: i=i+1
success = success + 1
for embed in soup.find_all('embed', src= True):
dots=[x.start(0) for x in re.finditer('\.", embed['src'])]
if url in embed['src'] or domain in embed['src'] or len(dots)==1:
success success + 1-1+1
