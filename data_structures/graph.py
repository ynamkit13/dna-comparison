# Custom Graph implementation using an adjacency list
# Used to represent the DNA similarity graph and the MST result


class Graph:
    """
    A weighted undirected graph using adjacency lists.
    Each vertex maps to a list of (neighbor, weight) pairs.
    """

    def __init__(self):
        # Adjacency list: vertex -> list of (neighbor, weight)
        # Using a simple list of (vertex, neighbors) pairs instead of dict
        self.adjacency = []
        # Keep track of vertex names for quick lookup
        self.vertex_list = []

    def add_vertex(self, vertex):
        """Add a new vertex to the graph."""
        if vertex not in self.vertex_list:
            self.vertex_list.append(vertex)
            self.adjacency.append((vertex, []))

    def _find_neighbors(self, vertex):
        """Find the neighbor list for a vertex. Returns None if not found."""
        for v, neighbors in self.adjacency:
            if v == vertex:
                return neighbors
        return None

    def add_edge(self, vertex1, vertex2, weight):
        """Add a weighted undirected edge between two vertices."""
        # Make sure both vertices exist
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        # Add edge in both directions (undirected graph)
        neighbors1 = self._find_neighbors(vertex1)
        neighbors2 = self._find_neighbors(vertex2)

        neighbors1.append((vertex2, weight))
        neighbors2.append((vertex1, weight))

    def get_neighbors(self, vertex):
        """Get all neighbors and edge weights for a vertex."""
        neighbors = self._find_neighbors(vertex)
        if neighbors is None:
            return []
        return neighbors

    def get_vertices(self):
        """Return a list of all vertices in the graph."""
        return list(self.vertex_list)

    def get_edges(self):
        """Return a list of all edges as (vertex1, vertex2, weight) tuples."""
        edges = []
        seen = []  # Track edges we've already added

        for vertex, neighbors in self.adjacency:
            for neighbor, weight in neighbors:
                # Avoid duplicates (since graph is undirected)
                edge_key = tuple(sorted([vertex, neighbor]))
                if edge_key not in seen:
                    edges.append((vertex, neighbor, weight))
                    seen.append(edge_key)

        return edges

    def __len__(self):
        return len(self.vertex_list)
