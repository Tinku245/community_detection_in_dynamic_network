import random
import networkx as nx
from networkx.generators.community import LFR_benchmark_graph
import matplotlib.pyplot as plt
import os
from get_communities import get_communities
from merge_communities import merge_communities
from node_addition import node_addition
from edge_addition import edge_addition
from edge_removal import edge_removal
from measuresNx import calculate_measures_NX
from convertGraph import AdjToNx
from convertGraph import NxToAdj


# n = random.randint(50,70)
# tau1 = 3
# tau2 = 1.5
# mu = 0.1
# G = LFR_benchmark_graph(
#     n, tau1, tau2, mu, average_degree=5, min_community=10, seed=10
# )
# nx.draw(G, with_labels = True)
# plt.show()
n = 250
tau1 = 3
tau2 = 1.5
mu = 0.1
G = LFR_benchmark_graph(
    n, tau1, tau2, mu, average_degree=5, min_community=20, seed=10
)


# Algorithm
# Step 1: Detect community structure from the first snapshot 
label = {}
CS = get_communities(adj_list, label)
print(CS)
calculate_measures_NX(G, CS)
adj_list = {}
CSS = merge_communities(adj_list, label, 0.005)


# Step 2: Detect community structure from every snapshot incrementally on the basis of previous snapshot 
for snapshot in range(1):
    prev_list = adj_list

    n = 1000
    tau1 = 3
    tau2 = 1.5
    mu = 0.1
    G = LFR_benchmark_graph(
        n, tau1, tau2, mu, average_degree=10, min_community=10, seed=10
    )
    nx.draw(G, with_labels = False)
    plt.show()


    # Algorithm
    # Step 1: Detect community structure from the first snapshot 
    label = {}
    CS = get_communities(adj_list, label)
    print(CS)
    calculate_measures_NX(G, CS)
    adj_list = {}
    CSS = merge_communities(adj_list, label, 0.005)

    # Handling node addition
    adj_list = node_addition(adj_list, label, prev_list)
    # Handling edge addition
    adj_list = edge_addition(adj_list, label, prev_list, 0.5)
    # Handling edge removal
    adj_list = edge_removal(adj_list, label, prev_list, 1/3)


    nx.draw(G, with_labels = True)
    plt.show()