class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

def floyd_warshall_algorithm(graph):
 
    # Initialize distance matrix
    distance = {}
    for u in graph:
        distance[u] = {}
        for v in graph:
            if u == v:
                distance[u][v] = 0
            else:
                # Get edge weight if it exists, otherwise infinity
                distance[u][v] = graph.get(u, {}).get(v, float('infinity'))
    
    # Floyd-Warshall algorithm
    for k in graph:
        for i in graph:
            for j in graph:
                # If using k as intermediate vertex gives shorter path
                if distance[i][k] != float('infinity') and distance[k][j] != float('infinity'):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    return distance

def print_graph(graph):
    print("Graph:")
    for u in graph:
        for v in graph[u]:
            print(f"{u} -> {v} : {graph[u][v]}")
    print()

def print_shortest_paths(all_pairs_shortest_paths):
    print("Shortest Paths:")
    for u in all_pairs_shortest_paths:
        for v in all_pairs_shortest_paths[u]:
            if all_pairs_shortest_paths[u][v] == float('infinity'):
                print(f"Shortest path from {u} to {v}: INF")
            else:
                print(f"Shortest path from {u} to {v}: {all_pairs_shortest_paths[u][v]}")
    print()

def construct_graph_from_shortest_paths(graph, all_pairs_shortest_paths):
    shortest_path_edges = []
    for u in graph:
        for v in graph[u]:
            shortest_path_edges.append(Edge(u, v, all_pairs_shortest_paths[u][v]))
    return shortest_path_edges

def print_shortest_path_graph(shortest_path_edges):
    print("Shortest Path Graph:")
    for edge in shortest_path_edges:
        print(f"{edge.start} -> {edge.end} : {edge.weight}")
    print()


if __name__ == "__main__":
    graph = {
        '1': {'2': 3, '3': 8, '5': -4},
        '2': {'5': 7, '4': 1},
        '3': {'2': 4},
        '4': {'3': -5, '1': 2},
        '5': {'4': 6}
    }
    
    print_graph(graph)
    
    all_pairs_shortest_paths = floyd_warshall_algorithm(graph)
    print_shortest_paths(all_pairs_shortest_paths)
    
    shortest_path_edges = construct_graph_from_shortest_paths(graph, all_pairs_shortest_paths)
    print_shortest_path_graph(shortest_path_edges)