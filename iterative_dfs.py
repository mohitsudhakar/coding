

def dfs(graph, start, V):
    vis = [False]*V
    stack = [start]
    vis[start] = True
    while stack:
        node = stack.pop()
        print(node)
        for nei in graph[node]:
            if not vis[node]:
                vis[nei] = True
                stack.append(nei)

