class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        run_sum=[]
        cursum=0
        for i in nums:
            cursum+=i
            run_sum.append(cursum)
        return run_sum
        