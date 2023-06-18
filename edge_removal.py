from convertGraph import AdjToNx
from convertGraph import NxToAdj
import networkx as nx
def remove_edge(adj_list, prev_graph):

    # Create the previous graph and assign communities to the nodes
    prev_graph = nx.karate_club_graph()
    communities = nx.algorithms.community.greedy_modularity_communities(prev_graph)

    # Remove some edges from the previous graph to create a new graph
    new_graph = prev_graph.copy()
    new_graph.remove_edge(0, 1)
    new_graph.remove_edge(0, 2)

    # Create a dictionary to store the communities of the nodes in the previous graph
    comm_dict = {}
    for i, comm in enumerate(communities):
        for node in comm:
            comm_dict[node] = i

    # Create a new graph and add the nodes from the previous graph to the new graph
    new_prev_nodes = prev_graph.nodes()
    new_graph.add_nodes_from(new_prev_nodes)

    # Assign the communities of the nodes in the previous graph to the nodes in the new graph
    for node in new_prev_nodes:
        new_graph.nodes[node]['community'] = comm_dict[node]

    # Print the communities of the nodes in the new graph
    # for node in new_graph.nodes():
    #     print(f"Node {node} belongs to community {new_graph.nodes[node]['community']}")
    return new_graph

def edge_removal(al, label, pl, gamma):
    adj_list = AdjToNx(al)
    prev_list = AdjToNx(pl)
    G = remove_edge(adj_list, prev_list)
    return NxToAdj(adj_list)


