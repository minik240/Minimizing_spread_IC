# Independent cascade model implementation for graphs.
# Assumes networkx as graph model. 
## Independent Cascade Model outputs a sequence of pairs (v,t) where v is a node and t is the time at which it gets activated.
## It takes as input a graph and initial_infected set. If initial_infected set is not given, it picks a random vertex as seed (given in main.py)
## The probability of infection is the edge weight between the nodes that is given in main.py.

import random

def independent_cascade_MARKOV(graph, initial_infected, num_simulations=1000):
    """
    Simulates the independent cascade model a number of times on the given graph.
    
    Parameters:
    graph (networkx.Graph): The input graph.
    initial_infected (int): The initial infected node.
    num_simulations (int): The number of simulations to run.
    
    Returns:
    dict: A dictionary of nodes and their infection probabilities.
    """
    # Initialize infection probabilities with all nodes from the original graph
    infection_probabilities = {node: 0 for node in graph.nodes}

    for i in range(num_simulations):
        infected = independent_cascade_model(graph, initial_infected)
        for node, time_step in infected:
            if node in infection_probabilities:
                infection_probabilities[node] += 1 / num_simulations
            else:
                infection_probabilities[node] = 1 / num_simulations

    # Ensure all nodes in the original graph have an entry in the infection probabilities
    for node in graph.nodes:
        if node not in infection_probabilities:
            infection_probabilities[node] = 0

    return infection_probabilities
 
def independent_cascade_model(graph, initial_infected):
    """
    Simulates the independent cascade model on the given graph.
    
    Parameters:
    graph (networkx.Graph): The input graph.
    initial_infected (int): The initial infected node.
    
    Returns:
    list: The list of tuples (node, time_step) indicating when each node was infected.
    """
    # Initialize the list of infected nodes with their infection time
    infected = []
    
    # Add the initial infected node
    infected.append((initial_infected, 0))
    
    # Initialize the list of newly infected nodes
    new_infected = [(initial_infected, 0)]
    time_step = 1
    
    while new_infected:
        current_new_infected = []
        for node, _ in new_infected:
            for neighbor in graph.neighbors(node):
                # Use the infection probability from the graph's edge attribute
                if neighbor not in [n for n, _ in infected] and random.random() < graph[node][neighbor]['weight']:
                    infected.append((neighbor, time_step))
                    current_new_infected.append((neighbor, time_step))
        new_infected = current_new_infected
        time_step += 1
    
    return infected