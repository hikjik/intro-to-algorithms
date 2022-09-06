from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    randomness = 0
    for i in range(len(temperatures)):
        randomness += (
            (i == 0 or temperatures[i-1] < temperatures[i])
            and
            (i == len(temperatures) - 1 or temperatures[i+1] < temperatures[i])
        )
    return randomness


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
