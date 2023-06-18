from convertGraph import AdjToNx
from convertGraph import NxToAdj
import networkx as nx
import community 
def expected_edges(node1, node2, degrees, m):
    return degrees[node1] * degrees[node2] / (2 * m)



def modularity(adj_list, communities):
    m = sum(len(adj_list[node]) for node in adj_list) / 2
    degrees = {node: len(adj_list[node]) for node in adj_list}
    q = 0
    
    for community in set(communities.values()):
        nodes_in_community = [node for node in adj_list if communities[node] == community]
        expected_edges_in_community = sum(expected_edges(node1, node2, degrees, m)
                                          for node1 in nodes_in_community
                                          for node2 in nodes_in_community)
        actual_edges_in_community = sum(1 for node1 in nodes_in_community
                                        for node2 in adj_list[node1]
                                        if communities[node1] == communities[node2])
        q += (actual_edges_in_community - expected_edges_in_community) / (2 * m)
    
    return q


def merge_communities(adj_matrix, CS, delta, vector_comm):
    mod = modularity(adj_matrix, vector_comm)

    l = set()
    for label in vector_comm.values():
        if label != -1:
            l.add(label)

# //Select the pair of communities with the largest modularity increment:

import numpy as np

def find_max_modularity_increment(G, CS):
    
    # Find the pair of communities with the largest modularity increment.
    # G: the graph as an adjacency matrix.
    # CS: the current community structure as a dictionary mapping node ids to community ids.
    # Returns a tuple (X, X', delta_Q) where X and X' are the communities with the largest modularity increment,
    # and delta_Q is the modularity increment when merging X and X'.

    n = G.shape[0]  # number of nodes
    m = G.sum() / 2  # number of edges
    k = G.sum(axis=1)  # degree of each node
    q = np.zeros((n, n))  # modularity matrix
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            q[i, j] = G[i, j] - k[i] * k[j] / (2 * m)
            if CS[i] == CS[j]:
                q[i, j] += k[i] * k[j] / (2 * m)
    max_delta_Q = -1
    max_X = None
    max_Xprime = None
    for X in set(CS.values()):
        for Xprime in set(CS.values()):
            if X == Xprime:
                continue
            delta_Q = 0
            for i in range(n):
                for j in range(n):
                    if CS[i] == X and CS[j] == Xprime:
                        delta_Q += q[i, j]
                    elif CS[i] == Xprime and CS[j] == X:
                        delta_Q += q[i, j]
            delta_Q /= (2 * m)
            if delta_Q > max_delta_Q:
                max_delta_Q = delta_Q
                max_X = X
                max_Xprime = Xprime
    return max_X, max_Xprime, max_delta_Q

    # Merge the selected pair of communities if the modularity increment is larger than modularity increment  threshold 

    import networkx as nx
import community

def merge_communities(G, k):
    # Calculate the modularity of the initial community structure
    initial_modularity = community.modularity(G, nx.get_node_attributes(G, 'community'))

    # Repeat until no further merges improve the modularity
    while True:
        # Calculate the modularity increment resulting from merging each pair of communities
        modularity_increments = {}
        communities = set(nx.get_node_attributes(G, 'community').values())
        for i in communities:
            for j in communities:
                if i < j:
                    merged_partition = nx.get_node_attributes(G, 'community').copy()
                    for node, community_id in merged_partition.items():
                        if community_id == i or community_id == j:
                            merged_partition[node] = i
                    merged_modularity = community.modularity(G, merged_partition)
                    modularity_increment = merged_modularity - initial_modularity
                    modularity_increments[(i, j)] = modularity_increment

        # Find the pair of communities with the largest modularity increment
        if not modularity_increments:
            break
        best_pair, best_increment = max(modularity_increments.items(), key=lambda x: x[1])
        if best_increment <= k:
            break

        # Merge the selected pair of communities
        i, j = best_pair
        merged_partition = nx.get_node_attributes(G, 'community').copy()
        for node, community_id in merged_partition.items():
            if community_id == i or community_id == j:
                merged_partition[node] = i
        nx.set_node_attributes(G, merged_partition, 'community')

    return G
    return mod
def merge_communities(al, label, delta):
    adj_list = AdjToNx(al)

    return NxToAdj(adj_list)