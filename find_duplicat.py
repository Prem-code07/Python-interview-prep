def find_duplicates(nums):
    result = []
    seen = set()
    for num in nums:
        if num in seen:
            result.append(num)
        else:
            seen.add(num)
    return result
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_duplicates(nums))
