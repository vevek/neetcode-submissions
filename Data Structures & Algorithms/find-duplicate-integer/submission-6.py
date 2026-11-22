class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # what are the possible range of values for n
        # len(nums) == n + 1
        # 1 <= nums[i] <= n

        seen = set()

        for val in nums:
            if val in seen:
                return val
            seen.add(val)

        
