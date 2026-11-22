class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # what are the possible range of values for n
        # len(nums) == n + 1
        # 1 <= nums[i] <= n

        numsv2 = sorted(nums)

        i = 1

        while i < len(numsv2):
            if numsv2[i - 1] == numsv2[i]:
                return numsv2[i]
            
            i += 1
