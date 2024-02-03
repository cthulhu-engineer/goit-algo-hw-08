import heapq
import random


n = 10
low = 1
high = 100


# Генеруємо список nums з випадковими числами
nums = [random.randint(low, high) for _ in range(n)]

heapq.heapify(nums)
print(nums)

total_cost = 0
while len(nums) > 1:
    first = heapq.heappop(nums)
    second = heapq.heappop(nums)
    combined = first + second
    total_cost += combined
    heapq.heappush(nums, combined)

print(f"Мінімальна з можливих сум загальних витрат: {total_cost}")
