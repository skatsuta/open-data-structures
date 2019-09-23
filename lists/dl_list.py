from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    x: object
    prev: Optional[object] = None
    next: Optional[object] = None


class DLList:

    def __init__(self) -> None:
        dummy = Node(None)
        dummy.prev = dummy
        dummy.next = dummy
        self.dummy = dummy
        self.n = 0

    def __str__(self) -> str:
        if self.n == 0:
            return '[]'

        elems = []
        cur = self.dummy.next
        while cur != self.dummy:
            elems.append(f'[{cur.x}]')
            cur = cur.next

        return ' <-> '.join(elems)

    def get_node(self, i: int) -> Node:
        if i < self.n // 2:
            p = self.dummy.next
            for _ in range(0, i):
                p = p.next
        else:
            p = self.dummy
            for _ in range(self.n, i, -1):
                p = p.prev

        return p

    def get(self, i: int) -> object:
        return self.get_node(i).x

    def set(self, i: int, x: object) -> object:
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def add_before(self, w: Node, x: object) -> Node:
        u = Node(x, prev=w.prev, next=w)
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u

    def add(self, i: int, x: object) -> None:
        self.add_before(self.get_node(i), x)

    def remove_node(self, w: Node) -> None:
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1

    def remove(self, i: int) -> object:
        w = self.get_node(i)
        x = w.x
        self.remove_node(w)
        return x

    def is_palindrome(self) -> bool:
        a = self.dummy.next
        b = self.dummy.prev

        for i in range(0, self.n // 2 + 1):
            if a.x != b.x:
                return False

            a = a.next
            b = b.prev

        return True

    def rotate(self, r: int) -> None:
        mod = r % self.n
        if mod == 0:
            return

        if mod <= self.n / 2:
            cur = self.dummy.next
            for _ in range(0, mod):
                cur = cur.next
        else:
            cur = self.dummy.prev
            for _ in range(self.n, mod + 1, -1):
                cur = cur.prev

        # current node is now a new head!
        new_head = cur

        dummy = self.dummy
        old_head = dummy.next
        old_tail = dummy.prev
        old_tail.next = old_head
        new_tail = new_head.prev
        new_tail.prev = old_tail
        new_tail.next = dummy
        new_head.prev = dummy
        dummy.prev = new_tail
        dummy.next = new_head
