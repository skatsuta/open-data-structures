class ArrayDeque:

    def __init__(self) -> None:
        self.a = []
        self.j = 0
        self.n = 0

    @property
    def size(self) -> int:
        return self.n

    def add(self, i: int, x: object) -> None:
        if self.n + 1 >= len(self.a):
            self._resize()

        length = len(self.a)
        if i < self.n // 2:
            # Shift a[0], ..., a[i-1] one to the left
            self.j = length - 1 if self.j == 0 else self.j - 1
            for k in range(0, i):
                self.a[(self.j + k) % length] = self.a[(self.j + k + 1) % length]
        else:
            # Shift a[i+1], ..., a[n-1] one to the right
            for k in range(self.n, i, -1):
                self.a[(self.j + k) % length] = self.a[(self.j + k - 1) % length]

        self.a[(self.j + i) % length] = x
        self.n += 1

    def remove(self, i: int) -> object:
        length = len(self.a)
        x = self.a[(self.j + i) % length]
        if i < self.n // 2:
            # Shift a[0], ..., a[i-1] one to the right
            for k in range(i, 0, -1):
                self.a[(self.j + k) % length] = self.a[(self.j + k - 1) % length]
            self.j = (self.j + 1) % length
        else:
            for k in range(i, self.n):
                self.a[(self.j + k) % length] = self.a[(self.j + k + 1) % length]

        self.n -= 1

        if len(self.a) > self.n * 3:
            self._resize()

        return x

    def _get(self, i: int) -> object:
        return self.a[(self.j + i) % len(self.a)]

    def _set(self, i: int, x: object) -> None:
        y = self._get(i)
        self.a[(self.j + i) % len(self.a)] = x
        return y

    def _resize(self) -> None:
        b = [None] * max(self.n * 2, 1)
        for k in range(0, self.n):
            b[k] = self.a[(self.j + k) % len(self.a)]
        self.a = b
        self.j = 0
