
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def parseArtifacts(artifacts):
    """
    Returns a list of (fromX, fromY, toX, toY) where from and to are positions in grid
    """
    artifactList = artifacts.split(',')
    resList = []
    for artifact in artifactList:
        fromCell, toCell = artifact.split(' ')

        fromX, fromY = fromCell[:-1], fromCell[-1]
        fromX = int(fromX) - 1
        fromY = ord(fromY) - ord('A')

        toX, toY = toCell[:-1], toCell[-1]
        toX = int(toX) - 1
        toY = ord(toY) - ord('A')

        resList.append((fromX, fromY, toX, toY))
    return resList

def parseSearched(searched):
    positions = searched.split(' ')
    resList = []
    for position in positions:
        x,y = position[:-1], position[-1]
        x = int(x) - 1
        y = ord(y) - ord('A')
        resList.append((x,y))
    return resList

def dfs(n, grid, x, y):

    grid[x][y] = '0'

    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    for dirn in dirs:
        i,j = dirn

        if 0 <= x+i < n and 0 <= y+j < n:
            if 'X' in grid[x+i][y+j]:
                dfs(n, grid, x+i, y+j)


def solution(N, artifacts, searched):

    # initialize grid of NxN
    grid = [['0']*N for _ in range(N)]

    artifactList = parseArtifacts(artifacts)
    for i in range(len(artifactList)):
        fromX, fromY, toX, toY = artifactList[i]
        for r in range(fromX, toX+1):
            for c in range(fromY, toY+1):
                grid[r][c] = str(i+1)

    numArtifacts = len(artifactList)

    # for each searched, put a new uniq in that pos, 1X,2X,3X etc
    searchList = parseSearched(searched)
    for x,y in searchList:
        if grid[x][y] != '0':
            grid[x][y] = grid[x][y] + 'X'

    max_count = 0
    uniqueFound = set()
    # do dfs on each cell containing X and count num of dfses say max_count
    for i in range(N):
        for j in range(N):
            if 'X' in grid[i][j]:
                max_count += 1
                dfs(N, grid, i, j)
    
    # then for each non zero unique cell, subtract from max_count
    remainingUniqueArtifacts = set()
    for i in range(N):
        for j in range(N):
            if grid[i][j] != '0':
                remainingUniqueArtifacts.add(grid[i][j])
    rem = len(remainingUniqueArtifacts)

    full = numArtifacts - rem

    return (full, max_count - full)


if __name__ == '__main__':

    N = 4
    artifacts = "1B 2C,2D 4D"
    searched = "2B2D 3D 4D 4A"
    assert (1,0) == solution(N, artifacts, searched)

    N = 12
    artifacts = "1A 2A,12A 12A"
    searched = "12A"
    assert (1,0) == solution(N, artifacts, searched)

    N = 3
    artifacts = "1A 1B,2C 2C"
    searched = "1B"
    assert (0,1) == solution(N, artifacts, searched)


