#!/usr/bin/python2.7
# Requires Python 2.7+
import sys, string, urllib2, os, argparse
from bs4 import BeautifulSoup

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
BASE = 'http://awoiaf.westeros.org/index.php/List_of_characters'
response = opener.open(BASE)
page = response.read()
soup = BeautifulSoup(page)

items = soup.find_all('li')
for item in items: 
	id = item.find('a')
	if id==None: continue
	id = id['href']
	if id==None: continue
	id = id[len('/index.php/'):].strip()
	desc = item.get_text().strip()
	print '{:30} ~ {}'.format(id, desc.encode("ascii","ignore"))
 
