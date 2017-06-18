import urllib2

url = raw_input("URL: ")
response = urllib2.urlopen(url)
html = response.read()

print html
