# def canVisitAllRooms(rooms):
#     # 방문한 방 저장하는 리스트
#     visited = [False] * len(rooms)
#     # visited = Set()
#     # visited = {}

#     # v에 연결되어 있는 모든 vertex 방문할 것
#     def dfs(v):
#         visited[v] = True  # 방문
#         for next_v in rooms[v]:
#             if visited[next_v] == False:  # 방문했었는지 확인, 리스트에서 in을 썼으므로 빅O 추가됨
#                 dfs(next_v)
#     dfs(0)

#     # visited에 모든 방이 있는지 확인
#     if visited == len(rooms):
#         return True
#     else:
#         return False
#     pass


# rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]
# print(canVisitAllRooms(rooms))

from collections import deque


def canVisitAllRooms(rooms):
    visited = [False] * len(rooms)

    def bfs(v):
        queue = deque()
        queue.append(v)
        visited[v] = True
        while queue:
            cur_v = queue.popleft()
            for next_v in rooms[cur_v]:
                if visited[next_v] == False:
                    queue.append(next_v)
                    visited[next_v] = True

    bfs(0)

    return all(visited)  # all: visited 내부의 원소가 모두 참이면 True return


rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]
print(canVisitAllRooms(rooms))
