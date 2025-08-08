import osmnx as ox
import networkx as nx

def download_city_graph(city_name):
  G = ox.graph_from_place(city_name, network_type='walk')
  G = ox.utils_graph.get_undirected(G)
  return G

def filter_graph_by_distance(G, dist_max=50):
  # Cria uma cópia do grafo para aplicar o filtro
  G_filtered = G.copy()

  # Remove nós que estão muito distantes do ponto de referência
  remove_edge = [(u, v, k) for (u, v, k, data) in G_filtered.edges(keys=True, data=True) 
                if data.get('length', 0) > dist_max]
  
  G_filtered.remove_edges_from(remove_edge)
  G_filtered.remove_nodes_from(list(nx.isolates(G_filtered)))

  return G_filtered

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



