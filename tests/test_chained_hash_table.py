import pytest

from hash_tables import ChainedHashTable


class TestChainedHashTable:

    @pytest.mark.parametrize('items, want', [([1], 1), ([1, 2], 2), ([1, 2, 3], 3)])
    def test_add(self, items, want):
        h = ChainedHashTable()

        for item in items:
            h.add(item)

        assert h.n == want

    @pytest.mark.parametrize('items, target, expected_item, expected_len', [
        ([], 1, None, 0),
        ([1, 2], 3, None, 2),
        ([1, 2, 3], 1, 1, 2),
        ([1, 2, 3], 2, 2, 2),
    ])
    def test_remove(self, items, target, expected_item, expected_len):
        h = ChainedHashTable()

        for item in items:
            h.add(item)

        assert h.remove(target) == expected_item
        assert h.n == expected_len
