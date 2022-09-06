import collections
from typing import Tuple
from collections import Counter

def get_excessive_letter(shorter: str, longer: str) -> str:
    dct = Counter(longer)
    for i in shorter:
        dct[i] -= 1
    for k, v in dct.items():
        if v == 1:
            return k

def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer

shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
