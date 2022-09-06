def is_power_of_four(number: int) -> bool:
    return number in {4 ** i for i in range(7)}

print(is_power_of_four(int(input())))
