import os
import json
import random
import networkx as nx


def evolve(g: nx.DiGraph, max_node: int):
    lp = random.random()
    nodes = list(g.nodes)
    n = len(nodes)
    if lp < 0.5:
        i1 = random.randint(0, n - 1)
        i2 = random.randint(0, n - 1)
        if i1 == i2:
            return
        if g.has_edge(nodes[i1], nodes[i2]):
            return
        if lp < 0.25:
            g.add_edge(nodes[i1], nodes[i2])
        else:
            g.remove_edge(nodes[i1], nodes[i2])


def generate(max_node: int, number: int = 100):
    random.seed(1234)
    directory = f'data/{max_node}'
    if not os.path.exists(directory):
        os.mkdir(directory)

    for i in range(1, number + 1):
        g1 = nx.fast_gnp_random_graph(max_node, 1 / 3, directed=True)
        g2 = g1.copy()
        n_evolve = random.randint(1, max_node)
        for _ in range(n_evolve):
            evolve(g2, max_node)

        file = f'{directory}/{i}.json'
        with open(file, 'w+') as fp:
            json.dump({'adj1': nx.adjacency_matrix(g1).todense().tolist(),
                       'adj2': nx.adjacency_matrix(g2).todense().tolist()}, fp)
