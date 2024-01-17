from collections import deque


def shortestPathBinaryMatrix(grid):
    shortest_path_len = -1
    row = len(grid)
    col = len(grid[0])

    if grid[0][0] != 0 or grid[row-1][col-1] != 0:
        return shortest_path_len

    visited = [[False] * col for _ in range(row)]
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1),
             (1, 1), (1, -1), (-1, 1), (-1, -1)]
    queue = deque()  # path의 길이도 추가적으로 넣어줌
    queue.append((0, 0, 1))

    visited[0][0] = True

    while queue:
        cur_r, cur_c, cur_len = queue.popleft()
        # 목적지에 도착했을 때 cur_len을 shortest_path_len에 저장하면 된다.
        if cur_r == row-1 and cur_c == cur_c - 1:
            shortest_path_len = cur_len
            break

        # 연결되어 있는 vertex 확인하기
        for dr, dc in delta:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if next_r >= 0 and next_r < row and next_c >= 0 and next_c < col:
                if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                    queue.append((next_r, next_c, cur_len + 1))
                    visited[next_r, next_c] = True

    return shortest_path_len
