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
    graph = GG.create_random_graph(40, 0.2, 0.1)
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

    # Calculate infection probabilities for the original graph
    original_infection_probabilities = CS.independent_cascade_MARKOV(graph, initial_infected)
    print("Infection probabilities for the original graph:")
    for node, prob in original_infection_probabilities.items():
        print(f"Node {node}: {prob:.4f}")
    original_mean_infection_probability = sum(original_infection_probabilities.values()) / len(original_infection_probabilities)
    print(f"Mean infection probability for the original graph: {original_mean_infection_probability:.4f}")

    # Apply the greedy algorithm to remove the highest degree nodes to create the updated graph
    degree_updatedgraph, removed_degree_nodes = greedy_remove_highest_degree_nodes(graph, k)
    degree_updated_infection_probabilities = CS.independent_cascade_MARKOV(degree_updatedgraph, initial_infected)
    print("Infection probabilities for the degree updated graph:")
    for node, prob in degree_updated_infection_probabilities.items():
        print(f"Node {node}: {prob:.4f}")
    degree_mean_infection_probability = sum(degree_updated_infection_probabilities.values()) / len(degree_updated_infection_probabilities)
    print(f"Mean infection probability for the degree updated graph: {degree_mean_infection_probability:.4f}")
    print(f"Removed nodes for nodedegree_editedgraph.gif are: {removed_degree_nodes}")

    # Apply the greedy algorithm to minimize the spread
    minimized_spread_graph, removed_minimized_spread_nodes = greedy_minimize_spread(graph1, k, initial_infected)
    minimized_spread_infection_probabilities = CS.independent_cascade_MARKOV(minimized_spread_graph, initial_infected)
    print("Infection probabilities for the minimized spread graph:")
    for node, prob in minimized_spread_infection_probabilities.items():
        print(f"Node {node}: {prob:.4f}")
    minimized_spread_mean_infection_probability = sum(minimized_spread_infection_probabilities.values()) / len(minimized_spread_infection_probabilities)
    print(f"Mean infection probability for the minimized spread graph: {minimized_spread_mean_infection_probability:.4f}")
    print(f"Removed nodes for minimizedspread_editedgraph.gif are: {removed_minimized_spread_nodes}")

    # Apply the greedy algorithm to remove the highest eigenvector centrality nodes
    eigenvector_updatedgraph, removed_eigenvector_nodes = greedy_remove_highest_eigenvector_centrality_nodes(graph2, k)
    eigenvector_updated_infection_probabilities = CS.independent_cascade_MARKOV(eigenvector_updatedgraph, initial_infected)
    print("Infection probabilities for the eigenvector updated graph:")
    for node, prob in eigenvector_updated_infection_probabilities.items():
        print(f"Node {node}: {prob:.4f}")
    eigenvector_mean_infection_probability = sum(eigenvector_updated_infection_probabilities.values()) / len(eigenvector_updated_infection_probabilities)
    print(f"Mean infection probability for the eigenvector updated graph: {eigenvector_mean_infection_probability:.4f}")
    print(f"Removed nodes for eigenvector_editedgraph.gif are: {removed_eigenvector_nodes}")

    # Apply the greedy algorithm to remove the highest Katz centrality nodes
    katz_updatedgraph, removed_katz_nodes = greedy_remove_highest_katz_centrality_nodes(graph3, k)
    katz_updated_infection_probabilities = CS.independent_cascade_MARKOV(katz_updatedgraph, initial_infected)
    print("Infection probabilities for the Katz updated graph:")
    for node, prob in katz_updated_infection_probabilities.items():
        print(f"Node {node}: {prob:.4f}")
    katz_mean_infection_probability = sum(katz_updated_infection_probabilities.values()) / len(katz_updated_infection_probabilities)
    print(f"Mean infection probability for the Katz updated graph: {katz_mean_infection_probability:.4f}")
    print(f"Removed nodes for katz_editedgraph.gif are: {removed_katz_nodes}")


    # Check if the initial infected node is removed
    if initial_infected not in degree_updatedgraph.nodes:
        # Visualize the updated graph with only gray nodes
        VS.create_visualisation(degree_updatedgraph, [], "nodedegree_editedgraph.gif", pos)
    else:
        # Create a cascade for the updated graph
        degree_updated_cascade = CS.independent_cascade_model(degree_updatedgraph, initial_infected)
        # Visualize the updated graph and the cascade
        VS.create_visualisation(degree_updatedgraph, degree_updated_cascade, "nodedegree_editedgraph.gif", pos)

    # Check if the initial infected node is removed
    if initial_infected not in minimized_spread_graph.nodes:
        # Visualize the updated graph with only gray nodes
        VS.create_visualisation(minimized_spread_graph, [], "minimizedspread_editedgraph.gif", pos)
    else:
        # Create a cascade for the updated graph
        minimized_spread_cascade = CS.independent_cascade_model(minimized_spread_graph, initial_infected)
        # Visualize the updated graph and the cascade
        VS.create_visualisation(minimized_spread_graph, minimized_spread_cascade, "minimizedspread_editedgraph.gif", pos)

    # Check if the initial infected node is removed
    if initial_infected not in eigenvector_updatedgraph.nodes:
        # Visualize the updated graph with only gray nodes
        VS.create_visualisation(eigenvector_updatedgraph, [], "eigenvector_editedgraph.gif", pos)
    else:
        # Create a cascade for the updated graph
        eigenvector_updated_cascade = CS.independent_cascade_model(eigenvector_updatedgraph, initial_infected)
        # Visualize the updated graph and the cascade
        VS.create_visualisation(eigenvector_updatedgraph, eigenvector_updated_cascade, "eigenvector_editedgraph.gif", pos)

    # Check if the initial infected node is removed
    if initial_infected not in katz_updatedgraph.nodes:
        # Visualize the updated graph with only gray nodes
        VS.create_visualisation(katz_updatedgraph, [], "katz_editedgraph.gif", pos)
    else:
        # Create a cascade for the updated graph
        katz_updated_cascade = CS.independent_cascade_model(katz_updatedgraph, initial_infected)
        # Visualize the updated graph and the cascade
        VS.create_visualisation(katz_updatedgraph, katz_updated_cascade, "katz_editedgraph.gif", pos)

if __name__ == "__main__":
    main()

"""def main():
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
    main()"""