import random
from typing import List

from main import binary_search, main, APIClient
from hypothesis import given, strategies as st
import pytest

# Original test
def test_binary_search():
    test_arr = [1,2,3,4,5,6,7,8,9,10]
    assert binary_search(test_arr, 1) == 0

# Parametrize let's you run a whole set of tests under the same conditions
@pytest.mark.parametrize('arr, target, expected', [
    ([1,2,3,4,5,6,7,8,9,10], 1, 0),
    ([1,2,3,4,5,9,8,7,6], 7, 6),
    ([], 1, -1)])
def test_binary_search(arr,  target, expected):
    assert binary_search(arr, target) == expected

# Fixtures are reusable functions
@pytest.fixture
def array_20260529():
    return [1,2,3,4,5,6,7,8]

# Monkeypatch helps you isolate your code from external dependencies
def test_main(monkeypatch, array_20260529):
    monkeypatch.setattr(APIClient, "get_data", lambda _: array_20260529)
    idx = main(4)
    assert idx >= 0


# Property based testing with Hypothesis. https://hypothesis.readthedocs.io/en/latest/
@given(st.lists(st.integers(), min_size=10, max_size=20))
def test_random_binary_search(arr: List[int]):
    val = arr[random.randint(1,10)]
    assert binary_search(arr, val) >= 0