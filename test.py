def total(nums: list[int]):
    total = 0
    for num in nums:
        total += num
    return total


def highest(nums: list[int]):
    nums.sort(reverse=True)
    return nums[0]


def minimum(nums: list[int]):
    nums.sort()
    return nums[0]


def average(nums: list[int]):
    SUM = total(nums)
    LENGTH = len(nums)

    return (SUM/LENGTH)


nums = [1, 2, -3.4, 4, 5.3]
TOTAL = total(nums)
HIGHEST = highest(nums)
MINIMUM = minimum(nums)
AVERAGE = average(nums)

print(MINIMUM, HIGHEST, TOTAL, AVERAGE)
