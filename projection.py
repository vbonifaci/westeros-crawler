#!/usr/bin/python2.7
# Requires Python 2.7+
import sys, string, urllib2, os, argparse
import networkx as nx
from networkx.algorithms import bipartite

def prepare(name):
	return name.replace(' ','_')

B = nx.read_gml('westeros_bip.gml')
chaps = set(n for n,d in B.nodes(data=True) if d['bipartite']==0)
chars = set(B) - chaps

#G = bipartite.weighted_projected_graph(B, chars)
#nx.write_gml(G, 'westeros.gml') # co-occurrence weighted graph

#R = bipartite.weighted_projected_graph(B, chars, True)
#nx.write_gml(R, 'westeros_ratio.gml') # ratio weighted graph

#M = bipartite.projected_graph(B, chars, True)
#nx.write_gml(M, 'westeros_multi.gml') # unweighted multigraph

##vip_list = ['Petyr Baelish','Sansa Stark','Tyrion Lannister','Sandor Clegane','Cersei Lannister','Varys','Benjen Stark','Jon Snow','Illyrio Mopatis']

DEG_THRESH = 25 # degree threshold
#vips = set(n for n,d in B.nodes(data=True) if d['label'] in vip_list)
vips = set(n for n,d in B.nodes(data=True) if B.degree(n) > DEG_THRESH and d['bipartite']==1)

#COLL_THRESH = 50 # collaboration threshold
COLL_THRESH = 0.005
VG = bipartite.weighted_projected_graph(B, vips, True).subgraph(vips)
VG.remove_edges_from([e for e in VG.edges(data=True) if e[2]['weight'] < COLL_THRESH])

nx.write_gml(VG, 'westeros_vips.gml')

