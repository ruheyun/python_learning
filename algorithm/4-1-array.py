# Import module
import random


# Initialize array
arr: list[int] = [0] * 5
nums: list[int] = [1, 2, 3, 4, 5]


# Random access element
def random_access(nums: list[int]) -> int:
    random_index = random.randint(0, len(nums) - 1)
    random_num = nums[random_index]
    return random_num


# Insert element num at index of array
def insert(nums: list[int], num: int, index: int):
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    nums[index] = num


# Remove the element at index
def remove(nums: list[int], index: int):
    for i in range(index, len(nums)):
        nums[i] = nums[i + 1]


# Iterate through an array
def traverse(nums: list[int]):
    count = 0

    # Traverse array through index
    for i in range(len(nums)):
        count += nums[i]

    # Traverse array elements directly
    for num in nums:
        count += num

    # Traverse both data indexs and elements simultaneously
    for i, num in enumerate(nums):
        count += nums[i]
        count += num


# Find the specified element in an array
def find(nums: list[int], target: int) -> int:
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1


# Extend array length
def extend(nums: list[int], enlarge: int) -> list[int]:
    res = [0] * (len(nums) + enlarge)

    for i in range(len(nums)):
        res[i] = nums[i]

    return res
