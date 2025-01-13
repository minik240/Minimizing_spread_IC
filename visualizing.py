## Create a visualisation of a graph and its cascade.
## The graph is a directed graph in networkx format.
## The cascade is a list of pairs (node, time) where node is the node that was activated at time time.
## The visualisation is an animated gif.

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_visualisation(graph, cascade, output_file, pos):
    ## Create a figure and axis
    fig, ax = plt.subplots(figsize=(8,5))
    ax.set_aspect('equal')
    ax.axis('off')
    ## Draw the graph
    # Draw the baseline graph so that each vertex is gray, the outline is set in main.py
    nx.draw(graph, pos, node_color='gray', ax=ax)
    
    ## Transform the cascade into a sequence of sets of vertices; each set 
    ## contains the vertices that have been activated up to that point
    cascade_sets = [set()]
    for node, time_step in cascade:
        while len(cascade_sets) <= time_step:
            cascade_sets.append(cascade_sets[-1].copy())
        cascade_sets[time_step].add(node)
    
    ## Create the animation by coloring the nodes when they are activated
    def update(i):
        ax.clear()
        ax.set_aspect('equal')
        ax.axis('off')
        nx.draw(graph, pos, node_color=['blue' if node in cascade_sets[i] else 'gray' for node in graph.nodes], ax=ax)
    
    ani = animation.FuncAnimation(fig, update, frames=len(cascade_sets), repeat=False)
    ## Save the animation to a file
    ani.save(output_file, writer='imagemagick', fps=1)
    