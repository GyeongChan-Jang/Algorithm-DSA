# Array List, Linked List 둘 다 가능
# Array List -> visit 할 경우 O(n), back/forward O(1)
# Linked List -> visit O(1), back/forward O(n)
class ListNode(object):
    def __init__(self, val=0, next=None, prev=None):
        # W Linked List
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory(object):
    def __init__(self, homepage):
        self.head = self.current = ListNode(val=homepage)

    def visit(self, url):
        self.current.next = ListNode(val=url, prev=self.current)
        self.current = self.current.next
        return NotImplementedError

    def back(self, steps):
        while steps > 0 and self.current.prev != None:
            steps -= 1
            self.current = self.current.prev
        return self.current.val

    def forward(self, steps):
        while steps > 0 and self.current.prev != None:
            steps -= 1
            self.current = self.current.next
        return self.current.vals
