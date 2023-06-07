Q1

def array_pair_sum(nums):
    nums.sort()  # Sort the array in ascending order
    max_sum = 0
    for i in range(0, len(nums), 2):
        max_sum += nums[i]
    return max_sum

Q2

def max_unique_candies(candyType):
    max_candies = len(candyType) // 2
    unique_candies = len(set(candyType))
    return min(max_candies, unique_candies)

Q3

from collections import Counter

def findLHS(nums):
    count = Counter(nums)
    max_length = 0

    for num in nums:
        if num + 1 in count:
            length = count[num] + count[num + 1]
            max_length = max(max_length, length)

    return max_length

Q4.

def can_place_flowers(flowerbed, n):
    count = 0
    length = len(flowerbed)

    for i in range(length):
        if (
            flowerbed[i] == 0 and
            (i == 0 or flowerbed[i - 1] == 0) and
            (i == length - 1 or flowerbed[i + 1] == 0)
        ):
            flowerbed[i] = 1
            count += 1

    return count >= n

Q5.

def maximum_product(nums):
    nums.sort()  # Sort the array in ascending order
    product1 = nums[-1] * nums[-2] * nums[-3]  # Product of the largest three numbers
    product2 = nums[0] * nums[1] * nums[-1]  # Product of the first two numbers and the largest number
    return max(product1, product2)

Q6.

def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

Q7.

def isMonotonic(nums):
    isIncreasing = True
    isDecreasing = True

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            isDecreasing = False
        if nums[i] < nums[i - 1]:
            isIncreasing = False
        if not isIncreasing and not isDecreasing:
            return False

    return True

Q8.

def minimumScore(nums, k):
    minimum = min(nums)
    maximum = max(nums)
    initial_score = maximum - minimum

    if initial_score <= 2 * k:
        return initial_score

    potential_min = float('inf')
    potential_max = float('-inf')

    for num in nums:
        potential_min = min(potential_min, num - k)
        potential_max = max(potential_max, num + k)

    if potential_max - potential_min <= initial_score:
        return potential_max - potential_min
    else:
        return initial_score
