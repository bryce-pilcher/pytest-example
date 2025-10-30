from typing import List

import requests


def get_data(limit: int = 10) -> List[int]:
    res = requests.get(f'http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count={limit}')
    return res.json()


def binary_search(arr, target):
    lo, hi = 0, len(arr)  # [lo, hi)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        elif arr[mid] > target:
            hi = mid
        else:
            return mid
    return -1


def main(val: int):
    print("Hello from pytest-example!")
    data = get_data()
    print(data)
    idx = binary_search(data, val)
    print(f"{'Found value' if idx >= 0 else 'Did not find value'}: {val}")


if __name__ == "__main__":
    main(3)
