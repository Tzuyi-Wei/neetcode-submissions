class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i, val in enumerate(nums):
            map[val] = i
        for i, val in enumerate(nums):
            diff = target - val
            if diff in map and map[diff] != i:
                return [i, map[diff]]
