import urllib2
import re 

response = urllib2.urlopen('http://gandul.info')
print response.info()
html = response.read()

# the regex stolen from the net
print re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', html)

response.close()  # best practice to close the file