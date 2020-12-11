
import networkx as nx
import matplotlib.pyplot as plt

G = nx.path_graph(100)
nx.draw_random(G)
plt.show()