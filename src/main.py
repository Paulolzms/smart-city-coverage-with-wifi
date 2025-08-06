from graph_generator import download_city_graph, graph_to_adj_list, save_adj_list_to_file
from greedy_algorithm import greedy_dominating_set_algorithm
from graph_viewer import view_graph

city = "João Monlevade, Brazil"
G = download_city_graph(city)
adj_list = graph_to_adj_list(G)
dominating_set = greedy_dominating_set_algorithm(adj_list)
view_graph(G, dominating_set, city)

print(f"Tamanho do conjunto dominante: {len(dominating_set)}")
#print(f"Conjunto dominante: {sorted(dominating_set)}")