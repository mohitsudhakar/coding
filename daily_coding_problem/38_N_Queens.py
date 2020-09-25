"""
This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N, returns the number of possible
arrangements of the board where N queens can be placed on the board without threatening
each other, i.e. no two queens share the same row, column, or diagonal.
"""

def is_valid(x,y):
    for j in range(y):
        if board[x][j] == 'Q':
            return False
    for i,j in zip(range(x,-1,-1), range(y,-1,-1)):
        if board[i][j] == 'Q':
            return False
    for i,j in zip(range(x,N), range(y,-1,-1)):
        if board[i][j] == 'Q':
            return False
    return True

count = 0
def nqueens(col):
    global count
    if col >= N:
        count += 1
        # print()
        # for b in board:
        #     print(b)
        return True
    poss = False
    for i in range(N):
        if is_valid(i, col):
            board[i][col] = 'Q'
            if nqueens(col+1):
                poss = True
            board[i][col] = '_'
    return poss

if __name__ == '__main__':
    N = 8
    board = [['_']*N for _ in range(N)]
    nqueens(0)
    print(count)