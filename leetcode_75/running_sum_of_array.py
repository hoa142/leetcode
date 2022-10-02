class Solution():
    """
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums.
    """
    @staticmethod
    def runningSum(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            output.append(sum)
        return output

nums = [1, 2, 3, 4, 5]
print(Solution.runningSum(nums))