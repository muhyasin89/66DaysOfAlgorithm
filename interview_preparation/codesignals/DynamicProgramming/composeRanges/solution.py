def composeRanges(nums):

    ranges = []
    while nums:
        start = end = nums.pop(0)
        while nums and nums[0] - end == 1:
            end = nums.pop(0)
        ranges.append(str(start) + ("", "->" + str(end))[start != end])
    return ranges
