from collections import deque

queue = deque()  # 양방향으로 enqueue, dequeue 가능

# enqueue() O(1)
queue.append(1)

# dequeue() O(1)
queue.popleft()
