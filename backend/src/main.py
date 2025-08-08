from flask import Flask, request, jsonify
from flask_cors import CORS
from graph_generator import download_city_graph, graph_to_adj_list, filter_graph_by_distance
from greedy_algorithm import greedy_dominating_set_algorithm
from graph_viewer import view_graph

app = Flask(__name__)
CORS(app)


@app.route("/generate-graph", methods=["POST"])
def generate_graph():
  data = request.get_json()
  city = data.get("city")
  dist_max = float(data.get("dist_max", 50))

  # Baixar e filtrar grafo
  G_complete = download_city_graph(city)
  G_filtered = filter_graph_by_distance(G_complete, dist_max)

  # Rodar algoritmo guloso
  adj_list = graph_to_adj_list(G_filtered)
  dominating_set = greedy_dominating_set_algorithm(adj_list)

  # Extrair coordenadas dos nós dominates
  coordinates = []
  for node_id in dominating_set:
    if "x" in G_complete.nodes[node_id] and "y" in G_complete.nodes[node_id]:
      coordinates.append({
        "lat": G_complete.nodes[node_id]["y"],
        "lng": G_complete.nodes[node_id]["x"]      
      })

  return jsonify({
    "city": city,
    "distance": dist_max,
    "dominates": coordinates,
    "total_nodes": len(G_complete.nodes),
    "total_dominates": len(dominating_set)
  })

if __name__ == "__main__":
  app.run(debug=True)