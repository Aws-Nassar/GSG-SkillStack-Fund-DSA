import math

class Edge:
    def __init__(self, target, weight):
        self.target = target
        self.weight = weight

class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = []

    def add_edge(self, target_vertex, weight):
        self.edges.append(Edge(target_vertex, weight))

    def remove_edge(self, target_vertex):
        self.edges = [e for e in self.edges if e.target != target_vertex]

class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, label):
        if not any(v.label == label for v in self.vertices):
            self.vertices.append(Vertex(label))

    def find_vertex(self, label):
        for v in self.vertices:
            if v.label == label:
                return v
        return None

    def add_edge(self, from_label, to_label, weight):
        from_vertex = self.find_vertex(from_label)
        to_vertex = self.find_vertex(to_label)
        if from_vertex and to_vertex:
            from_vertex.add_edge(to_vertex, weight)

    def remove_edge(self, from_label, to_label):
        from_vertex = self.find_vertex(from_label)
        to_vertex = self.find_vertex(to_label)
        if from_vertex and to_vertex:
            from_vertex.remove_edge(to_vertex)

    def remove_vertex(self, label):
        target_vertex = self.find_vertex(label)
        if target_vertex:
            self.vertices = [v for v in self.vertices if v != target_vertex]
            for v in self.vertices:
                v.remove_edge(target_vertex)

    # BFS-based reachable locations
    def reachable_locations(self, start_label):
        start_vertex = self.find_vertex(start_label)
        if not start_vertex:
            return []
        
        visited = set()
        queue = [start_vertex]
        reachable = []
        
        while queue:
            vertex = queue.pop(0)
            if vertex.label not in visited:
                reachable.append(vertex.label)
                visited.add(vertex.label)
                for edge in vertex.edges:
                    if edge.target.label not in visited:
                        queue.append(edge.target)
        return reachable

    # Dijkstra's Shortest Path                  // With heap it will be better for complexity 
    def shortest_path(self, start_label, end_label):

        # Initialize distances and previous nodes
        dist = {v.label: math.inf for v in self.vertices}
        prev = {v.label: None for v in self.vertices}
        dist[start_label] = 0
        
        # Track unvisited nodes
        unvisited = set(v.label for v in self.vertices)
        
        while unvisited:
            # Find unvisited node with smallest distance
            min_dist = math.inf
            current_label = None
            for node in unvisited:
                if dist[node] < min_dist:
                    min_dist = dist[node]
                    current_label = node
            
            # If no reachable nodes left, break
            if current_label is None:
                break
                
            unvisited.remove(current_label)
            current_vertex = self.find_vertex(current_label)
            
            # Explore neighbors
            for edge in current_vertex.edges:
                neighbor = edge.target
                if neighbor.label not in unvisited:
                    continue
                    
                new_dist = dist[current_label] + edge.weight
                if new_dist < dist[neighbor.label]:
                    dist[neighbor.label] = new_dist
                    prev[neighbor.label] = current_label
        
        # Reconstruct path if exists
        path = []
        current = end_label
        while current is not None:
            path.append(current)
            current = prev[current]
        path.reverse()
        
        return (path, dist[end_label]) if path and path[0] == start_label else ([], math.inf)



# Create city graph
city = Graph()

# Add locations (vertices)
locations = [
    "Hospital", 
    "School", 
    "Mall", 
    "Park", 
    "Stadium", 
    "Airport"
]

for location in locations:
    city.add_vertex(location)

# Add roads (edges)
roads = [
    ("Hospital", "School", 5),
    ("School", "Mall", 3),
    ("Mall", "Park", 7),
    ("Park", "Stadium", 2),
    ("Stadium", "Airport", 15),
    ("Airport", "Hospital", 20),
    ("Hospital", "Mall", 10),
    ("School", "Park", 8),
    ("Mall", "Airport", 4),
    ("Park", "Hospital", 6)
]

for road in roads:
    city.add_edge(road[0], road[1], road[2])

# Test reachable locations
print("Locations reachable from Hospital:")
print(city.reachable_locations("Hospital"))

# Test shortest path
start = "Hospital"
destination = "Airport"
path, time = city.shortest_path(start, destination)

print(f"\nShortest path from {start} to {destination}:")

if path:
    print(" → ".join(path))
    print(f"Total travel time: {time} minutes")

else:
    print("No path exists")