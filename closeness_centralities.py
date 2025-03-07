# Calculates the Closeness centralities of nodes in a graph and removes the nodes with the highest closeness centralities from the graph.
import networkx as nx

def calculate_and_sort_closeness_centrality(graph):
    # Calculate the closeness centralities of nodes
    closeness_centrality = nx.closeness_centrality(graph)

    # Create a list of nodes with their closeness centralities
    node_centralities = [(node, centrality) for node, centrality in closeness_centrality.items()]

    # Sort the list from highest centrality to lowest centrality
    sorted_node_centralities = sorted(node_centralities, key=lambda x: x[1], reverse=True)

    return sorted_node_centralities

def greedy_remove_highest_closeness_centrality_nodes(graph, k, initial_infected = None):
    removed_nodes = []
    for _ in range(k):
        # Calculate and sort closeness centralities
        sorted_node_centralities = calculate_and_sort_closeness_centrality(graph)
        
        if not sorted_node_centralities:
            break
        
        # Remove the node with the highest closeness centrality
        highest_centrality_node = sorted_node_centralities[0][0] if sorted_node_centralities[0][0] != initial_infected else sorted_node_centralities[1][0]
        graph.remove_node(highest_centrality_node)
        removed_nodes.append(highest_centrality_node)
    
    return graph, removed_nodes