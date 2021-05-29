#!/usr/bin/python2.7
# Requires Python 2.7+
import sys, string, urllib2, os, argparse
from bs4 import BeautifulSoup
import networkx as nx

BASE = 'http://awoiaf.westeros.org/index.php/'
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

def read_dic(fname, side):
	dic = {}
	file = open(fname)
	for line in file:
		[id, desc] = map(str.strip,line.split('~'))
		dic[id] = desc
		G.add_node(unroll(id), desc=desc.replace('"',"'"), bipartite=side)
	return dic

def prepare(name):
	return name.replace(' ','_')

def unroll(id):
	return id.replace('_',' ')

def crawl(chap):
	response = opener.open(BASE+chap)
	page = response.read()
	soup = BeautifulSoup(page)
	for a_tag in soup.select('a[href]'): 
		if '/index.php/' in a_tag.get('href'):
			target = a_tag.get('href')[len('/index.php/'):]
			if target in chars:
				print ':: ', chars[target]
				G.add_edge(unroll(chap), unroll(target))
		
G = nx.Graph()
chaps = read_dic('CHAPTERS.txt',0)
print str(len(chaps))+' chapters found.'
chars = read_dic('CHARACTERS.txt',1)
print str(len(chars))+' characters found.'

for chap in chaps.iterkeys():
	print '**', unroll(chap), '**'
	crawl(chap)

nx.write_gml(G, "westeros_bip.gml")





















