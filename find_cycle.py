def bfs(start, graph):
    s = set()
    vis = [False] * len(graph)
    q = [start]
    while q:
        node = q.pop(0)
        vis[node] = True
        if node in s:
            return True
        else:
            s.add(node)
        for neighbor in graph[node]:
            if not vis[neighbor]:
                q.append(neighbor)
    return False

graph = [[1, 2], [2, 0], [1, 0]]

print(bfs(0, graph))
