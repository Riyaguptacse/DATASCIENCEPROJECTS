class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sol= [0] * len(nums)
        sol[0] = nums[0]
        for i in range(1, len(nums)):
            sol[i] = sol[i-1] + nums[i]
        return sol
        