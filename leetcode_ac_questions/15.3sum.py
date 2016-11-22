class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3 or not nums:
            return []

        nums = sorted(nums)
        return_list = []

        for i in range(0, len(nums)-2):
            if i >= 1 and nums[i] == nums[i-1]:
                continue

            residul_sum_list = self.twoSum(nums[i + 1:], -nums[i])

            for residul_sum in residul_sum_list:
                return_list.append([nums[i], residul_sum[0], residul_sum[1]])

        return return_list

    def twoSum(self, nums, target):
        start, end = 0, len(nums) - 1

        while start < end:
            smaller, bigger = nums[start], nums[end]

            if smaller + bigger == target:
                yield (smaller, bigger)
                while start < end and nums[start] == nums[start+1]:
                    start += 1
                while start < end and nums[end-1] == nums[end]:
                    end -= 1
                start += 1
                end -= 1

            elif smaller + bigger < target:
                start += 1
            else:
                end -= 1

            if smaller == bigger:
                break

s = Solution()
print s.threeSum([-2,0,0,2,2])
