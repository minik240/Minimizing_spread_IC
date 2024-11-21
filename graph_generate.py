### Create a random graph with a given number of nodes and edges, using networkx

import networkx as nx
import random

## Create random graph using stochastic block model
def create_random_graph(n, m, p, q, w):
    # n is the number of nodes
    # m is the number of blocks
    # p is the probability of an edge within a block
    # q is the probability of an edge between blocks
    # w is the edge weight

    # Create a list of blocks
    blocks = [0] * n
    nodes_in_blocks = [[] for i in range(m)]
    for i in range(n):
        b = random.randint(0, m-1)
        blocks[i] = b
        nodes_in_blocks[b].append(i)
    
    # Create a graph
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for i in range(n):
        for j in range(i+1, n):
            if blocks[i] == blocks[j]:
                if random.random() < p:
                    G.add_edge(i, j)
                    G[i][j]['weight'] = w
            else:
                if random.random() < q:
                    G.add_edge(i, j)
                    G[i][j]['weight'] = w
    return G
        

