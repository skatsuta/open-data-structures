from lists import SLList


class TestSLList:

    def test_push_pop(self):
        sl = SLList()

        for i in range(0, 10):
            sl.push(i)

        for i in range(9, -1, -1):
            assert sl.pop() == i

    def test_add_remove(self):
        sl = SLList()

        for i in range(0, 10):
            sl.add(i)

        for i in range(0, 10):
            assert sl.remove() == i
