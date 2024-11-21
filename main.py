## The main.py file is the entry point for the application

import cascades as CS
import graph_generate as GG
import visualize as VS

def main():
    # Generate a graph
    graph = GG.create_random_graph(50, 10, 0.3, 0.1, 0.2)
    # Generate a cascade
    cascade = CS.independent_cascade_model(graph)
    # Visualize the graph and the cascade
    VS.create_visualisation(graph,cascade, "graph.gif")

if __name__ == "__main__":
    main()

