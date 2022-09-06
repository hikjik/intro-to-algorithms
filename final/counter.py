# 69617830

import typing as tp
from collections import Counter


FIELD_SIZE = 4


def read_input() -> tp.Tuple[int, str]:
    k = int(input())
    field = "".join(input().strip() for _ in range(FIELD_SIZE))
    return k, field


def score(k: int, field: str) -> int:
    stats = Counter(filter(str.isdigit, field))
    return sum(v <= 2 * k for v in stats.values())


if __name__ == "__main__":
    k, field = read_input()
    print(score(k, field))
