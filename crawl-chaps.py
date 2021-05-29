#!/usr/bin/python2.7
# Requires Python 2.7+
import sys, string, urllib2, os, argparse
from bs4 import BeautifulSoup

def prepare(name):
	return name.replace(' ','_')

def crawl(chap):
	#response = opener.open(BASE+chap)
	#page = response.read()
	#soup = BeautifulSoup(page)
	#print soup.find('meta',property='og:title')['content']
	#print chap
	print '{:30} ~ {}'.format(chap, chap.replace('_',' ').encode("ascii","ignore"))

books = ['A Game of Thrones', 'A Clash of Kings', 'A Storm of Swords', 'A Feast for Crows', 'A Dance with Dragons']
nchaps = [72, 69, 80, 45, 71]
has_prologue = [True, True, True, True, True]
has_epilogue = [False, False, True, False, True]
has_appendix = [True, True, True, True, True]

BASE = 'http://awoiaf.westeros.org/index.php/'
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]


b = 0
for book in books: 
	if has_prologue[b]:
		crawl(prepare(book+'-Prologue'))	
	for c in range(1,nchaps[b]+1):
		crawl(prepare(book+'-Chapter '+str(c)))
	if has_epilogue[b]:
		crawl(prepare(book+'-Epilogue'))	
	##if has_appendix[b]:  ## avoid appendices -- they have ALL characters together...
	##	crawl(prepare(book+'-Appendix'))
	b += 1

	

