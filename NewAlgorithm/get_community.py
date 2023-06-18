def get_community(adj_list, label):
    for node in adj_list:
        label[node] = 0
    CS = {}
    def u_set(adj_list, label):
        unclassified_set = []
        for v in adj_list:
            if label[v] == 0:
                unclassified_set.append(v)
        return unclassified_set

    def findCommonNodes(u, v, adj_list):
        lst = []
        for n_u in adj_list[u]:
            for n_v in adj_list[v]:
                if n_u == n_v:
                    lst.append(n_u)
        return lst

    sameComm = []
    diffComm = []

    # Assign community based on modified algorithm 

    for v in u_set(adj_list, label):
        isChanged = u_set(adj_list, label)
        sameComm.append(v)
        for neighbor in adj_list[v]:
            lst = findCommonNodes(v, neighbor, adj_list)
            isDifferentComm = False
            for u in lst:
                lls = adj_list[v]
                lls.append(v)
                if u not in lls:
                    isDifferentComm = True
                    diffComm.append(neighbor)
            if isDifferentComm == False:
                sameComm.append(neighbor)

        
        # max frequency label if not zero
        def max_freq_label(adj_list, label):
            freq = {}
            mx = 0
            for l in label:
                if label[l] not in freq:
                    freq[label[l]] = 1
                else:
                    freq[label[l]] += 1
            for f in freq:
                if freq[f] > mx:
                    mx = freq[f]
            return mx
        mfl = max_freq_label(adj_list, label)

        if mfl == 0:
            for node in sameComm:
                label[node] = 1
        else:
            for node in sameComm:
                if label[node] != 0:
                    label[node] = mfl

        sameComm = []

        if isChanged == u_set(adj_list, label):
            break
    
    # assign the remaining nodes label to max occurence of neighbors label
    
    def max_freq_neighb_label(u, adj_list, label):
        freq = {}
        mx = 0
        mxL = 0
        for nn in adj_list[u]:
            if label[nn] not in freq:
                freq[label[nn]] = 1
            else:
                freq[label[nn]] += 1
        for f in freq:
            if mx < freq[f]:
                mx = freq[f]
                mxL = f
        return mxL
        
    remaining_nodes = u_set(adj_list, label)
    for rn in remaining_nodes:
        mfn = max_freq_neighb_label(rn, adj_list, label)
        if mfn == 0:
            label[rn] = 1
        label[rn] = mfn
    

    # Return the final community structure
    print(label)
    for l in label:
        if label[l] not in CS:
            CS[label[l]] = []
        CS[label[l]].append(l+1)
    return CS
    
