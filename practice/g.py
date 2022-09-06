def to_binary(number: int) -> str:
    digits = []
    while number:
        digits.append(number % 2)
        number //= 2
    digits = digits or [0]
    return "".join(map(str, reversed(digits)))

def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))
