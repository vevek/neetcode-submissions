class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # what are the possible range of values for n
        # len(nums) == n + 1
        # 1 <= nums[i] <= n

        seen = [0] * len(nums)

        for num in nums:
            if seen[num] != 0:
                return num
            seen[num] = num
 
        
