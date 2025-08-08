def greedy_dominating_set_algorithm(graph):
  dominated = set()
  D = set()

  while len(dominated) < len(graph):
    best_node = None
    max_coverage = -1

    for node in graph:
      if node in dominated:
        continue

      coverage = 1 if node not in dominated else 0
      for neighbor in graph[node]:
        if neighbor not in dominated:
          coverage += 1

      if coverage > max_coverage:
        best_node = node
        max_coverage = coverage

    D.add(best_node)
    dominated.add(best_node)
    for neighbor in graph[best_node]:
      dominated.add(neighbor)

  return D