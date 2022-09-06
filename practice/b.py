def check_parity(a: int, b: int, c: int) -> bool:
    return sum(i & 1 == 0 for i in [a, b, c]) in [0, 3]

def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")

a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
