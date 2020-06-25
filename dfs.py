def dfs(n, edges):
    """Given a list of all edges of a graph with vertices 1 to n,
    will explore every vertex, depth first, without recursion."""
    edges_by_vertex = dict([(i, []) for i in range(n)])
    for edge in edges:
        edges_by_vertex[edge[0]].append(edge[1])
        edges_by_vertex[edge[1]].append(edge[0])

    undiscovered = set(range(n))

    while undiscovered:
        first_vertex = undiscovered.pop()
        undiscovered.add(first_vertex)
        stack = [first_vertex]              # the stack is a list of vertices to explore
        while stack:
            v = stack.pop()
            if v in undiscovered:
                print('Just discovered vertex {}.'.format(v))
                undiscovered.remove(v)
                for w in edges_by_vertex[v]:
                    stack.append(w)


dfs(8, [[0, 1], [0, 2], [0, 4], [1, 3], [1, 5], [2, 6], [4, 5], ])
