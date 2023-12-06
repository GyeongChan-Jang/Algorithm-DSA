from collections import deque

grid = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]


def numIslands(grid):
    number_of_islands = 0
    m = len(grid)
