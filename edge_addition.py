from convertGraph import AdjToNx
from convertGraph import NxToAdj
def adjust_community_affiliations(G_prev, G_curr):
    # Collect newly added edges
    new_edges = set(G_curr.edges()) - set(G_prev.edges())
    return G_curr
    for (u, v) in new_edges:
        # Check if u and v are in the same community
        if G_curr.nodes[u]['community'] == G_curr.nodes[v]['community']:
            continue
        
        # Check if most of u's neighbors are in v's community and vice versa
        u_neighbors = set(G_curr.neighbors(u))
        v_neighbors = set(G_curr.neighbors(v))
        u_neighbors_in_v = u_neighbors.intersection(set(G_curr.nodes[n]['community'] == G_curr.nodes[v]['community'] for n in u_neighbors))
        v_neighbors_in_u = v_neighbors.intersection(set(G_curr.nodes[n]['community'] == G_curr.nodes[u]['community'] for n in v_neighbors))
        if len(u_neighbors_in_v) > 0.5 * len(u_neighbors) and len(v_neighbors_in_u) > 0.5 * len(v_neighbors):
            # Create a new community for u and v
            new_community = max(nx.get_node_attributes(G_curr, 'community').values()) + 1
            G_curr.nodes[u]['community'] = new_community
            G_curr.nodes[v]['community'] = new_community
            
            # Move some neighbor nodes into the new community
            for node in u_neighbors:
                if G_curr.nodes[node]['community'] == G_curr.nodes[u]['community']:
                    if len(set(G_curr.neighbors(node)).intersection(v_neighbors)) > 0.5 * len(G_curr.neighbors(node)):
                        G_curr.nodes[node]['community'] = new_community
            for node in v_neighbors:
                if G_curr.nodes[node]['community'] == G_curr.nodes[v]['community']:
                    if len(set(G_curr.neighbors(node)).intersection(u_neighbors)) > 0.5 * len(G_curr.neighbors(node)):
                        G_curr.nodes[node]['community'] = new_community
        elif len(u_neighbors_in_v) > len(v_neighbors_in_u):
            G_curr.nodes[u]['community'] = G_curr.nodes[v]['community']
        else:
            G_curr.nodes[v]['community'] = G_curr.nodes[u]['community']
            
    return G_curr
def edge_addition(adj_list, label, prev_list, delta):
    G_prev = AdjToNx(adj_list)
    G_curr = AdjToNx(prev_list)
    G_curr = adjust_community_affiliations(G_prev, G_curr)
    return NxToAdj(G_curr)

