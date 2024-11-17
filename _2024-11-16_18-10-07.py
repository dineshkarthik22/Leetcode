# Problem: 
# Link: https://leetcode.com/problems/two-sum/
class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            dicti = {}
            for a,b in enumerate(nums):
                diff = target - b
                if diff in dicti:
                    return dicti[diff], a
                dicti[b] = a
    