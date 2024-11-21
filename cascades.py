# Independent and linear threshold model implementations for graphs.
# Assumes networkx as graph model. 

import random


## Independent Cascade Model outputs a sequence of pairs (v,t) where v is a node and t is the time at which it gets infected.
## It takes as input a graph G and a seed set S. If S is not given, it picks a random vertex as seed.
## The probability of infection is the edge weight between the nodes.

def independent_cascade_model(G, S = None):
    if S == None:
        S = [random.choice(list(G.nodes()))]
    infected = set(S)
    time = 0
    infected_at = {v:0 for v in S}
    while S:
        time += 1
        new_S = []
        for v in S:
            for u in G.neighbors(v):
                if u not in infected:
                    # The random.random() takes a random number from [0,1], and that must be smaller than the
                    # weight (probability) of the edge (v,u)
                    if random.random() < G[v][u]['weight']:
                        infected.add(u)
                        infected_at[u] = time
                        new_S.append(u)
        S = new_S
    return [(v, infected_at[v]) for v in infected]

## The linear Threshold model outputs a sequence of pairs (v,t) where v is a node and t is the time at which it gets infected.
## It takes as input a graph G and a seed set S, and threshold th. If S is not given, it picks a random vertex as seed.
## The threshold of of a node u is th(u). If th is not given, it picks a random threshold between 0 and 1.

def linear_threshold_model(G, S = None, th = None):
    if S == None:
        S = [random.choice(list(G.nodes()))]
    if th == None:
        th = {v:random.random() for v in G.nodes()}
    infected = set(S)
    time = 0
    infected_at = {v:0 for v in S}
    while S:
        time += 1
        new_S = []
        for v in S:
            for u in G.neighbors(v):
                if u not in infected:
                    if sum([1 for w in G.neighbors(u) if w in infected and G[u][w]['weight'] > th[u]]) >= th[u]:
                        infected.add(u)
                        infected_at[u] = time
                        new_S.append(u)
        S = new_S
    return [(v, infected_at[v]) for v in infected]