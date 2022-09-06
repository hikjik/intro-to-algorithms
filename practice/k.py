from typing import List, Tuple


def get_sum(number_list: List[int], k: int) -> List[int]:
    result: List[int] = []

    for number in reversed(number_list):
        number += k
        result.append(number % 10)
        k = number // 10
    while k:
        result.append(k % 10)
        k //= 10
    return result[::-1]


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k


number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))
