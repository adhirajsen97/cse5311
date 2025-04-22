class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

class Graph:
    def __init__(self, num_vertices, num_edges):
        self.num_vertices = num_vertices
        self.num_edges = num_edges
        self.edges = []

def create_graph(num_vertices, num_edges):
    return Graph(num_vertices, num_edges)

def initialize_distances(num_vertices, src):
    distances = [float('infinity')] * num_vertices
    distances[src] = 0
    return distances

def relax_edges(graph, distances):
    for _ in range(graph.num_vertices - 1):
        for edge in graph.edges:
            u = edge.source
            v = edge.destination
            weight = edge.weight
            if distances[u] != float('infinity') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

def check_negative_cycles(graph, distances):
    for edge in graph.edges:
        u = edge.source
        v = edge.destination
        weight = edge.weight
        if distances[u] != float('infinity') and distances[u] + weight < distances[v]:
            print("Graph contains negative-weight cycle")
            return True
    return False

def print_distances(distances):
    print("Vertex   Distance from Source")
    for i, distance in enumerate(distances):
        if distance == float('infinity'):
            print(f"{i} -> INF")
        else:
            print(f"{i} -> {distance}")

def bellman_ford(graph, src):
    distances = initialize_distances(graph.num_vertices, src)
    relax_edges(graph, distances)
    if check_negative_cycles(graph, distances):
        return None
    
    print_distances(distances)
    
    return distances


if __name__ == "__main__":
    # Predefined example
    num_vertices = 5
    num_edges = 8
    
    graph = create_graph(num_vertices, num_edges)
    
    # Adding edges (example graph with a negative edge but no negative cycle)
    graph.edges.append(Edge(0, 1, 6))
    graph.edges.append(Edge(0, 2, 7))
    graph.edges.append(Edge(1, 2, 8))
    graph.edges.append(Edge(1, 3, -4))
    graph.edges.append(Edge(1, 4, 5))
    graph.edges.append(Edge(2, 3, 9))
    graph.edges.append(Edge(2, 4, -3))
    graph.edges.append(Edge(3, 4, 7))
    
    source_vertex = 0
    
    print("Using predefined graph with vertices:", num_vertices)
    print("Number of edges:", num_edges)
    print("Source vertex:", source_vertex)

    # Run Bellman-Ford algorithm
    bellman_ford(graph, source_vertex)