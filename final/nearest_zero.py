# 69628536

import typing as tp

INFINITY = 10 ** 6


def read_input() -> tp.List[str]:
    input()
    return input().split()


def zero_dist(arr: tp.Iterable[str]) -> tp.List[int]:
    distances: tp.List[int] = []

    dist = INFINITY
    for elem in arr:
        if elem == '0':
            dist = 0
        else:
            if dist < INFINITY:
                dist += 1
        distances.append(dist)

    return distances


def nearest_to_zero(arr: tp.List[str]) -> tp.Iterable[int]:
    left_to_right = zero_dist(arr)
    right_to_left = zero_dist(reversed(arr))

    return map(min, zip(left_to_right, reversed(right_to_left)))


if __name__ == "__main__":
    arr = read_input()
    res = nearest_to_zero(arr)
    print(*res)
