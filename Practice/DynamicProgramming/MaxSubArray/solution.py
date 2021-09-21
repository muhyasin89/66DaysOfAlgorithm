from types import List

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
expected = 6  # Output:
# Explanation: [4,-1,2,1] has the largest sum = 6.

nums1 = [1]
expected1 = 1

nums2 = [5, 4, -1, 7, 8]
expected2 = 23


def maxSubArray(self, nums: List[int]) -> int:
    cursum = 0
    maxsum = nums[0]
    for n in nums:
        cursum = max(cursum + n, n)
        maxsum = max(maxsum, cursum)
    return maxsum
