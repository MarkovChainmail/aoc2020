import re
from functools import reduce

#I'm compromising here by using a non-standard library...
import networkx as nx

# Exercise A
print(len(nx.ancestors(nx.convert.from_edgelist(list(((l[0], t) for l in list(re.split(' contain [0-9] | contain |, [0-9] ',l.replace('bags','bag').replace('\n','').replace('.','')) for l in open('bags.txt')) for t in l[1:])),create_using=nx.DiGraph), 'shiny gold bag')))

# Exercise B
print(reduce(lambda x,y: {**x, y: sum(x[z[1]] * z[2]['weight'] for z in list(e))+1} if (e := G.out_edges([y],data=True)) else {**x, y:1}, nx.dfs_postorder_nodes(G := nx.DiGraph(list((h[0],t[2:],{'weight': int(t[0])}) for h in (re.split(' contain |, ', re.sub(r'[\n|.]','', l.replace('bags','bag'))) for l in open('bags.txt')) for t in h[1:] if t[0].isdigit())), 'shiny gold bag'), {})['shiny gold bag']-1)
