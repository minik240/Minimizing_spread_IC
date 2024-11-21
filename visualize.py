## Create a visualisation of a graph and its cascade.
## The graph is a directed graph in networkx format.
## The cascade is a list of pairs (node, time) where node is the node that was activated at time time.
## The visualisation is an animated gif.

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import sys
import os

def create_visualisation(graph, cascade, output_file):
    ## Create a figure and axis
    fig, ax = plt.subplots(figsize=(8,5))
    ax.set_aspect('equal')
    ax.axis('off')
    ## Draw the graph
    pos = nx.spring_layout(graph)
    # Draw the baseline graph so that each vertex is gray
    nx.draw(graph, pos, node_color='gray', ax=ax)
    
    ## Transform the cascade into a sequence of sets of vertices; each set 
    ## contains the vertices that have been activated up to that point
    cascade_sets = [set()]
    current_time = cascade[0][1]
    for node, time in cascade:
        if time != current_time:
            current_time = time
            cascade_sets.append(cascade_sets[-1].copy())
        cascade_sets[-1].add(node)
    ## Create the animation by coloring the nodes red when they are activated
    def update(i):
        ax.clear()
        ax.set_aspect('equal')
        ax.axis('off')
        nx.draw(graph, pos, node_color=['green' if node in cascade_sets[i] else 'gray' for node in graph.nodes], ax=ax)
    ani = animation.FuncAnimation(fig, update, frames=len(cascade_sets), repeat=False)
    ## Save the animation to a file
    ani.save(output_file, writer='imagemagick', fps=2)
    