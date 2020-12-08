from functools import reduce
import networkx as nx

# Exercise A:
# Build network, traverse instruction path for accumulator
print(reduce(lambda x,y: (x[0] + t['amount'] if (t := G.get_edge_data(*y))['type']=='acc' else x[0], x[1] + [y[0]]), nx.bfs_edges(G:=nx.convert.from_edgelist(list(([k, k+v[1] if v[0]=='jmp' else k+1, {'type': v[0], 'amount': v[1]}] for k,v in {l[0]:l[1:] for l in map(lambda x: x[:2] + [int(x[2][:-1])], ([e] + line.split(" ") for e, line in enumerate(open('game.txt'))))}.items())),create_using=nx.DiGraph()),0), [0, []])[0])

# Exercise B:
# Do the same thing as A, except you can try every single swapped version
# DOES NOT ACTUALLY WORK YET
print(list(filter(lambda x: x[1], list(filter(lambda x: x[0] != 1930, (reduce(lambda x,y: (x[0] + t['amount'] if (t := G.get_edge_data(*y))['type']=='acc' else x[0], x[1] +[y[1]]), nx.bfs_edges(G:=nx.convert.from_edgelist(list(([k, k+v[1] if v[0]=='jmp' else k+1, {'type': v[0], 'amount': v[1]}] for k,v in {l[0]:l[1:] for l in map(lambda x: x[:2] + [int(x[2][:-1])], ([e, "jmp" if line.split(" ")[0]=="acc" else "acc", line.split(" ")[1]] if not line.split(" ")[0] == "acc" and e==current else [e] + line.split(" ") for e, line in enumerate(open('game.txt'))))}.items())),create_using=nx.DiGraph()),0), [0, []]) for current in range(623)))))))
