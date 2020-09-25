# # Count number of Knight's Tours in NxN chessboard
#
# # class Position:
# #     def __init__(self, x, y):
# #         self.x = x
# #         self.y = y
#
#
# def getMoves(start, vis, n):
#     valid = []
#     poss_x = [2, 2, 1, 1, -1, -1, -2, -2]
#     poss_y = [1, -1, 2, -2, 2, -2, 1, -1]
#     for i in range(8):
#         x, y = start[0] + poss_x[i], start[1] + poss_y[i]
#         if 0 <= x < n and 0 <= y < n: # and (x,y) not in vis:
#             valid.append((x,y))
#     return valid
#
# def runKnightTours(start, vis, n):
#     print('runKnightTours', start, n, vis)
#     if len(vis) == n*n:
#         return 1
#     count = 0
#     moves = getMoves(start, vis, n)
#     for move in moves:
#         if move not in vis:
#             vis.add(move)
#             count += runKnightTours(move, vis, n)
#             vis.remove(move)
#
#     return count
#
# def countKnightTours(n):
#     print('countKnightTours', n)
#     count = 0
#     for i in range(n):
#         for j in range(n):
#             start = (i,j)
#             vis = {start}
#             count += runKnightTours(start, vis, n)
#
#     return count
#
# if __name__ == '__main__':
#     N = 5
#     assert 1 == countKnightTours(1)
#     assert 0 == countKnightTours(2)
#     assert 0 == countKnightTours(3)
#     assert 0 == countKnightTours(4)
#     assert 1728 == countKnightTours(5)
#

import random


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "[{},{}]".format(self.x, self.y)


def get_potential_knight_moves(start, size, visited):
    moves = list()
    moves.append(Position(start.x + 1, start.y + 2))
    moves.append(Position(start.x + 1, start.y - 2))
    moves.append(Position(start.x - 1, start.y + 2))
    moves.append(Position(start.x - 1, start.y - 2))
    moves.append(Position(start.x + 2, start.y + 1))
    moves.append(Position(start.x + 2, start.y - 1))
    moves.append(Position(start.x - 2, start.y + 1))
    moves.append(Position(start.x - 2, start.y - 1))

    valid_moves = [pos for pos in moves if
                   pos.x >= 0 and pos.x < size and
                   pos.y >= 0 and pos.y < size and
                   pos not in visited]

    return valid_moves


def run_knights_tour(start, size, visited):
    # global ct
    # ct += 1
    # print('run tour', start, size, 'len', len(visited), ct)

    if len(visited) == size * size:
        return 1

    moves = get_potential_knight_moves(start, size, visited)

    count = 0
    for move in moves:
        tmp_visted = visited.copy()
        tmp_visted.add(move)
        count += run_knights_tour(move, size, tmp_visted)

    # if count > 0:
    #     print('count', count)

    return count


def count_knights_tours(size):
    # print('count tour', size)
    count = 0
    vis = set()
    for i in range(size):
        for j in range(size):
            start = Position(i, j)
            vis.add(start)
            count += run_knights_tour(start, size, vis.copy())
            print(start, count)

    return count


if __name__ == '__main__':
    ct = 0
    # assert count_knights_tours(1) == 1
    # assert count_knights_tours(2) == 0
    # assert count_knights_tours(3) == 0
    # assert count_knights_tours(4) == 0
    assert count_knights_tours(5) == 1728