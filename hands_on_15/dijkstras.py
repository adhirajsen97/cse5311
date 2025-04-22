def dijkstra(graph, start):
    import heapq
    
    # Initialize distances dictionary
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # Initialize priority queue and visited set
    priority_queue = [(0, start)]
    visited = set()
    
    while priority_queue:
        # Get the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # If we've already processed this vertex, continue
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        # If current distance is greater than the known distance, skip
        if current_distance > distances[current_vertex]:
            continue
        
        # Check all neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            if neighbor in visited:
                continue
                
            # Calculate new distance
            new_distance = current_distance + weight
            
            # If we found a shorter path, update the distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))
    
    return distances


if __name__ == "__main__":
    # Example graph represented as adjacency list
    graph = {
        'A': {'B': 7, 'C': 9, 'F': 14},
        'B': {'A': 7, 'C': 10, 'D': 15},
        'C': {'A': 9, 'B': 10, 'D': 11, 'F': 2},
        'D': {'B': 15, 'C': 11, 'E': 6},
        'E': {'D': 6, 'F': 9},
        'F': {'A': 14, 'C': 2, 'E': 9}
    }
    
    start_node = 'A'
    distances = dijkstra(graph, start_node)
    
    print(f"Shortest distances from node {start_node}:")
    for vertex, distance in sorted(distances.items()):
        print(f"{vertex}: {distance}")