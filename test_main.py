import random
from typing import List

import pytest
from hypothesis import given, strategies as st

from main import binary_search, main, APIClient


@pytest.mark.parametrize('arr, target, expected', [
    ([1,2,3,4,5,6,7,8,9,10], 1, 0),
    ([1,2,3,4,5,9,8,7,6], 7, 6),
    ([], 1, -1)
]
)
def test_binary_search(arr, target, expected):
    assert binary_search(arr, target) == expected


@given(st.lists(st.integers(), min_size=10, max_size=20))
def test_random_binary_search(arr: List[int]):
    val = arr[random.randint(1,10)]
    assert binary_search(arr, val) >= 0



@pytest.fixture
def array_20251020():
    return [1,2,3,4,5,6,7,8]


def test_main(monkeypatch, array_20251020):
    monkeypatch.setattr(APIClient, "get_data", lambda _: array_20251020)
    idx = main(4)
    assert idx >= 0

