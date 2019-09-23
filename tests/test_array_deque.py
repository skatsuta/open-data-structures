from lists import ArrayDeque


class TestArrayDeque:

    def test_empty(self):
        a = ArrayDeque()

        assert a.size == 0

    def test_add(self):
        a = ArrayDeque()
        for i in range(0, 10):
            a.add(a.size, i)

        assert a.size == 10

    def test_remove(self):
        a = ArrayDeque()
        for i in range(0, 10):
            a.add(a.size, i)

        for i in range(0, 10):
            assert a.remove(0) == i
