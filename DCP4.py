# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # return 1 if 1 is not here in the array
        if 1 not in nums:
            return 1
        # if 1 is present and then the length is 1 that means 2 is the only answer
        if n==1:
            return 2
        # we start by replacing all the negative, 0 or values that are more than the length of array 
        for i in range(n):
            if nums[i] < 0 or nums[i]==0 or nums[i] > n:
                nums[i]=1
#       using negative sign as presence of that index
        for i in range(n):
            temp = abs(nums[i])
            if temp==n:
                nums[0] = -abs(nums[0])
            else:
                nums[temp] = -abs(nums[temp])
        
        for i in range(1, n):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return n
        return n+1
        