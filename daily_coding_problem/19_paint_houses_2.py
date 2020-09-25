"""
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors.
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build
the nth house with kth color, return the minimum cost which achieves this goal.
"""

def fn(matrix):
    if not matrix or not matrix[0]:
        return

    min_cost = float('inf')
    prev_color = 0
    for c in range(K):
        if matrix[0][c] < min_cost:
            min_cost = matrix[0][c]
            prev_color = c

    for i in range(1, N):
        min_k, sec_min_k = float('inf'), float('inf')
        min_idx, sec_min_idx = 0, 0
        # 2 conditions
        # keep track of 1st min and 2nd min for each color (j)
        # if prev color is same as 1st min, take 2nd min
        for j in range(K):
            if matrix[i][j] < min_k:
                sec_min_k = min_k
                sec_min_idx = min_idx
                min_k = matrix[i][j]
                min_idx = j
            elif matrix[i][j] < sec_min_k:
                sec_min_k = matrix[i][j]
                sec_min_idx = j
        if prev_color == min_idx:
            curr_color = sec_min_idx
        else:
            curr_color = min_idx
        prev_color = curr_color
        min_cost += matrix[i][curr_color]

    return min_cost

if __name__ == '__main__':
    K = 3
    N = 5
    matrix = [
        [5,5,1],
        [4,7,2],
        [5,1,3],
        [1,9,4],
        [2,10,5]
    ]
    res = fn(matrix)
    print(res)