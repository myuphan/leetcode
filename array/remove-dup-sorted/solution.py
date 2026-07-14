class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        k = 0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[k] = nums[i]
                k += 1
        nums[k] = nums[-1]
        k += 1
        print(k)


Solution = Solution()


nums = [1,1,2]
Solution.removeDuplicates(nums)
print(nums)
