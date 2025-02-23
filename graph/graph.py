import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def gen_random_graph(n: int, min_degree: int, max_degree: int):
    '''
        generate a undirect graph with n vertices, 
            each vertex has at most max_degree neighbors, and at least min_degree neighbors
    '''
    adjacency_list = [[] for _ in range(n)]
    for v in range(n):
        degree = len(adjacency_list[v])
        if degree >= min_degree and degree <= max_degree:
            continue
        candidates = np.array([
            u for u in range(n)
            if u not in adjacency_list[v]
            and u != v # neighbor is not self
            and len(adjacency_list[u]) < max_degree # if select previous vertices, need to ensure its degree < max
            ])
        more = np.random.randint(min_degree-degree, min(max_degree-degree, len(candidates))+1) # add more neighbors to v
        neighbors = np.random.choice(candidates, size=more, replace=False)
        adjacency_list[v].extend(neighbors.tolist())
        # add v into neighbors' list
        for nei in neighbors:
            adjacency_list[nei].append(v)
    # TODO: ensure the connectivity
    return adjacency_list

class Graph:

    def __init__(self, adjacency_list):
        assert adjacency_list is not None

        self.graph = adjacency_list
    
    @classmethod
    def random_graph(cls, n, max_degree, min_degree=1):
        adj_list = gen_random_graph(n, min_degree, max_degree)
        return cls(adj_list)


    def visualize(self):
        """
        将邻接表可视化为图形
        :param adjacency_list: 邻接表
        """
        G = nx.Graph()
        
        # 添加所有顶点
        G.add_nodes_from(range(len(self.graph)))
        
        # 添加所有边
        for i, neighbors in enumerate(self.graph):
            for neighbor in neighbors:
                G.add_edge(i, neighbor)
        
        # 绘制图形
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(G)  # 使用弹簧布局
        nx.draw(G, pos, with_labels=True, node_color='lightblue', 
                node_size=500, font_size=16, font_weight='bold')
        plt.show()
        plt.savefig('graph.png')


if __name__ == '__main__':
    graph = Graph.random_graph(5, max_degree=3, min_degree=2)
    graph.visualize()