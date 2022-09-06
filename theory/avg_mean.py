def moving_average(data, K):
    result = []
    current_sum = sum(data[0:K])
    result.append(current_sum / K)
    for i in range(0, len(data) - K):
        current_sum -= data[i]
        current_sum += data[i+K]
        current_avg = current_sum / K
        result.append(current_avg)
    return result 

n = int(input())
a = list(map(int, input().split()))
K = int(input())

result = moving_average(a, K)
print(" ".join(list(map(str, result))))
