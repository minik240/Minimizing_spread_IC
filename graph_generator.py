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