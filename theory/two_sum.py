n = int(input())
nums = list(map(int, input().split()))
x = int(input())


def two_sum_hash(nums, x):
    prev = set()
    for a in nums:
        y = x - a
        if y in prev:
            return a, y
        prev.add(a)
    return None


def two_sum_sort(nums, x):
    nums.sort()

    i, j = 0, len(nums) - 1
    while i < j:
        y = nums[i] + nums[j]
        if y == x:
            return nums[i], nums[j]
        elif y > x:
            j -= 1
        else:
            i += 1
    return None

res = two_sum_sort(nums, x)
if res is not None:
    print(*res)
else:
    print(None)

