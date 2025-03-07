""" This file implements the empirical tests.
    The parameters are set in the beginning of the file and the results are printed in the end,
    into a csv file. The graphs are generated and written. 
    The results will appear in ./results/ folder.
"""

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
import pandas as pd

# Parameters
graph_size_params = [(20, 4), (40, 6) , (60, 8), (80, 10), (100, 12)]
p = 0.4
q = 0.1
w = 0.15
nodes_to_remove = 2
num_iterations = 30
num_simulations = 10000

# Results
df = pd.DataFrame(columns=['n', 'b', 'raw_influence_mean', 'raw_influence_std', 'degree_influence_mean', 'degree_influence_std', 'eigenvector_influence_mean', 'eigenvector_influence_std', 'katz_influence_mean', 'katz_influence_std', 'influence_influence_mean', 'influence_influence_std', 'betweenness_influence_mean', 'betweenness_influence_std', 'closeness_influence_mean', 'closeness_influence_std'])
for n, b in graph_size_params:
    raw_influence_list = []
    degree_influence_list = []
    eigenvector_influence_list = []
    katz_influence_list = []
    influence_influence_list = []
    betweenness_influence_list = []
    closeness_influence_list = []
    for _ in range(num_iterations):
        initial_infected = random.randint(0, n-1)
        G = GG.create_sbm(n, b, p, q, w)
        infection_probabilities = CS.independent_cascade_MARKOV(
            graph=G,
            num_simulations=num_simulations,
            initial_infected=initial_infected
        )
        raw_influence = sum(infection_probabilities.values())/len(infection_probabilities)
        raw_influence_list.append(raw_influence)
        # Greedy Degree
        G_degree = G.copy()
        G_degree, d_nodes = greedy_remove_highest_degree_nodes(
            graph=G_degree,
            k=nodes_to_remove,
            initial_infected=initial_infected
        )
        ic(d_nodes, initial_infected)
        degree_infection_probabilities = CS.independent_cascade_MARKOV(
            graph=G_degree,
            num_simulations=num_simulations,
            initial_infected=initial_infected
        )
        degree_influence = sum(degree_infection_probabilities.values())/len(degree_infection_probabilities)
        degree_influence_list.append(degree_influence)

        # Greedy Eigenvector
        G_eigenvector = G.copy()
        G_eigenvector, e_nodes = greedy_remove_highest_eigenvector_centrality_nodes(
            graph=G_eigenvector,
            k=nodes_to_remove,
            initial_infected=initial_infected
        )
        eigenvector_infection_probabilities = CS.independent_cascade_MARKOV(
            graph=G_eigenvector,
            num_simulations=num_simulations,
            initial_infected=initial_infected
        )
        eigenvector_influence = sum(eigenvector_infection_probabilities.values())/len(eigenvector_infection_probabilities)
        eigenvector_influence_list.append(eigenvector_influence)

        # Greedy Katz
        G_katz = G.copy()
        G_katz, k_nodes = greedy_remove_highest_katz_centrality_nodes(
            graph=G_katz,
            k=nodes_to_remove,
            initial_infected=initial_infected
        )
        katz_infection_probabilities = CS.independent_cascade_MARKOV(
            graph=G_katz,
            num_simulations=num_simulations,
            initial_infected=initial_infected
        )
        katz_influence = sum(katz_infection_probabilities.values())/len(katz_infection_probabilities)
        katz_influence_list.append(katz_influence)

        # Greedy Influence
        G_influence = G.copy()
        G_influence, i_nodes = greedy_minimize_spread(
            graph=G_influence,
            k=nodes_to_remove,
            initial_infected=initial_infected,
            number_of_simulations=num_simulations
        )
        influence_infection_probabilities = CS.independent_cascade_MARKOV(
            graph=G_influence,
            num_simulations=num_simulations,
            initial_infected=initial_infected
        )
        influence_influence = sum(influence_infection_probabilities.values())/len(influence_infection_probabilities)
        influence_influence_list.append(influence_influence)
        ## Greedy Betweenness
        G_betweenness = G.copy()
        G_betweenness, b_nodes = greedy_remove_highest_betweenness_centrality_nodes(
            graph=G_betweenness,
            k=nodes_to_remove,
            initial_infected=initial_infected
        )
        betweenness_infection_probabilities = CS.independent_cascade_MARKOV(
            graph=G_betweenness,
            num_simulations=num_simulations,
            initial_infected=initial_infected
        )
        betweenness_influence = sum(betweenness_infection_probabilities.values())/len(betweenness_infection_probabilities)
        betweenness_influence_list.append(betweenness_influence)

        # Greedy Closeness
        G_closeness = G.copy()
        G_closeness, c_nodes = greedy_remove_highest_closeness_centrality_nodes(
            graph=G_closeness,
            k=nodes_to_remove,
            initial_infected=initial_infected
        )
        closeness_infection_probabilities = CS.independent_cascade_MARKOV(
            graph=G_closeness,
            num_simulations=num_simulations,
            initial_infected=initial_infected
        )
        closeness_influence = sum(closeness_infection_probabilities.values())/len(closeness_infection_probabilities)
        closeness_influence_list.append(closeness_influence)
    ## Calculate the statistic for this graph size
    raw_influence_mean = sum(raw_influence_list)/len(raw_influence_list)
    raw_influence_std = sum([(x - raw_influence_mean)**2 for x in raw_influence_list])/len(raw_influence_list)
    degree_influence_mean = sum(degree_influence_list)/len(degree_influence_list)
    degree_influence_std = sum([(x - degree_influence_mean)**2 for x in degree_influence_list])/len(degree_influence_list)
    eigenvector_influence_mean = sum(eigenvector_influence_list)/len(eigenvector_influence_list)
    eigenvector_influence_std = sum([(x - eigenvector_influence_mean)**2 for x in eigenvector_influence_list])/len(eigenvector_influence_list)
    katz_influence_mean = sum(katz_influence_list)/len(katz_influence_list)
    katz_influence_std = sum([(x - katz_influence_mean)**2 for x in katz_influence_list])/len(katz_influence_list)
    influence_influence_mean = sum(influence_influence_list)/len(influence_influence_list)
    influence_influence_std = sum([(x - influence_influence_mean)**2 for x in influence_influence_list])/len(influence_influence_list)
    betweenness_influence_mean = sum(betweenness_influence_list)/len(betweenness_influence_list)
    betweenness_influence_std = sum([(x - betweenness_influence_mean)**2 for x in betweenness_influence_list])/len(betweenness_influence_list)
    closeness_influence_mean = sum(closeness_influence_list)/len(closeness_influence_list)
    closeness_influence_std = sum([(x - closeness_influence_mean)**2 for x in closeness_influence_list])/len(closeness_influence_list)
    df = df.append({
        'n': n,
        'b': b,
        'raw_influence_mean': raw_influence_mean,
        'raw_influence_std': raw_influence_std,
        'degree_influence_mean': degree_influence_mean,
        'degree_influence_std': degree_influence_std,
        'eigenvector_influence_mean': eigenvector_influence_mean,
        'eigenvector_influence_std': eigenvector_influence_std,
        'katz_influence_mean': katz_influence_mean,
        'katz_influence_std': katz_influence_std,
        'influence_influence_mean': influence_influence_mean,
        'influence_influence_std': influence_influence_std,
        'betweenness_influence_mean': betweenness_influence_mean,
        'betweenness_influence_std': betweenness_influence_std,
        'closeness_influence_mean': closeness_influence_mean,
        'closeness_influence_std': closeness_influence_std
    }, ignore_index=True)
df.to_csv('./results/results.csv', index=False)
ic(df)