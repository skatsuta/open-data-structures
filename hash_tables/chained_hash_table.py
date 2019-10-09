class ChainedHashTable:

    def __init__(self) -> None:
        self.t = [[]]
        self.n = 0

    def add(self, x: object) -> bool:
        if self.find(x) is not None:
            return False

        if self.n + 1 > len(self.t):
            self.t.append([])

        self.t[self._hash(x)].append(x)
        self.n += 1

        return True

    def remove(self, x: object) -> object:
        bucket = self.t[self._hash(x)]

        for i in range(len(bucket)):
            y = bucket[i]
            if y == x:
                del bucket[i]
                self.n -= 1
                return y

        return None

    def find(self, x: object) -> object:
        bucket = self.t[self._hash(x)]

        for i in range(len(bucket)):
            if x == bucket[i]:
                return bucket[i]

        return None

    def _hash(self, x: object) -> int:
        if len(self.t) == 0:
            return 0
        return (hash(x) & (1 << 64 - 1)) % len(self.t)
