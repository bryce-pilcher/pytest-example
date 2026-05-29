from typing import List

import requests


class APIClient:
    def get_data(self, limit: int = 10) -> List[int]:
        res = requests.get(f'http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count={limit}')
        return res.json()


def binary_search(arr: List[int], target):
    lo, hi = 0, len(arr)
    arr.sort()  # [lo, hi)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        elif arr[mid] > target:
            hi = mid
        else:
            return mid
    return -1


def main(val: int) -> int:
    print("Hello from pytest-example!")
    data = APIClient().get_data()
    print(data)
    idx = binary_search(data, val)
    print(f"{'Found value' if idx >= 0 else 'Did not find value'}: {val}")
    return idx


if __name__ == "__main__":
    main(3)
