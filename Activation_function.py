#A greedy algorithm for minimization of spread
#with submodular activation function under the Independent Cascade model.

import networkx as nx
import Independentcascade as CS

def greedy_minimize_spread(graph, k, initial_infected):
    """
    Uses a greedy algorithm to remove k nodes from the graph to minimize the spread of activation.
    
    Parameters:
    graph (networkx.Graph): The input graph.
    k (int): The number of nodes to remove.
    initial_infected (int): The initial infected node.
    
    Returns:
    networkx.Graph: The updated graph after removing k nodes.
    """
    removed_nodes = []
    
    for _ in range(k):
        min_spread = float('inf')
        node_to_remove = None
        
        # Iterate over all nodes to find the one whose removal minimizes the spread
        for node in list(graph.nodes):
            if node == initial_infected:
                continue
            
            # Create a copy of the graph and remove the node
            temp_graph = graph.copy()
            temp_graph.remove_node(node)
            
            # Check if the initial infected node is still in the graph
            if initial_infected not in temp_graph.nodes:
                continue
            
            # Simulate the cascading process
            infected_nodes = CS.independent_cascade_model(temp_graph, initial_infected)
            
            # Calculate the number of active nodes (nodes that turn blue)
            spread = len(infected_nodes)
            
            # Update the node to remove if this node results in a smaller spread
            if spread < min_spread:
                min_spread = spread
                node_to_remove = node
        
        # Remove the selected node from the graph
        if node_to_remove is not None:
            graph.remove_node(node_to_remove)
            removed_nodes.append(node_to_remove)
    
    return graph, removed_nodes
    """for _ in range(k):
        min_spread = float('inf')
        node_to_remove = None
        
        # Iterate over all nodes to find the one whose removal minimizes the spread
        for node in list(graph.nodes):
            if node == initial_infected:
                continue
            
            # Create a copy of the graph and remove the node
            temp_graph = graph.copy()
            temp_graph.remove_node(node)
            
            # Check if the initial infected node is still in the graph
            if initial_infected not in temp_graph.nodes:
                continue
            
            # Simulate the cascading process
            infected_nodes = CS.independent_cascade_model(temp_graph, initial_infected)
            
            # Calculate the number of active nodes (nodes that turn blue)
            active_nodes = set(node for node, _ in infected_nodes)
            
            # Check if this node removal results in a smaller spread
            if len(active_nodes) < min_spread:
                min_spread = len(active_nodes)
                node_to_remove = node
        
        # Remove the selected node from the original graph
        if node_to_remove is not None:
            graph.remove_node(node_to_remove)
    
    return graph"""