from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    x: object
    nxt: Optional[object] = None


@dataclass
class SLList:
    head: Optional[Node] = None
    tail: Optional[Node] = None
    n: int = 0

    def push(self, x: object) -> object:
        u = Node(x, nxt=self.head)
        self.head = u

        if self.n == 0:
            self.tail = u

        self.n += 1

        return x

    def pop(self) -> Optional[object]:
        if self.n == 0:
            return None

        x = self.head.x
        self.head = self.head.nxt
        self.n -= 1

        if self.n == 0:
            self.tail = None

        return x

    def add(self, x: object) -> bool:
        u = Node(x)

        if self.n == 0:
            self.head = u
        else:
            self.tail.nxt = u

        self.tail = u
        self.n += 1

        return True

    def remove(self) -> Optional[object]:
        return self.pop()
