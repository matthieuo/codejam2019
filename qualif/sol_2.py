import collections
import numpy as np


def create_board(size, exist_path):
    board = np.zeros((size, size))
    cur_pos = (0, 0)

    board[0, 0] = 1
    while exist_path:
        e = exist_path.pop(0)
        if e == 'E':
            cur_pos = (cur_pos[0] + 1, cur_pos[1])
        else:
            cur_pos = (cur_pos[0], cur_pos[1] + 1)
        board[cur_pos] = 1
    return board


def find_path(dim, ext_board, cur_pos):
    cur_node = (cur_pos, '')
    visited = set()
    to_visit = collections.deque()
    to_visit.append(cur_node)

    while True:
        cur_pos, cur_path = to_visit.pop()

        if cur_pos[0] == dim - 1 and cur_pos[1] == dim - 1:
            return cur_path

        if cur_pos in visited:
            continue

        if cur_pos[0] + 1 < dim and not (ext_board[cur_pos] == 1 and ext_board[(cur_pos[0] + 1, cur_pos[1])] == 1):
            to_visit.append(((cur_pos[0] + 1, cur_pos[1]), cur_path + 'E'))

        if cur_pos[1] + 1 < dim and not (ext_board[cur_pos] == 1 and ext_board[(cur_pos[0], cur_pos[1] + 1)] == 1):
            to_visit.append(((cur_pos[0], cur_pos[1] + 1), cur_path + 'S'))

        visited.add(cur_pos)


nt = int(input())
inputs = []
outputs = []
for t in range(nt):
    dim = int(input())
    paths = input()
    board = create_board(dim, list(paths))
    inputs.append((dim, board))

outputs = [find_path(d, b, (0, 0)) for d, b in inputs]

for i, p in enumerate(outputs):
    print("Case #" + str(i+1) + ': ' + p)
