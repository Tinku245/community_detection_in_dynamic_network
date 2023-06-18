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
from lfr import lfr


adj_list = {}
GG = lfr()

# Step 2: Detect community structure from every snapshot incrementally on the basis of previous snapshot 
for snapshot in range(4):
    prev_list = adj_list

    G = GG[snapshot]
    nx.draw(G, with_labels = False)
    plt.show()


    # Algorithm
    # Step 1: Detect community structure from the first snapshot 
    label = {}
    # CS = get_communities(adj_list, label)
    communities_generator = nx.community.girvan_newman(G)
    top_level_communities = next(communities_generator)
    CS = next(communities_generator)
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