from lists import ArrayStack


class TestArrayStack:

    def test_empty(self):
        a = ArrayStack()

        assert a.size == 0

    def test_push(self):
        a = ArrayStack()
        for i in range(0, 10):
            a.push(i)

        assert a.size == 10

    def test_pop(self):
        a = ArrayStack()
        for i in range(0, 10):
            a.push(i)

        for i in range(9, -1, -1):
            assert a.pop() == i
