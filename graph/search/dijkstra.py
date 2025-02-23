from queue import PriorityQueue
import math

INF = math.inf

def DijkstraSPA(G, v):
    '''
    G: adjacency list with weight in edge of Graph
        [[(1, 10), ...], ...]
    v: begin vertex
    '''
    p = PriorityQueue()
    for u in range(len(G)):
        p.put((INF, u))
    p.put((0, v))

    n = len(G)
    dist = [INF] * n
    dist[v] = 0

    while not p.empty():
        d, u = p.get() # return the min dist from v
        for nei, w in G[u]:
            if dist[nei] > d + w: # find the shorter path and update
                dist[nei] = d + w
                p.put((dist[nei], nei))

    return dist