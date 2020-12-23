class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# given
nums = [2, 6, 3, 1]
target = 9

# debug
print(Solution().twoSum(nums, target))