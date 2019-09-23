class ArrayQueue:

    def __init__(self) -> None:
        self.a = []
        self.j = 0
        self.n = 0

    @property
    def size(self) -> int:
        return self.n

    def add(self, x: object) -> bool:
        if self.n + 1 >= len(self.a):
            self._resize()

        self.a[(self.j + self.n) % len(self.a)] = x
        self.n += 1
        return True

    def remove(self) -> object:
        x = self.a[self.j]
        self.j = (self.j + 1) % len(self.a)
        self.n -= 1
        if len(self.a) >= self.n * 3:
            self._resize()
        return x

    def _resize(self) -> None:
        b = [None] * max(self.n * 2, 1)
        for k in range(0, self.n):
            b[k] = self.a[(self.j + k) % len(self.a)]
        self.a = b
        self.j = 0
