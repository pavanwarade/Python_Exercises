import urllib
x=urllib.urlopen("https://www.google.co.in")
print(x.read())
print(x)