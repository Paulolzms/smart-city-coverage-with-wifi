import osmnx as ox
import networkx as nx

def download_city_graph(city_name):
  G = ox.graph_from_place(city_name, network_type='walk')
  G = nx.convert_node_labels_to_integers(G)
  return G

def graph_to_adj_list(G):
  return {u: list(G.neighbors(u)) for u in G.nodes}

def save_adj_list_to_file(adj_list, filename):
  with open(filename, 'w') as f:
    for node, neighbors in adj_list.items():
      line = f"{node}: {' '.join(map(str, neighbors))}\n"
      f.write(line)

if __name__ == '__main__':
  city = "João Monlevade, Brazil"
  G = download_city_graph(city)
  adj_list = graph_to_adj_list(G)
  save_adj_list_to_file(adj_list, 'graph_joao_monlevade.txt')
  print("Grafo salvo com sucesso!")



