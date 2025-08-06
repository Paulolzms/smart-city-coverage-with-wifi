import os
import osmnx as ox
import matplotlib.pyplot as plt

def view_graph(G, dominating_set, city_name):
  node_colors = ['red' if node in dominating_set else 'blue' for node in G.nodes]
  
  fig, ax = ox.plot_graph(
    G,
    node_color=node_colors,
    edge_color='lightgray',
    node_size=10,
    edge_linewidth=0.5,
    bgcolor='white',
    show=True,
    close=True
  )
  output_file = os.path.join("out", f"graph_{city_name.lower().replace(',', '').replace(' ', '_')}.png")
  fig.savefig(output_file, dpi=300, bbox_inches='tight')