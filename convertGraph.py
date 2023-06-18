import networkx as nx
# adj_list to networkx Graph
def AdjToNx(adj_list):
    G = nx.Graph()
    # G.add_nodes_from(adj_list.keys())
    # for node, neighbors in adj_list.items():
    #     for neighbor in neighbors:
    #         G.add_edge(node, neighbor)
    for u in adj_list:
        G.add_node(u)
        for neighbor in adj_list[u]:
            G.add_edge(u, neighbor)
    return G 


# networkx Graph to adj_list
def NxToAdj(G):
    adj_list = {}
    for node in G.nodes():
        adj_list[node] = list(G.neighbors(node))
    return adj_list