from lists import ArrayQueue


class TestArrayQueue:

    def test_empty(self):
        a = ArrayQueue()

        assert a.size == 0

    def test_add(self):
        a = ArrayQueue()
        for i in range(0, 10):
            a.add(i)

        assert a.size == 10

    def test_remove(self):
        a = ArrayQueue()
        for i in range(0, 10):
            a.add(i)

        for i in range(0, 10):
            assert a.remove() == i
