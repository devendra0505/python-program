#!/usr/bin/env python3
import sys,bs4,requests,webbrowser ,lxml
re=requests.get('http://google.com/search?q=' + ' ' ' ''.join(sys.argv[1:]))  
re.raise_for_status()
#CHECK SEARCH PAGES HAS BEEN DOWNLOADED OR NOT BY STATUS CODE
sp=bs4.BeautifulSoup(re.text,'parser.html')
link=sp.select('.r a')
num = min(3, len(link))
for i in range (num):
    webbrowser.open('http://google.com' + link[i].get('href'))
