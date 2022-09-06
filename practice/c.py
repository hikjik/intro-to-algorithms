from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    neighbours: List[int] = []
    for k, l in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        if 0 <= k+row < len(matrix) and 0 <= l+col < len(matrix[0]):
            neighbours.append(matrix[k+row][l+col])
    neighbours.sort()
    return neighbours


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
