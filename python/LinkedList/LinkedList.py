# LinkedList의 노드 구현
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


first = Node(1)
second = Node(2)
third = Node(3)
first.next = second
second.next = third
first.value = 6

# LinkedList: append


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while (current.next):
                current = current.next
            current.next = new_node

    def get(self, idx):
        current = self.head
        # while (current.value != idx):
        #     current = current.next
        # return current.value
        for _ in range(idx):
            current = current.next
        return current.value

    def insert(self, idx, value):
        insert_node = Node(value)
        if idx == 0:
            insert_node.next = self.head
            self.head = insert_node
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            insert_node.next = current.next
            current.next = insert_node

    def remove(self, idx):
        if idx == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(idx-1):
                current = current.next
            current.next = current.next.next

    def append_back(self, value):  # O(1)
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        # 맨 뒤의 node가 new_node를 가리키도록
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
