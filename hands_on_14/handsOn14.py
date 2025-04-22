"""
Enhanced implementations of graph algorithms in Python:
1. Depth-First Search (DFS)
2. Kruskal's Minimum Spanning Tree Algorithm
3. Topological Sort

Each algorithm is implemented as a separate class with clear documentation.
"""

class Graph:
    """A directed graph implementation with DFS traversal capability."""
    
    def __init__(self):
        """Initialize an empty graph."""
        self.graph = {}
    
    def add_edge(self, u, v):
        """Add a directed edge from vertex u to vertex v."""
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
    
    def dfs(self, start_vertex):
        """
        Perform DFS traversal starting from the given vertex.
        
        Args:
            start_vertex: The vertex to start DFS from
            
        Returns:
            A list of vertices in DFS traversal order
        """
        # Find the maximum vertex to properly size the visited array
        all_vertices = set(self.graph.keys())
        for neighbors in self.graph.values():
            all_vertices.update(neighbors)
        
        max_vertex = max(all_vertices) if all_vertices else start_vertex
        visited = [False] * (max_vertex + 1)
        result = []
        
        def dfs_util(v):
            visited[v] = True
            result.append(v)
            
            if v in self.graph:
                for neighbor in self.graph[v]:
                    if not visited[neighbor]:
                        dfs_util(neighbor)
        
        dfs_util(start_vertex)
        return result


class KruskalMST:
    """Implementation of Kruskal's Minimum Spanning Tree algorithm."""
    
    class Edge:
        """Edge class with source, destination, and weight."""
        def __init__(self, src, dest, weight):
            self.src = src
            self.dest = dest
            self.weight = weight
        
        def __lt__(self, other):
            return self.weight < other.weight
    
    def __init__(self):
        """Initialize an empty graph for Kruskal's algorithm."""
        self.vertices = set()
        self.edges = []
    
    def add_edge(self, src, dest, weight):
        """Add an edge to the graph."""
        self.edges.append(self.Edge(src, dest, weight))
        self.vertices.add(src)
        self.vertices.add(dest)
    
    def find(self, parent, i):
        """Find the set of an element i with path compression."""
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]
    
    def union(self, parent, rank, x, y):
        """Union of two sets by rank."""
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)
        
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1
    
    def find_mst(self):
        """
        Find the Minimum Spanning Tree using Kruskal's algorithm.
        
        Returns:
            A list of Edge objects that form the MST
        """
        result = []  # Stores the MST edges
        
        # Create vertex-to-index mapping for disjoint set operations
        vertex_to_index = {v: i for i, v in enumerate(self.vertices)}
        
        self.edges.sort()  # Sort edges by weight
        
        parent = list(range(len(self.vertices)))
        rank = [0] * len(self.vertices)
        
        for edge in self.edges:
            # Map actual vertices to indices
            src_idx = vertex_to_index[edge.src]
            dest_idx = vertex_to_index[edge.dest]
            
            x = self.find(parent, src_idx)
            y = self.find(parent, dest_idx)
            
            if x != y:
                result.append(edge)
                self.union(parent, rank, x, y)
        
        return result


class TopologicalSort:
    """Implementation of topological sorting algorithm."""
    
    def __init__(self):
        """Initialize an empty directed acyclic graph."""
        self.graph = {}
    
    def add_edge(self, u, v):
        """Add a directed edge from vertex u to vertex v."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
    
    def topological_sort(self):
        """
        Perform topological sort on the graph.
        
        Returns:
            A list of vertices in topological order
        """
        # Initialize visited and stack
        visited = {node: False for node in self.graph}
        stack = []
        
        # Helper DFS function
        def dfs_util(node):
            visited[node] = True
            
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    dfs_util(neighbor)
            
            stack.append(node)
        
        # Call DFS for all unvisited vertices
        for node in self.graph:
            if not visited[node]:
                dfs_util(node)
        
        # Return the reversed stack
        return stack[::-1]


def test_all_algorithms():
    """Test all three graph algorithms with example inputs."""
    
    print("=== Testing Depth-First Search ===")
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    result = g.dfs(2)
    print(f"DFS traversal starting from vertex 2: {result}")
    assert result == [2, 0, 1, 3], "DFS traversal incorrect"
    
    print("\n=== Testing Kruskal's MST Algorithm ===")
    kruskal = KruskalMST()
    kruskal.add_edge(0, 1, 10)
    kruskal.add_edge(0, 2, 6)
    kruskal.add_edge(0, 3, 5)
    kruskal.add_edge(1, 3, 15)
    kruskal.add_edge(2, 3, 4)
    
    mst = kruskal.find_mst()
    print("Edges in the Minimum Spanning Tree:")
    total_weight = 0
    for edge in mst:
        print(f"{edge.src} -- {edge.dest} == {edge.weight}")
        total_weight += edge.weight
    print(f"Total MST weight: {total_weight}")
    assert total_weight == 19, "MST weight incorrect"
    
    print("\n=== Testing Topological Sort ===")
    topo = TopologicalSort()
    topo.add_edge(3, 4)
    topo.add_edge(3, 1)
    topo.add_edge(1, 2)
    topo.add_edge(2, 5)
    topo.add_edge(0, 5)
    topo.add_edge(0, 4)
    
    result = topo.topological_sort()
    print(f"Topological Sort result: {result}")
    # Check if the result is a valid topological ordering
    visited = set()
    valid = True
    for node in result:
        visited.add(node)
        for neighbor in topo.graph.get(node, []):
            if neighbor in visited:
                valid = False
                break
    assert valid, "Topological sort result is not valid"


if __name__ == "__main__":
    test_all_algorithms()