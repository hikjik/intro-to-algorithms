from typing import Tuple
from itertools import zip_longest


def get_sum(first_number: str, second_number: str) -> str:
    result = []

    carry = 0
    for l, r in zip_longest(reversed(first_number), reversed(second_number), fillvalue='0'):
        r = carry + [l, r].count('1')
        result.append('1' if r % 2 == 1 else '0')
        carry = 0 if r < 2 else 1

    if carry:
        result.append('1')

    return "".join(reversed(result))


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
