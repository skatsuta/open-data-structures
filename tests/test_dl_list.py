import pytest

from lists import DLList


class TestDLList:

    def test_add_remove(self):
        dl = DLList()

        for i in range(0, 10):
            dl.add(0, i)

        for i in range(9, -1, -1):
            assert dl.remove(0) == i

    @pytest.mark.parametrize('expected, items', [
        (True, []),
        (True, [0]),
        (True, [0, 0]),
        (True, [0, 1, 0]),
        (True, [0, 1, 1, 0]),
        (True, [0, 1, 2, 1, 0]),
        (True, [0, 1, 2, 2, 1, 0]),
        (False, [0, 1]),
        (False, [0, 1, 2]),
        (False, [0, 1, 2, 0]),
        (False, [0, 1, 1, 3]),
        (False, [0, 1, 2, 1, -1]),
        (False, [0, 1, 2, 2, -1, 0]),
        (False, [0, 1, 2, 3, 1, 0]),
    ])
    def test_is_palindrome(self, expected, items):
        dl = DLList()

        for i in items:
            dl.add(0, i)

        assert dl.is_palindrome() == expected

    @pytest.mark.parametrize('r, expected', [
        (0, [0, 1, 2, 3, 4, 5]),
        (1, [1, 2, 3, 4, 5, 0]),
        (2, [2, 3, 4, 5, 0, 1]),
        (3, [3, 4, 5, 0, 1, 2]),
        (4, [4, 5, 0, 1, 2, 3]),
        (5, [5, 0, 1, 2, 3, 4]),
        (6, [0, 1, 2, 3, 4, 5]),
        (7, [1, 2, 3, 4, 5, 0]),
    ])
    def test_rotate(self, r, expected):
        dl = DLList()

        items = [i for i in range(0, 6)]
        for i in items:
            dl.add(dl.n, i)

        dl.rotate(r)

        for i in range(0, dl.n):
            print(f'assertion {i}, n = {dl.n}')
            assert dl.remove(0) == items[(i + r) % len(items)]
