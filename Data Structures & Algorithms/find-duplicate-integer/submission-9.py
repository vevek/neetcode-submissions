class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # what are the possible range of values for n
        # len(nums) == n + 1
        # 1 <= nums[i] <= n

        for num in nums:
            if nums[abs(num)] < 0:
                return abs(num)
            nums[abs(num)] *= -1
 
        
