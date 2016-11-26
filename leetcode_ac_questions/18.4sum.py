class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)

        return self.iterToGetKSsum(nums, target, 4)

    def iterToGetKSsum(self, nums, target, k):
        if len(nums) < k:
            return []

        if k != 2:
            results_list = []
            for i in range(0, len(nums) - k + 1):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                k_subtract_1_sum_result = map(lambda tmp_list: [nums[i]] + tmp_list,
                                              self.iterToGetKSsum(nums[i + 1:], target - nums[i], k - 1))
                results_list += k_subtract_1_sum_result

            return results_list
        else:
            two_sum_result = []
            start, end = 0, len(nums) - 1

            while start < end:
                if nums[start] + nums[end] == target:
                    two_sum_result.append([nums[start], nums[end]])

                    while start < end and nums[start + 1] == nums[start]:
                        start += 1
                    while start < end and nums[end - 1] == nums[end]:
                        end -= 1

                    start += 1
                    end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    end -= 1

            return two_sum_result


s = Solution()
print s.fourSum([1, 0, -1, 0, -2, 2], 0)
print s.fourSum([0, 0, 0, 0], 0)
