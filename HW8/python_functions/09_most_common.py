def most_common(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    return max(counts, key=counts.get)

print("Most common number:", most_common([1, 3, 3, 2, 3, 2, 1]))

