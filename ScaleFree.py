import networkx as nx
import matplotlib.pyplot as plt

def new_scale_graph(num, gammat):
    G = nx.scale_free_graph(num, 0.4, 0.59, 0.01, gammat, 0, None, None)
    nx.draw(G)
    plt.savefig("1.png")
    plt.show()
    return G


new_scale_graph(100, 0.9)
