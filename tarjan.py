class Graph:
    def __init__(self, nodes):
        self.graph = [[] for _ in range(nodes)]
        self.nodes = nodes
        self.scc = 0
        self.sccs = []
        self.id = 1
    
    def add_edge(self, *args):
        self.graph[args[0]].append(args[1])
    
    def tarjansSCC(self):
        ids = [-1] * self.nodes
        low = [0] * self.nodes
        on_stack = [False] * self.nodes
        stack = []

        def dfs(at):
            on_stack[at] = True
            stack.append(at)
            ids[at] = low[at] = self.id
            self.id += 1
            
            for to in self.graph[at]:
                if ids[to] == -1:
                    dfs(to)
                if on_stack[to]:
                    low[at] = min(low[at], low[to])
                    
            if low[at] == ids[at]:
                scc = []
                while stack:
                    i = stack.pop()
                    on_stack[i] = False
                    low[i] = ids[at]
                    scc.append(i)
                    if i == at:
                        break
                self.sccs += [scc]
                self.scc += 1
        
        for i in range(self.nodes):
            if ids[i] == -1:
                dfs(i)
        
        return self.scc, self.sccs

def main():
    graph = Graph(8)
    graph.add_edge(6, 0)
    graph.add_edge(6, 2)
    graph.add_edge(3, 4)
    graph.add_edge(6, 4)
    graph.add_edge(2, 0)
    graph.add_edge(0, 1)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(3, 7)
    graph.add_edge(7, 5)
    graph.add_edge(1, 2)
    graph.add_edge(7, 5)
    graph.add_edge(7, 3)
    graph.add_edge(5, 0)

    g4 = Graph(11)
    g4.add_edge(0, 1)
    g4.add_edge(0, 3)
    g4.add_edge(1, 2)
    g4.add_edge(1, 4)
    g4.add_edge(2, 0)
    g4.add_edge(2, 6)
    g4.add_edge(3, 2)
    g4.add_edge(4, 5)
    g4.add_edge(4, 6)
    g4.add_edge(5, 6)
    g4.add_edge(5, 7)
    g4.add_edge(5, 8)
    g4.add_edge(5, 9)
    g4.add_edge(6, 4)
    g4.add_edge(7, 9)
    g4.add_edge(8, 9)
    g4.add_edge(9, 8)
    
    print("Number of comps.: {}, List of comps: {}".format(*g4.tarjansSCC()))

main()
