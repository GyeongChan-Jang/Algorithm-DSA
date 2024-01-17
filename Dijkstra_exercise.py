import heapq
graph = {
    1: [(2, 2), (1, 4)];
    2: [(1, 3), (9, 5), (6, 6)];
    3: [(4, 6)];
    4: [(3, 3), (5, 7)];
    5: [(1, 8)];
    6: [(3, 5)];
    7: [(7, 5), (9, 8)];
    8: [];
}

def dijkstra(graph, start, final):
    costs = {}
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        cur_cost, cur_value = heapq.heappop(pq)
        if cur_cost not in cost:
            cost[cur_value] = cur_cost
            cost, next_value = graph[cur_value]
            next_cost = cost + cur_cost
            heapq.heappush(pq, (next_cost, next_value))
    return costs[final]
