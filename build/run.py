import networkx as nx

from data.load_nx import load_nx


def run():
    g1, g2 = load_nx()
    print(nx.adjacency_matrix(g1).todense())
    print(nx.adjacency_matrix(g2).todense())
    print(nx.graph_edit_distance(g1, g2))
