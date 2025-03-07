#Calculates the degrees of nodes in a graph and removes the nodes with the highest degrees from the graph.
import graph_generator as GG

def calculate_and_sort_degrees(graph):
    # Calculate the degrees of nodes
    node_degrees = [(node, degree) for node, degree in graph.degree()]

    # Sort the list from highest degree to lowest degree using lambda 
    # as the key that returns the second element of the tuple (degree)
    sorted_node_degrees = sorted(node_degrees, key=lambda x: x[1], reverse=True)

    return sorted_node_degrees

def greedy_remove_highest_degree_nodes(graph, k, initial_infected = None):
    removed_nodes = []
    for _ in range(k):
        ## Remove the node with the highest degree that is not the initial infected node
        sorted_node_degrees = calculate_and_sort_degrees(graph)
        highest_degree_node = sorted_node_degrees[0][0] if sorted_node_degrees[0][0] != initial_infected else sorted_node_degrees[1][0]
        graph.remove_node(highest_degree_node)
        removed_nodes.append(highest_degree_node)
    return graph, removed_nodes

"""def greedy_remove_highest_degree_nodes(graph, k):
    for _ in range(k):
        # Calculate and sort degrees
        sorted_node_degrees = calculate_and_sort_degrees(graph)
        
        if not sorted_node_degrees:
            break
        
        # Remove the node with the highest degree
        highest_degree_node = sorted_node_degrees[0][0]
        graph.remove_node(highest_degree_node)
    
    return graph"""