class ArrayStack:

    def __init__(self) -> None:
        self.a = []
        self.n = 0

    @property
    def size(self) -> int:
        return self.n

    def push(self, x: object) -> None:
        self._add(self.n, x)

    def pop(self) -> object:
        return self._remove(self.n - 1)

    def _get(self, i: int) -> object:
        return self.a[i]

    def _set(self, i: int, x: object) -> object:
        y = self.a[i]
        self.a[i] = x
        return y

    def _add(self, i: int, x: object) -> None:
        if self.n + 1 >= len(self.a):
            self._resize()

        for j in range(self.n, i, -1):
            self.a[j] = self.a[j - 1]

        self.a[i] = x
        self.n += 1

    def _remove(self, i: int) -> object:
        x = self.a[i]

        for j in range(i, self.n - 1):
            self.a[j] = self.a[j + 1]

        self.n -= 1

        if len(self.a) >= self.n * 3:
            self._resize()

        return x

    def _resize(self) -> None:
        b = [None] * max(self.n * 2, 1)
        for i in range(0, self.n):
            b[i] = self.a[i]
        self.a = b
