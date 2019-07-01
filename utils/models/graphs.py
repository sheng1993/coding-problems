class Graph():
    V = set
    E = set

    def __init__(self):
        self.V = set()
        self.E = set()

    def add_vertex(self, v: str):
        if v not in self.V:
            self.V.add(v)

    def add_vertex(self, v: list):
        self.V.update(v)

    def add_edge(self, v1: str, v2: str):
        if (v1, v2) not in self.E:
            self.E.add((v1, v2))