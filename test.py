from utils.models.graphs import Graph

g = Graph()
g.add_vertex(['a', 'b', 'c'])

V = map(lambda x: x.upper(), g.V)
print(list(V))