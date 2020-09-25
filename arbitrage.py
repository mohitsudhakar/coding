import math
import collections

def bellman_ford(edges, V, source):
    dist = [float('inf')]*V
    pre = [-1]*V
    dist[source] = 0
    for _ in range(V-1):
        for u,v,w in edges:
            if u in dist and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pre[v] = u


    negEdgeCycle = False
    for u,v,w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print_cycle = [v, u]
            # Start from the source and go backwards until you see the source vertex again or any vertex that already exists in print_cycle array
            while pre[u] not in print_cycle:
                print_cycle.append(pre[u])
                u = pre[u]
            print("Arbitrage Opportunity:")
            print(" --> ".join([vertices[p] for p in print_cycle[::-1]]))


def analyze(graph):
    V = len(vertices)
    # graph is edge list
    # products of weights w1 * w2 * w3 *... > 1
    # - log(w1 * w2 * w3 *...) < 0
    # - log(w1) - log(w2) - log(w3) - ... < 0
    # run bellman ford to find negative weight cycle

    print('num vertices =', V)
    print('num edges =', len(graph))

    for edge in graph:
        edge[2] = -math.log(edge[2])

    for source in v_ids:
        bellman_ford(graph, V, source)

if __name__ == '__main__':

    with open('prices.csv', 'r') as f:
        lines = f.readlines()
        lines = [line.split(',') for line in lines]
        lines.pop(0)

    vertices = set()
    for line in lines:
        vertices.add(line[0])
        vertices.add(line[1])
    vertices = list(vertices)
    v_ids = range(len(vertices))
    map_v_to_id = collections.defaultdict(int)
    for i in v_ids:
        map_v_to_id[vertices[i]] = i

    lines = [[line[0], line[1], line[2]] for line in lines if float(line[2]) > 0]

    # map_id_to_v = collections.defaultdict(str)
    # for l in lines:
    #     map_id_to_v[]

    graph = [[map_v_to_id[line[0]], map_v_to_id[line[1]], float(line[2])]
             for line in lines]
    analyze(graph)

"""
BQX,BTC,0.00001532
BQX,ETH,0.00045090
ETH,BTC,0.03375800
"""