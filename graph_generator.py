### Create a random graph with a given number of nodes and edges, using networkx

import networkx as nx
import random

## Create random graph using stochastic block model
def create_random_graph(n, p, w):
    # n is the number of nodes
    # p is the probability of an edge within any two nodes
    # w is the edge weight
    
    # Create a graph
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for i in range(n):
        for j in range(i+1, n):
                if random.random() < p:
                    G.add_edge(i, j)
                    #w = random.random()
                    G[i][j]['weight'] = w
    return G

## Create a stochastic block model graph with n vertices, b blocks, and probabilities p and q
## Edge weight is uniform w.
def create_sbm(n, b, p, q, w):
    blocks = [[i] for i in range(b)]
    for node in range(b, n):
        blocks[random.choice(range(b))].append(node)
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for block in blocks:
         for u in block:
            for v in block:
                if u != v and random.random() < p:
                    G.add_edge(u, v)
                    G[u][v]['weight'] = w
            for other_block in blocks:  
                if block != other_block:
                    for v in other_block:
                        if random.random() < q:
                            G.add_edge(u, v)
                            G[u][v]['weight'] = w
    return G  
