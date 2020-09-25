class Solution:
    def solve(self, matrix):
        # Write your code here

        def dfs(u, v, u0, v0, nodes):
            vis[u][v] = True
            nodes.append((u-u0, v-v0))
            for d in dirs:
                x,y = u+d[0], v+d[1]
                if 0 <= x < m and 0 <= y < n and matrix[x][y] == 1 and not vis[x][y]:
                    dfs(x,y,u0,v0, nodes)

        m,n = len(matrix), len(matrix[0])
        vis = [[False for _ in range(n)] for _ in range(m)]
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        coord = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1 and not vis[i][j]:
                    nodes = []
                    dfs(i, j, i, j, nodes)
                    coord.add(tuple(nodes))

        return len(coord)