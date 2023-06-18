import networkx as nx
import matplotlib.pyplot as plt
import os
from get_community import get_community


G = nx.Graph()
adj_list = {}
adj_list[0] = []
path = os.path.realpath(__file__)
dir = os.path.dirname(path)
dir = dir.replace('NewAlgorithm', 'NewAlgorithm\case01.txt')
edge_file =  open(dir,'r')
edge_list = edge_file.readlines()
for edge in edge_list:
    edge = edge.split()
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
nx.draw(G, with_labels = True)
plt.show()


# Algorithm
# Step 1: Detect community structure from the first snapshot 
label = {}
CS = get_community(adj_list, label)
print(CS)