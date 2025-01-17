## The main.py file is the entry point for the application

import graph_generator as GG
import Independentcascade as CS
import visualizing as VS
from nodedegrees import greedy_remove_highest_degree_nodes
from eigenvector_centralities import greedy_remove_highest_eigenvector_centrality_nodes
from Katz_centralities import greedy_remove_highest_katz_centrality_nodes
from Activation_function import greedy_minimize_spread
import networkx as nx
import random

def main():
    # Generate a graph with infection probability
    graph = GG.create_random_graph(25, 0.3, 0.3)
    graph1 = graph.copy()
    graph2 = graph.copy()
    graph3 = graph.copy()
    # Input the value of k
    k = int(input("Enter the number of nodes to remove: "))

    # Inform the user about the number of times the greedy algorithm will be implemented
    print(f"The greedy algorithm will be implemented {k} times to remove the highest degree nodes.")

    # Compute the layout for the graph so that its the same for both gif files
    pos = nx.spring_layout(graph)

    # Randomly select an initial infected node
    initial_infected = random.choice(list(graph.nodes))

    # Create a cascade for the original graph, that starts from the initial infected node
    original_cascade = CS.independent_cascade_model(graph, initial_infected)

    # Visualize the original graph and the cascade in the layout
    VS.create_visualisation(graph, original_cascade, "graph.gif", pos)

    # Apply the greedy algorithm to remove the highest degree nodes to create the updated graph
    degree_updatedgraph = greedy_remove_highest_degree_nodes(graph, k)
    
    
    
#1 Check if the initial infected node is removed
    if initial_infected not in degree_updatedgraph.nodes:
        # Visualize the updated graph with only gray nodes
        VS.create_visualisation(degree_updatedgraph, [], "nodedegree_editedgraph.gif", pos)
        
    else:
        # Create a cascade for the updated graph
        degree_updated_cascade = CS.independent_cascade_model(degree_updatedgraph, initial_infected)
        

        # Visualize the updated graph and the cascade
        VS.create_visualisation(degree_updatedgraph, degree_updated_cascade, "nodedegree_editedgraph.gif", pos)

    minimized_spread_graph = greedy_minimize_spread(graph1, k, initial_infected)
   
#2 Check if the initial infected node is removed
    if initial_infected not in minimized_spread_graph.nodes:
        # Visualize the updated graph with only gray nodes
        VS.create_visualisation(minimized_spread_graph, [], "minimizedspread_editedgraph.gif", pos)

    else:
        # Create a cascade for the updated graph
        minimized_spread_cascade = CS.independent_cascade_model(minimized_spread_graph, initial_infected)
        # Visualize the updated graph and the cascade
        VS.create_visualisation(minimized_spread_graph, minimized_spread_cascade, "minimizedspread_editedgraph.gif", pos)

    eigenvector_updatedgraph = greedy_remove_highest_eigenvector_centrality_nodes(graph2, k)    

#3 Check if the initial infected node is removed
    if initial_infected not in eigenvector_updatedgraph.nodes:
        # Visualize the updated graph with only gray nodes
        VS.create_visualisation(eigenvector_updatedgraph, [], "nodeeigenvector_editedgraph.gif", pos)

    else:
        # Create a cascade for the updated graph
        eigenvector_updated_cascade = CS.independent_cascade_model(eigenvector_updatedgraph, initial_infected)
        # Visualize the updated graph and the cascade
        VS.create_visualisation(eigenvector_updatedgraph, eigenvector_updated_cascade, "nodeeigenvector_editedgraph.gif", pos)

    katz_updatedgraph = greedy_remove_highest_katz_centrality_nodes(graph3, k)

#4 Check if the initial infected node is removed
    if initial_infected not in katz_updatedgraph.nodes:
        # Visualize the updated graph with only gray nodes
        VS.create_visualisation(katz_updatedgraph, [], "nodekatz_editedgraph.gif", pos)

    else:
        # Create a cascade for the updated graph
        katz_updated_cascade = CS.independent_cascade_model(katz_updatedgraph, initial_infected)
        # Visualize the updated graph and the cascade
        VS.create_visualisation(katz_updatedgraph, katz_updated_cascade, "nodekatz_editedgraph.gif", pos)

if __name__ == "__main__":
    main()