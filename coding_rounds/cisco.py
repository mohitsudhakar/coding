# Sample code to read input and write output:

'''
NAME = raw_input()            # Read input from STDIN
print 'Hello %s' % NAME       # Write output to STDOUT
'''

# Warning: Printing unwanted or ill-formatted
# data to output will cause the test cases to fail

# Write your code here

def exist(board, word):
    first = word[0]
    m = len(board)
    n = len(board[0])
    starts = []
    for i in range(m):
        for j in range(n):
            if board[i][j] == first:
                starts.append((i,j))

    if not starts:
        return False

    def dfs(s, idx):
        visited[s[0]][s[1]] = True
        idx += 1

        if idx == len(word):
            return True

        for dirn in dirns:
            new_s = (s[0]+dirn[0], s[1]+dirn[1])
            if 0 <= new_s[0] < m and 0 <= new_s[1] < n:
                if not visited[new_s[0]][new_s[1]] and board[new_s[0]][new_s[1]] == word[idx] and dfs(new_s, idx):
                    return True

        visited[s[0]][s[1]] = False
        return False

    dirns = [(0,1), (1,0), (-1,0), (0,-1)]
    for start in starts:
        visited = [[False]*n for _ in range(m)]
        if dfs(start, 0):
            return True

    return False


def checkWordsInGrid(board, words):

    return ["Yes" if exist(board, word) else "No" for word in words]


if __name__ == '__main__':

    N = int(raw_input())
    board = []
    for i in range(N):
        row = raw_input()
        board.append(row.split(' '))

    M = int(raw_input())
    strings = raw_input().split(' ')

    ans = checkWordsInGrid(board, strings)
    print(' '.join(ans))

"""
3
M O M
S O N
R A T
4
MNT RAH MSR OOB
"""

"""
4
M O M A
E X P O
T E M P
T O Y S
4
OPS MET MXMS APS
"""