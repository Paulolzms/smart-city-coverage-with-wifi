import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

def view_graph(G, node_color='red', edge_color='gray', node_size=10, edge_width=0.5):
  fig, ax = ox.plot_graph(
    G,
    node_color=node_color,
    edge_color=edge_color,
    node_size=node_size,
    edge_linewidth=edge_width,
    bgcolor='white',
    show=True,
    close=True
  )

if __name__ == '__main__':
  city = "João Monlevade, Brazil"
  G = ox.graph_from_place(city, network_type='walk')
  G = nx.convert_node_labels_to_integers(G)

  print(f"Número de nós: {len(G.nodes())}")
  print(f"Número de arestas: {len(G.edges())}")

  view_graph(G)