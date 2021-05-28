#!/usr/bin/python2.7
# Requires Python 2.7+, curl, iptc
import sys, string, urllib2, os, argparse
from bs4 import BeautifulSoup

#soup = BeautifulSoup(urllib2.urlopen( *** ))

def crawl(url):
	soup = BeautifulSoup(urllib2.urlopen(url))
	print soup.find('meta',property='og:title')['content']

books = ['A Game of Thrones', 'A Clash of Kings', 'A Storm of Swords', 'A Feast for Crows', 'A Dance with Dragons']
nchaps = [72, 69, 80, 45, 71]
has_prologue = [True, True, True, True, True]
has_epilogue = [False, False, True, False, True]
has_appendix = [True, True, True, True, True]

#b = 0
#for book in books: 
#	print '*** '+book+' ***'
#	if has_prologue[b]:
#		crawl(
#		
#	b += 1

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')] # fake browser agent
#BASE = 'http://awoiaf.westeros.org/index.php/Chapters'
#BASE = 'http://awoiaf.westeros.org/index.php/A_Clash_of_Kings-Chapter_1'
BASE = 'http://awoiaf.westeros.org/index.php/List_of_characters'
response = opener.open(BASE)
page = response.read()
soup = BeautifulSoup(page)
print soup.find('meta',property='og:title')['content']

items = soup.select('a[href^="/index.php/"]')
for item in items:
	#print item.get_text().strip() + '\t' + item['href']
	id = item['href'][len('/index.php/'):].strip()
	desc = item.get_text().strip()
	print id, "\t~\t", desc
	
 
