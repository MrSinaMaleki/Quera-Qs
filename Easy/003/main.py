num = int(input())
nums = list(map(int, input().split()))

nums_list_sorted = sorted(nums, reverse=True)

total_price = 0
for i in range(len(nums_list_sorted)):
    if (i + 1) % 3 != 0:
        total_price += nums_list_sorted[i]

print(total_price)
