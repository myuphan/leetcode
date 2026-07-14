class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] < nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1

        while n > 0:
            nums1[m+n-1] = nums2[n-1]
            n -= 1


# Create an object
solution = Solution()

# Test case
nums1 = [1, 2, 3, 0, 0, 0]
m = 3

nums2 = [2, 5, 6]
n = 3

# Call the function
solution.merge(nums1, m, nums2, n)

# Print the modified nums1
print(nums1)