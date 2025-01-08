## The main.py file is the entry point for the application

import Independentcascade as CS
import graph_generator as GG
import visualizing as VS
import random
#random imported for edge weights

def main():
    # Generate a graph
    # n is the number of nodes (50)
    # p is the probability of an edge within a block (0.3)
    # w is the edge weight (removed for now)

    graph = GG.create_random_graph(20, 0.3, 0.3)
    # Generate a cascade
    cascade = CS.independent_cascade_model(graph)
    # Visualize the graph and the cascade
    VS.create_visualisation(graph,cascade, "graph.gif")

if __name__ == "__main__":
    main()