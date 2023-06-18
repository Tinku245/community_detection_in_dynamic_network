import networkx as nx
import random


def lfr():
    # Set the initial parameters
    n = 1000 # number of nodes
    tau1 = 2.0 # power-law exponent for the degree distribution of nodes
    tau2 = 1.5 # power-law exponent for the degree distribution of communities
    mu = 0.1 # fraction of internal edges in each community
    timesteps = 5 # number of time steps

    # Generate the initial graph
    G = nx.LFR_benchmark_graph(n, tau1, tau2, mu, average_degree=5, min_community=20, seed=0)

    # Define the initial communities
    communities = {frozenset(G.nodes[v]['community']) for v in G}
    GG = []

    # Perform the dynamic community generation
    for t in range(timesteps):
        # Birth
        node = max(G.nodes()) + 1
        G.add_node(node)
        deg = nx.utils.powerlaw_sequence(1, tau1)[0]
        targets = set(random.choices(sorted(list(G.nodes())), k=int(deg)))
        G.add_edges_from((node, t) for t in targets)

        # Switch
        if random.random() < 0.1:
            u, v = random.sample(list(G.nodes()), 2)
            cu = G.nodes[u]['community']
            cv = G.nodes[v]['community']
            G.nodes[u]['community'] = cv
            G.nodes[v]['community'] = cu
            communities.discard(cu)
            communities.discard(cv)
            communities.add(frozenset(G.nodes[u]['community']))
            communities.add(frozenset(G.nodes[v]['community']))

        # Expand
        if random.random() < 0.1:
            c = random.choice(list(communities))
            node = max(G.nodes()) + 1
            G.add_node(node)
            deg = nx.utils.powerlaw_sequence(1, tau1)[0]
            targets = set(random.choices(sorted(list(G.nodes())), k=int(deg)))
            targets &= c
            G.add_edges_from((node, t) for t in targets)
            G.nodes[node]['community'] = c
            communities.discard(c)
            communities.add(frozenset(G.nodes[node]['community']))

        # Merge
        if random.random() < 0.1:
            c1, c2 = random.sample(list(communities), 2)
            c = c1.union(c2)
            for node in c:
                G.nodes[node]['community'] = c
            communities.discard(c1)
            communities.discard(c2)
            communities.add(frozenset(c))
        adj_list = nx.to_dict_of_lists(G)
        GG.append(G)
    return GG

