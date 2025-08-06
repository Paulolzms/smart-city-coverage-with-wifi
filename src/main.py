from graph_generator import download_city_graph, graph_to_adj_list, filter_graph_by_distance
from greedy_algorithm import greedy_dominating_set_algorithm
from graph_viewer import view_graph

city = "João Monlevade, Brazil"
dist_max = 50

G_complete = download_city_graph(city)

G_filtered = filter_graph_by_distance(G_complete, dist_max)
adj_list = graph_to_adj_list(G_filtered)
dominating_set = greedy_dominating_set_algorithm(adj_list)
view_graph(G_complete, dominating_set, city)

print(f"Tamanho do conjunto dominante: {len(dominating_set)}")
#print(f"Conjunto dominante: {sorted(dominating_set)}")