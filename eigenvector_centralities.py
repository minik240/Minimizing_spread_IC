#Calculates the Eigenvector centralities of nodes in a graph and removes the nodes with the highest Eigenvector centralities from the graph.
import graph_generator as GG
import networkx as nx

def calculate_and_sort_eigenvector_centrality(graph):
    # Calculate the Eigenvector centralities of nodes
    eigenvector_centrality = nx.eigenvector_centrality(graph)

    # Create a list of nodes with their Eigenvector centralities
    node_centralities = [(node, centrality) for node, centrality in eigenvector_centrality.items()]

    # Sort the list from highest centrality to lowest centrality
    sorted_node_centralities = sorted(node_centralities, key=lambda x: x[1], reverse=True)

    return sorted_node_centralities

def greedy_remove_highest_eigenvector_centrality_nodes(graph, k, initial_infected = None):
    removed_nodes = []
    for _ in range(k):
        # Calculate and sort eigenvector centralities
        sorted_node_centralities = calculate_and_sort_eigenvector_centrality(graph)
        
        if not sorted_node_centralities:
            break
        
        # Remove the node with the highest eigenvector centrality that is not the initial infected node
        highest_centrality_node = sorted_node_centralities[0][0] if sorted_node_centralities[0][0] != initial_infected else sorted_node_centralities[1][0]
        graph.remove_node(highest_centrality_node)
        removed_nodes.append(highest_centrality_node)
    
    return graph, removed_nodes
