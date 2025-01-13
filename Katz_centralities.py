#Calculates the Katz-centralities of nodes in a graph and removes the nodes with the highest Katz-centralities from the graph.
import graph_generator as GG
import networkx as nx

def calculate_and_sort_katz_centrality(graph):
    # Calculate the Katz-centralities of nodes
    katz_centrality = nx.katz_centrality(graph, max_iter=10000, tol=1e-6) # max_iter and tol are optional parameters

    # Create a list of nodes with their Katz-centralities
    node_centralities = [(node, centrality) for node, centrality in katz_centrality.items()]

    # Sort the list from highest centrality to lowest centrality
    sorted_node_centralities = sorted(node_centralities, key=lambda x: x[1], reverse=True)

    return sorted_node_centralities

def greedy_remove_highest_katz_centrality_nodes(graph, k):
    for _ in range(k):
        # Calculate and sort Katz-centralities
        sorted_node_centralities = calculate_and_sort_katz_centrality(graph)
        
        if not sorted_node_centralities:
            break
        
        # Remove the node with the highest Katz-centrality
        highest_centrality_node = sorted_node_centralities[0][0]
        graph.remove_node(highest_centrality_node)
    
    return graph