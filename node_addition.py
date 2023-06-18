import networkx as nx

def node_addition(adj_list, label, prev_list):
    # Identify the common nodes and new nodes
    common_nodes = []
    new_nodes = []
    for nu in adj_list:
        for nv in prev_list:
            if nu == nv:
                common_nodes.append(nv)
            else:
                new_nodes.append(nv)

    Nadj_list = nx.Graph()            
                                                
    # Add the common nodes to the spiderweb model
    for node in common_nodes:
        Nadj_list.add_node(node)

    # Add the new nodes to the spiderweb model and connect them to the core nodes
    def unclassified_set(label):
        u_set = []
        for l in label:
            if label[l] == 0:
                u_set.append(l)
        return u_set
    
    def most_frequent_classified_neighbor_label(u):
        dct = {}
        mx = 0
        for neighbor in adj_list[u]:
            if label[neighbor] != 0:
                dct[label[neighbor]] = dct.get(label[neighbor], 0) + 1
        ans = 0
        for d in dct:
            if dct[d] > mx:
                mx = dct[d]
                ans = d 
        return ans

    unclassified = unclassified_set(label)
    for u in unclassified:
        ll = most_frequent_classified_neighbor_label(u)
        if ll != 0:
            label[u] = ll
            Nadj_list.add_node(u)

    return Nadj_list