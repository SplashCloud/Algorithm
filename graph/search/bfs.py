from collections import deque
import math

INF = math.inf

def BFS(G, v):
    '''
    G: adjacency list of graph
    v: begin vertex
    '''
    q = deque()
    n = len(G)
    dist = [INF] * n

    q.append(v)
    dist[v] = 0
    while len(q) > 0:
        u = q.popleft()
        for neighbor in G[u]:
            if dist[neighbor] == INF: # not visited
                dist[neighbor] = dist[u] + 1
                q.append(neighbor)

    return dist