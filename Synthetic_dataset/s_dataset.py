import networkx as nx
import random
import pandas as pd
import os
import shutil
p = [
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
    (3.0, 2.0, 0.2, 56)
]
def intial_graph(i,j):
    G = nx.LFR_benchmark_graph(500, p[0], p[1], p[2], average_degree=10, min_community=25, seed=p[3])
    G.remove_edges_from(nx.selfloop_edges(G))
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(1, 7)
    df = pd.DataFrame([(u, v, d['weight']) for u, v, d in G.edges(data=True)], columns=['source', 'target', 'weight'])
    df.to_csv(f'syn-datasets{i}/graph{j}.csv', index=False)
    communities = {frozenset(G.nodes[v]["community"]) for v in G}
    ground_truth = [list(c) for c in communities]
    print(ground_truth)
for i in range(1,4):
    folder_name = "syn-datasets"+str(i)
    if os.path.exists(folder_name) and os.path.isdir(folder_name):
        shutil.rmtree(os.getcwd()+'\\'+folder_name)
    os.mkdir(folder_name)
    for j in range(6):
        intial_graph(i,j)
    