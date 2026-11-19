def pathCount(graph, vStart, vEnd, visited=[]):
    if vStart == vEnd:
        return 1
    visited.append(vStart)
    count = 0
    for v in graph[vStart]:
        if not v in visited:
            count += pathCount(graph, v, vEnd, visited)
    visited.pop()
    return count


Graph = [[], [4], [1, 3], [], [2, 3, 5], [3]]
print(pathCount(Graph, 1, 3))
