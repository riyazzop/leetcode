class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(nums):
            rob1,rob2=0,0
            for num in nums:
                newRob=max(rob1+num,rob2)
                rob1=rob2
                rob2=newRob
            return rob2
        if len(nums)==1:return nums[0]
        return max(helper(nums[1:]),helper(nums[:-1]))
        