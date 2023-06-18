import networkx as nx
from convertGraph import AdjToNx
from sklearn import metrics
import community
from sklearn.metrics.cluster import normalized_mutual_info_score


def modularity(G, communities):
    m = G.number_of_edges()
    Q = 0
    for c in communities:
        for i in c:
            for j in c:
                if i != j:
                    Aij = 1 if G.has_edge(i,j) else 0
                    ki = G.degree(i)
                    kj = G.degree(j)
                    Q += (Aij - ki*kj/(2*m))
    return Q/(2*m)


def conductance(graph, communities):
    conductances = []
    for community in communities:
        internal_edges = 0
        external_edges = 0
        for node in community:
            for neighbor in graph[node]:
                if neighbor in community:
                    internal_edges += 1
                else:
                    external_edges += 1
        if external_edges + 2*internal_edges == 0:
            conductance = 1.0
        else:
            conductance = external_edges / (external_edges + 2*internal_edges)
        conductances.append(conductance)
    return sum(conductances)/len(conductances)


def expansion(graph, communities):
    expansions = []
    for community in communities:
        internal_edges = 0
        external_edges = 0
        for node in community:
            for neighbor in graph[node]:
                if neighbor in community:
                    internal_edges += 1
                else:
                    external_edges += 1
        expansio = external_edges/len(community)
        expansions.append(expansio)
    return sum(expansions)/len(expansions)


def external_density(graph, communities):
    external_densities = []
    for community in communities:
        internal_edges = 0
        external_edges = 0
        for node in community:
            for neighbor in graph[node]:
                if neighbor in community:
                    internal_edges += 1
                else:
                    external_edges += 1
        k = len(community)
        if k == 1:
            return 0
        external_density = external_edges / (k * (k-1) / 2)
        external_densities.append(external_density)
    return sum(external_densities)/len(external_densities)


def calculate_ari(graph, communities):
   
    # create a dictionary to map nodes to their corresponding community labels
    node2comm = {}
    for i, comm in enumerate(communities):
        for node in comm:
            node2comm[node] = i
    # generate the label lists
    ground_truth = community.best_partition(graph)
    predicted_labels = []
    true_labels = []
    i = 0
    for node in node2comm:
        j = i
        for node in node2comm:
            if(i==node):
                predicted_labels.append(node2comm.get(node))
                i += 1
        if(j==i):
            i += 1
    i = 0
    for node in ground_truth:
        j = i
        for node in ground_truth:
            if(i==node):
                true_labels.append(ground_truth.get(node))
                i += 1
        if(j==i):
            i += 1
    # calculate the Adjusted Rand Index (ARI) score
    ari_score = metrics.adjusted_rand_score(true_labels, predicted_labels)

    return ari_score


#tested
def calculate_nmi(graph, communities):
    
    # create a dictionary to map nodes to their corresponding community labels
    node2comm = {}
    for i, comm in enumerate(communities):
        for node in comm:
            node2comm[node] = i
    # generate the label lists
    ground_truth = community.best_partition(graph)
    predicted_labels = []
    true_labels = []
    i = 0
    for node in node2comm:
        j = i
        for node in node2comm:
            if(i==node):
                predicted_labels.append(node2comm.get(node))
                i += 1
        if(j==i):
            i += 1
    i = 0
    for node in ground_truth:
        j = i
        for node in ground_truth:
            if(i==node):
                true_labels.append(ground_truth.get(node))
                i += 1
        if(j==i):
            i += 1
    # calculate the Adjusted Rand Index (ARI) score
    nmi_score = metrics.normalized_mutual_info_score(true_labels, predicted_labels)

    return nmi_score

def calculate_measures_real(graph, communities):

    # modularity_g = modularity(graph, communities)
    # print("Modularity of The graph is: " + str(modularity_g))
    conductance_g = conductance(graph, communities)
    print("Conductance of the graph is: " + str(conductance_g))
    expansion_g = expansion(graph, communities)
    print("Expansion of the graph is: " + str(expansion_g))
    external_density_g = external_density(graph, communities)
    print("External Density of the graph is: " + str(external_density_g))
    nmi_g = calculate_nmi(graph, communities)
    print("NMI of the graph is: " + str(nmi_g))
    ari_g = calculate_ari(graph, communities)
    print("ARI of the graph is: " + str(ari_g))