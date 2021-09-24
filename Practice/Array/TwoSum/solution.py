from typing import List

arr = [1, 2, 3, 4, 5, 6, 7]
target = 8

arr1 = [2, 7, 11, 15]
target1 = 9
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

arr2 = [3, 2, 4]
target2 = 6
# expected Output: [1,2]

arr3 = [3, 3]
target3 = 6
# Expected Output: [0,1]


def twoSum(nums: List[int], target: int) -> List[int]:
    hash_map = {}
    for i in range(len(nums)):
        if target - nums[i] in hash_map:
            return [hash_map[target - nums[i]], i]
        else:
            hash_map[nums[i]] = i


print(twoSum(arr, target))
print(twoSum(arr1, target1))
print(twoSum(arr2, target2))
print(twoSum(arr3, target3))
