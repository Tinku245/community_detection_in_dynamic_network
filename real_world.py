import networkx as nx
import matplotlib.pyplot as plt
import os
from get_communities import get_communities
from merge_communities import merge_communities
from node_addition import node_addition
from edge_addition import edge_addition
from edge_removal import edge_removal
from measureReal import calculate_measures_real
from convertGraph import AdjToNx
from convertGraph import NxToAdj


# timastamps from real world data sets
dataset_content = [991846192, 1001369511, 998407138, 996510960, 996529015]


G = nx.Graph()
adj_list = {}
adj_list[0] = []
path = os.path.realpath(__file__)
dir = os.path.dirname(path)
dir = dir.replace('sna_project', 'sna_project\datasets\enron_email.txt')
edge_file =  open(dir,'r')
edge_list = edge_file.readlines()
for edge in edge_list:
    edge = edge.split()
    if int(edge[3]) != dataset_content[0]:
        continue
    G.add_node(int(edge[0]))
    G.add_node(int(edge[1]))
    G.add_edge(int(edge[0]), int(edge[1]))
    if int(edge[0]) not in adj_list:
        adj_list[int(edge[0])] = []
    if int(edge[1]) not in adj_list:
        adj_list[int(edge[1])] = []
    adj_list[int(edge[0])].append(int(edge[1]))
    adj_list[int(edge[1])].append(int(edge[0]))
G = G.to_undirected()
nx.draw(G, with_labels = False)
plt.show()

# print(adj_list)
# Algorithm
# Step 1: Detect community structure from the first snapshot 
label = {}
CS = get_communities(adj_list, label)
print(CS)
calculate_measures_real(G, CS)
CS = merge_communities(adj_list, label, 0.005)


# Step 2: Detect community structure from every snapshot incrementally on the basis of previous snapshot 

for snapshot in range(1,5):
    prev_list = adj_list
    dir = dir.replace(str(snapshot-1), str(snapshot))
    adj_list = {}
    adj_list[0] = []
    edge_file =  open(dir,'r')
    edge_list = edge_file.readlines()
    for edge in edge_list:
        edge = edge.split()
        if int(edge[3]) != dataset_content[snapshot]:
            continue
        G.add_node(int(edge[0]))
        G.add_node(int(edge[1]))
        G.add_edge(int(edge[0]), int(edge[1]))
        if int(edge[0]) not in adj_list:
            adj_list[int(edge[0])] = []
        if int(edge[1]) not in adj_list:
            adj_list[int(edge[1])] = []
        adj_list[int(edge[0])].append(int(edge[1]))
        adj_list[int(edge[1])].append(int(edge[0]))
    G = G.to_undirected()
    label = {}
    CS = get_communities(adj_list, label)
    print(CS)
    calculate_measures_real(G, CS)

    # Handling node addition
    adj_list = node_addition(adj_list, label, prev_list)
    # Handling edge addition
    adj_list = edge_addition(adj_list, label, prev_list, 0.5)
    # Handling edge removal
    adj_list = edge_removal(adj_list, label, prev_list, 1/3)


    nx.draw(G, with_labels = False)
    plt.show()