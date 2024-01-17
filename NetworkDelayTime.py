import heapq
from collections import defaultdict
# 주어진 네트워크에는 n개의 노드가 있으며, 이는 1부터 n까지 레이블이 붙어 있습니다.
# 또한 times[i] = (u, v, w)
# k노드에서 신호를 보낼 때, 모든 노드에 신호가 도달하기 위한 최소 비용을 반환하시오.
# 하나의 노드라도 도달하지 못한다면 -1을 반환하시오.
# (한 노드에서 연결된 여러 개의 edge 신호를 동시에 전달할 수 있습니다.)

# input: times = [[2, 1, 2], [2, 3, 5], [2, 4, 1], [4, 3, 3]]
# n = 4
# k = 2
# output: 4

# input: times = [[2, 1, 2], [2, 3, 5], [2, 4, 1], [4, 3, 3]]
# n = 4
# k = 4
# output: 4

times = [[2, 1, 2], [2, 3, 5], [2, 4, 1], [4, 3, 3]]
n = 4
k = 2


def dijkstra(graph, n, k):
    # 1. 그래프 구현 O(times.length)
    graph = defaultdict(list)
    for time in times:
        graph[time[0]].append((time[2], time[1]))

    print(graph)
    # 2. 다익스트라 알고리즘 O(ElogE)
    costs = {}
    pq = []
    heapq.heappush(pq, (0, k))

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if cur_cost not in costs:
            costs[cur_node] = cur_cost
            for cost, next_node in graph[cur_node]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_node))

    # 3. 방문 못한 노드 찾기 O(n)
    for node in range(1, n + 1):
        if node not in costs:
            return -1

    # 4. 최소값중에서 최대값 구하기 O(n)
    return max(costs.values())


dijkstra(times, n, k)
