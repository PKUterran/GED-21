import json
import numpy as np
import networkx as nx
from typing import Tuple


def load_nx(path: str = 'data/9/1.json') -> Tuple[nx.Graph, nx.Graph]:
    with open(path) as fp:
        d = json.load(fp)
    g1, g2 = nx.from_numpy_matrix(np.array(d['adj1']), create_using=nx.DiGraph), \
             nx.from_numpy_matrix(np.array(d['adj2']), create_using=nx.DiGraph)
    return g1, g2
