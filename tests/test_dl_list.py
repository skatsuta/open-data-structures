from lists import DLList


class TestDLList:

    def test_add_remove(self):
        dl = DLList()

        for i in range(0, 10):
            dl.add(0, i)

        for i in range(9, -1, -1):
            assert dl.remove(0) == i
