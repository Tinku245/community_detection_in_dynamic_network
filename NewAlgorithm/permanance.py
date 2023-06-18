
# Permanence Measure
def Permanence(G, label):

    def I(node):
        cnt = 0
        for neighbor in G[node]:
            if label[neighbor] == label[node]:
                cnt += 1
        return cnt
    
    def D(node):
        return len(G[node])

    def E_MAX(node):
        freq = {}
        for neighbor in G[node]:
            if label[node] == label[neighbor]:
                continue
            if label[neighbor] not in freq:
                freq[label[neighbor]] = 1
            else:
                freq[label[neighbor]] += 1 
        mx = 0
        for f in freq:
            mx = max(freq[f], mx)
        return mx

    def CIN(node):
        def NOICN(node):#num_of_internal_connection_of_neighbor
            cnt = 0
            for neighbor in G[node]:
                for nn in G[node]:
                    if nn != neighbor and (neighbor in G[nn]):
                        cnt += 1
        return cnt//2
        def denom(node):
            return I(node)*(I(node)-1)/2
        return NOICN(node)/denom(node)

    avg_permanence = 0
    for node in G:
        avg_permanence += ((I(node)/(E_MAX(node)*D(node)))-(1-CIN(node)))
    return avg_permanence/len(G)