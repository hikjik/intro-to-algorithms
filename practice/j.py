from typing import List


def factorize(number: int) -> List[int]:
    factors: List[int] = []
    d = 2
    while d*d <= number:
        while number % d == 0:
            factors.append(d)
            number //= d
        d += 1
    if number > 1:
        factors.append(number)
    return factors


result = factorize(int(input()))
print(" ".join(map(str, result)))
