# Algorithm-DSA

<details>
<summary>스택</summary>
<div markdown="1">

- LIFO(Last In First Out): 후입선출
- push, pop, top, size, empty

  ```python
  # 스택 구현

  def __init__(self):
      self.data = []

  def push(self, x):
      self.data.append(x)

  def pop(self):
      // 비어있을 때
      if not self.data:
          return -1
      return self.data.pop()

  def size(self):
      if not self.data:
          return -1
      return len(self.data)

  def empty(self):
      if not self.data:
          return 1
      else 0

  def top(self):
      if not self.data:
          return -1
      return self.data[-1]
  ```

</div>
</details>

<details>
<summary>큐</summary>
<div markdown="1">

- FIFO(First In First Out): 선입선출
- enqueue, size, dequeue
- 구현방식
  - 원형 큐, 순환 큐
    - front: 데이터를 삭제할 위치를 지정하는 변수
    - rear: 데이터를 저장할 위치를 지정하는 변수
    - count: 데이터의 개수를 저장하는 변수
    - 데이터:front에서 rear 전 까지
    - rear와 배열의 max 사이즈가 같다면 rear을 0으로
    - front == rear 두 가지 경우 -> count 필요
      1. 데이터가 꽉 찬 경우
      2. 데이터가 없는 경우
  - 가변크기 큐

</div>
</details>

<details>
    <summary>연결리스트</summary>
    <div>
        <details>
            <summary>단일 연결리스트</summary>
            <div markdown="1">
                `
                class LinkedList:
                def __init__(self, size):
                    self.size = size
                    self.num = 0
                    self.head = Node(None)
                
                def insert(self, value):
                    if self.num >= self.size:
                        return False
                    
                    node = Node(value)
                    node.next = self.head.next # 비어있을 경우 None
                `
            </div>
            </details>
        </div>
    <details>
        <summary>이중 연결리스트</summary>
    </details>

</details>
