import networkx as nx
from networkx.generators.community import LFR_benchmark_graph

n = 500  # number of nodes

# List of parameter tuples: (tau1, tau2, mu, seed)
params = [
    (2.5, 1.5, 0.1, 42),
    (2.5, 1.5, 0.2, 43),
    (2.5, 2.0, 0.1, 44),
    (2.0, 1.5, 0.1, 45),
    (2.0, 1.5, 0.2, 46),
    (3.0, 1.5, 0.1, 47),
    (2.5, 1.0, 0.1, 48),
    (2.5, 1.5, 0.3, 49),
    (2.5, 2.0, 0.2, 50),
    (3.0, 2.0, 0.1, 51),
    (2.0, 1.0, 0.1, 52),
    (2.5, 1.0, 0.2, 53),
    (2.0, 1.5, 0.3, 54),
    (3.0, 1.5, 0.2, 55),
    (3.0, 2.0, 0.2, 56),
]

# Generate LFR benchmark graphs with different parameter values
for i, (tau1, tau2, mu, seed) in enumerate(params):
    G = LFR_benchmark_graph(n, tau1, tau2, mu, average_degree=10, min_community=25, seed=seed)
    nx.write_graphml(G, f'lfr_graph_{i}.graphml')