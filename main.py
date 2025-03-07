## The main.py file is the entry point for the application

import graph_generator as GG
import Independentcascade as CS
import visualizing as VS
from nodedegrees import greedy_remove_highest_degree_nodes
from eigenvector_centralities import greedy_remove_highest_eigenvector_centrality_nodes
from Katz_centralities import greedy_remove_highest_katz_centrality_nodes
from Influence_function import greedy_minimize_spread
from betweenness_centralities import greedy_remove_highest_betweenness_centrality_nodes
from closeness_centralities import greedy_remove_highest_closeness_centrality_nodes 
import networkx as nx
import random
from icecream import ic

def main():
    # Generate a graph with infection probability
    graph = GG.create_random_graph(35, 0.2, 0.2)
    graph1 = graph.copy()
    graph2 = graph.copy()
    graph3 = graph.copy()
    graph4 = graph.copy()
    graph5 = graph.copy()
    graph6 = graph.copy()
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

    """# Calculate infection probabilities for the original graph
    original_infection_probabilities = CS.independent_cascade_MARKOV(graph, initial_infected)
    print("Infection probabilities for the original graph:")
    for node, prob in original_infection_probabilities.items():
        print(f"Node {node}: {prob:.4f}")
    original_mean_infection_probability = sum(original_infection_probabilities.values()) / len(original_infection_probabilities)
    print(f"Mean infection probability for the original graph: {original_mean_infection_probability:.4f}")"""
    
    #NEW Calculate infection probabilities for the original graph
    original_infection_probabilities = CS.independent_cascade_MARKOV(graph, initial_infected)
    original_mean_infection_probability = sum(original_infection_probabilities.values()) / len(original_infection_probabilities)
    print(f"Mean infection probability for the original graph: {original_mean_infection_probability:.4f}")

    """# Apply the greedy algorithm to remove the highest degree nodes to create the updated graph
    degree_updatedgraph, removed_degree_nodes = greedy_remove_highest_degree_nodes(graph, k)
    degree_updated_infection_probabilities = CS.independent_cascade_MARKOV(degree_updatedgraph, initial_infected)
    print("Infection probabilities for the degree updated graph:")
    for node, prob in degree_updated_infection_probabilities.items():
        print(f"Node {node}: {prob:.4f}")
    degree_mean_infection_probability = sum(degree_updated_infection_probabilities.values()) / len(degree_updated_infection_probabilities)
    print(f"Mean infection probability for the degree updated graph: {degree_mean_infection_probability:.4f}")
    print(f"Removed nodes for nodedegree_editedgraph.gif are: {removed_degree_nodes}")"""
    
    #NEW Apply the greedy algorithm to remove the highest degree nodes
    degree_updatedgraph, removed_degree_nodes = greedy_remove_highest_degree_nodes(graph1, k)    
    degree_updated_infection_probabilities = CS.independent_cascade_MARKOV(degree_updatedgraph, initial_infected)
    degree_mean_infection_probability = sum(degree_updated_infection_probabilities.values()) / len(degree_updated_infection_probabilities)
    print(f"Mean infection probability for the degree updated graph: {degree_mean_infection_probability:.4f}")
    print(f"Removed nodes for degree_editedgraph.gif are: {removed_degree_nodes}")

    """# Apply the greedy algorithm to minimize the spread
    minimized_spread_graph, removed_minimized_spread_nodes = greedy_minimize_spread(graph1, k, initial_infected)
    minimized_spread_infection_probabilities = CS.independent_cascade_MARKOV(minimized_spread_graph, initial_infected)
    print("Infection probabilities for the minimized spread graph:")
    for node, prob in minimized_spread_infection_probabilities.items():
        print(f"Node {node}: {prob:.4f}")
    minimized_spread_mean_infection_probability = sum(minimized_spread_infection_probabilities.values()) / len(minimized_spread_infection_probabilities)
    print(f"Mean infection probability for the minimized spread graph: {minimized_spread_mean_infection_probability:.4f}")
    print(f"Removed nodes for minimizedspread_editedgraph.gif are: {removed_minimized_spread_nodes}")"""

    #NEW Apply the greedy algorithm to minimize the spread
    minimized_spread_graph, removed_minimized_spread_nodes = greedy_minimize_spread(graph2, k, initial_infected)
    minimized_spread_infection_probabilities = CS.independent_cascade_MARKOV(minimized_spread_graph, initial_infected)
    minimized_spread_mean_infection_probability = sum(minimized_spread_infection_probabilities.values()) / len(minimized_spread_infection_probabilities)
    print(f"Mean infection probability for the minimized spread graph: {minimized_spread_mean_infection_probability:.4f}")
    print(f"Removed nodes for minimized_spread_editedgraph.gif are: {removed_minimized_spread_nodes}")

    """# Apply the greedy algorithm to remove the highest eigenvector centrality nodes
    eigenvector_updatedgraph, removed_eigenvector_nodes = greedy_remove_highest_eigenvector_centrality_nodes(graph2, k)
    eigenvector_updated_infection_probabilities = CS.independent_cascade_MARKOV(eigenvector_updatedgraph, initial_infected)
    print("Infection probabilities for the eigenvector updated graph:")
    for node, prob in eigenvector_updated_infection_probabilities.items():
        print(f"Node {node}: {prob:.4f}")
    eigenvector_mean_infection_probability = sum(eigenvector_updated_infection_probabilities.values()) / len(eigenvector_updated_infection_probabilities)
    print(f"Mean infection probability for the eigenvector updated graph: {eigenvector_mean_infection_probability:.4f}")
    print(f"Removed nodes for eigenvector_editedgraph.gif are: {removed_eigenvector_nodes}")"""

    #NEW Apply the greedy algorithm to remove the highest eigenvector centrality nodes
    eigenvector_updatedgraph, removed_eigenvector_nodes = greedy_remove_highest_eigenvector_centrality_nodes(graph3, k)
    eigenvector_updated_infection_probabilities = CS.independent_cascade_MARKOV(eigenvector_updatedgraph, initial_infected)
    eigenvector_mean_infection_probability = sum(eigenvector_updated_infection_probabilities.values()) / len(eigenvector_updated_infection_probabilities)
    print(f"Mean infection probability for the eigenvector updated graph: {eigenvector_mean_infection_probability:.4f}")
    print(f"Removed nodes for eigenvector_editedgraph.gif are: {removed_eigenvector_nodes}")

    """# Apply the greedy algorithm to remove the highest Katz centrality nodes
    katz_updatedgraph, removed_katz_nodes = greedy_remove_highest_katz_centrality_nodes(graph3, k)
    katz_updated_infection_probabilities = CS.independent_cascade_MARKOV(katz_updatedgraph, initial_infected)
    print("Infection probabilities for the Katz updated graph:")
    for node, prob in katz_updated_infection_probabilities.items():
        print(f"Node {node}: {prob:.4f}")
    katz_mean_infection_probability = sum(katz_updated_infection_probabilities.values()) / len(katz_updated_infection_probabilities)
    print(f"Mean infection probability for the Katz updated graph: {katz_mean_infection_probability:.4f}")
    print(f"Removed nodes for katz_editedgraph.gif are: {removed_katz_nodes}")"""

    #NEW Apply the greedy algorithm to remove the highest Katz centrality nodes
    katz_updatedgraph, removed_katz_nodes = greedy_remove_highest_katz_centrality_nodes(graph4, k)
    katz_updated_infection_probabilities = CS.independent_cascade_MARKOV(katz_updatedgraph, initial_infected)
    katz_mean_infection_probability = sum(katz_updated_infection_probabilities.values()) / len(katz_updated_infection_probabilities)
    print(f"Mean infection probability for the Katz updated graph: {katz_mean_infection_probability:.4f}")
    print(f"Removed nodes for katz_editedgraph.gif are: {removed_katz_nodes}")

    """# Apply the greedy algorithm to remove the highest betweenness centrality nodes
    betweenness_updatedgraph, removed_betweenness_nodes = greedy_remove_highest_betweenness_centrality_nodes(graph4, k)
    betweenness_updated_infection_probabilities = CS.independent_cascade_MARKOV(betweenness_updatedgraph, initial_infected)
    print("Infection probabilities for the betweenness updated graph:")
    for node, prob in betweenness_updated_infection_probabilities.items():
        print(f"Node {node}: {prob:.4f}")
    betweenness_mean_infection_probability = sum(betweenness_updated_infection_probabilities.values()) / len(betweenness_updated_infection_probabilities)
    print(f"Mean infection probability for the betweenness updated graph: {betweenness_mean_infection_probability:.4f}")
    print(f"Removed nodes for betweenness_editedgraph.gif are: {removed_betweenness_nodes}")"""
    
    #NEW Apply the greedy algorithm to remove the highest betweenness centrality nodes
    betweenness_updatedgraph, removed_betweenness_nodes = greedy_remove_highest_betweenness_centrality_nodes(graph5, k)
    betweenness_updated_infection_probabilities = CS.independent_cascade_MARKOV(betweenness_updatedgraph, initial_infected)
    betweenness_mean_infection_probability = sum(betweenness_updated_infection_probabilities.values()) / len(betweenness_updated_infection_probabilities)
    print(f"Mean infection probability for the betweenness updated graph: {betweenness_mean_infection_probability:.4f}")
    print(f"Removed nodes for betweenness_editedgraph.gif are: {removed_betweenness_nodes}")

    """# Apply the greedy algorithm to remove the highest closeness centrality nodes
    closeness_updatedgraph, removed_closeness_nodes = greedy_remove_highest_closeness_centrality_nodes(graph5, k)
    closeness_updated_infection_probabilities = CS.independent_cascade_MARKOV(closeness_updatedgraph, initial_infected)
    print("Infection probabilities for the closeness updated graph:")
    for node, prob in closeness_updated_infection_probabilities.items():
        print(f"Node {node}: {prob:.4f}")
    closeness_mean_infection_probability = sum(closeness_updated_infection_probabilities.values()) / len(closeness_updated_infection_probabilities)
    print(f"Mean infection probability for the closeness updated graph: {closeness_mean_infection_probability:.4f}")
    print(f"Removed nodes for closeness_editedgraph.gif are: {removed_closeness_nodes}")"""

    #NEW Apply the greedy algorithm to remove the highest closeness centrality nodes
    closeness_updatedgraph, removed_closeness_nodes = greedy_remove_highest_closeness_centrality_nodes(graph6, k)
    closeness_updated_infection_probabilities = CS.independent_cascade_MARKOV(closeness_updatedgraph, initial_infected)
    closeness_mean_infection_probability = sum(closeness_updated_infection_probabilities.values()) / len(closeness_updated_infection_probabilities)
    print(f"Mean infection probability for the closeness updated graph: {closeness_mean_infection_probability:.4f}")
    print(f"Removed nodes for closeness_editedgraph.gif are: {removed_closeness_nodes}")

    

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
    
    # Check if the initial infected node is removed
    if initial_infected not in betweenness_updatedgraph.nodes:
        # Visualize the updated graph with only gray nodes
        VS.create_visualisation(betweenness_updatedgraph, [], "betweenness_editedgraph.gif", pos)
    else:
        # Create a cascade for the updated graph
        betweenness_updated_cascade = CS.independent_cascade_model(betweenness_updatedgraph, initial_infected)
        # Visualize the updated graph and the cascade
        VS.create_visualisation(betweenness_updatedgraph, betweenness_updated_cascade, "betweenness_editedgraph.gif", pos)
    
    # Check if the initial infected node is removed
    if initial_infected not in closeness_updatedgraph.nodes:
        # Visualize the updated graph with only gray nodes
        VS.create_visualisation(closeness_updatedgraph, [], "closeness_editedgraph.gif", pos)
    else:
        # Create a cascade for the updated graph
        closeness_updated_cascade = CS.independent_cascade_model(closeness_updatedgraph, initial_infected)
        # Visualize the updated graph and the cascade
        VS.create_visualisation(closeness_updatedgraph, closeness_updated_cascade, "closeness_editedgraph.gif", pos)

# Load the existing Excel file
    """try:
        workbook = openpyxl.load_workbook('ekadata.xlsx')
        sheet = workbook['nollakaksi']

    # Find the next available row
        next_row = 73
        while sheet[f'B{next_row}'].value is not None:
            next_row += 1

    # Write the mean infection probabilities to the Excel file
        sheet[f'B{next_row}'] = degree_mean_infection_probability
        sheet[f'C{next_row}'] = minimized_spread_mean_infection_probability
        sheet[f'D{next_row}'] = eigenvector_mean_infection_probability
        sheet[f'E{next_row}'] = katz_mean_infection_probability
        sheet[f'F{next_row}'] = betweenness_mean_infection_probability
        sheet[f'G{next_row}'] = closeness_mean_infection_probability
        sheet[f'H{next_row}'] = original_mean_infection_probability

    # Save the workbook
    #workbook.save('ekadata.xlsx')
        workbook.save('ekadata.xlsx')
        print(f"Data successfully written to ekadata.xlsx at row {next_row}")
    except PermissionError as e:
        print(f"PermissionError: {e}. Please ensure the file is not open in another program and you have the necessary permissions.")
    except Exception as e:
        print(f"An error occurred: {e}")"""
if __name__ == "__main__":
    main()
