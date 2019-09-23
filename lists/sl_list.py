from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    x: object
    next: Optional[object] = None


@dataclass
class SLList:
    head: Optional[Node] = None
    tail: Optional[Node] = None
    n: int = 0

    def __str__(self) -> str:
        if self.n == 0:
            return '[]'

        elems = []
        cur = self.head
        while cur:
            elems.append(f'[{cur.x}]')
            cur = cur.next

        return ' -> '.join(elems)

    def push(self, x: object) -> object:
        u = Node(x, next=self.head)
        self.head = u

        if self.n == 0:
            self.tail = u

        self.n += 1

        return x

    def pop(self) -> Optional[object]:
        if self.n == 0:
            return None

        x = self.head.x
        self.head = self.head.next
        self.n -= 1

        if self.n == 0:
            self.tail = None

        return x

    def add(self, x: object) -> bool:
        u = Node(x)

        if self.n == 0:
            self.head = u
        else:
            self.tail.next = u

        self.tail = u
        self.n += 1

        return True

    def remove(self) -> Optional[object]:
        return self.pop()

    def second_last(self) -> Optional[object]:
        prev = None
        cur = self.head
        while cur and cur.next:
            prev = cur
            cur = cur.next
        return None if prev is None else prev.x

    def reverse(self) -> None:
        if self.n <= 1:
            return

        u = self.head
        self.tail = u
        w = u.next
        u.next = None
        for i in range(0, self.n - 1):
            v = w.next
            w.next = u

            u = w
            w = v

        self.head = u
