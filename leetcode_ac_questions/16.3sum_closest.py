class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0

        nums = sorted(nums)
        first_value, second_value, third_value = nums[0], nums[1], nums[-1]
        min_diff = abs(first_value + second_value + third_value - target)

        for i in range(0, len(nums) - 2):
            if i > 1 and nums[i] == nums[i - 1]:
                continue

            tmp_second_value, tmp_third_value = self.twoSumClosest(nums[i + 1:], target - nums[i])
            cur_diff = nums[i] + tmp_second_value + tmp_third_value - target

            if abs(cur_diff) < min_diff:
                min_diff, first_value, second_value, third_value = abs(cur_diff), nums[
                    i], tmp_second_value, tmp_third_value

        return first_value + second_value + third_value

    def twoSumClosest(self, nums, target):
        start, end = 0, len(nums) - 1
        return_start_value, return_end_value = nums[start], nums[end]
        min_diff = abs(return_start_value + return_end_value - target)

        while start < end:
            cur_diff = nums[start] + nums[end] - target

            if abs(cur_diff) < min_diff:
                min_diff = abs(cur_diff)
                return_start_value, return_end_value = nums[start], nums[end]

            if cur_diff > 0:
                end -= 1
            else:
                start += 1

        return return_start_value, return_end_value


s = Solution()
print s.threeSumClosest(
    [13, 2, 0, -14, -20, 19, 8, -5, -13, -3, 20, 15, 20, 5, 13, 14, -17, -7, 12, -6, 0, 20, -19, -1, -15, -2, 8, -2, -9,
     13, 0, -3, -18, -9, -9, -19, 17, -14, -19, -4, -16, 2, 0, 9, 5, -7, -4, 20, 18, 9, 0, 12, -1, 10, -17, -11, 16,
     -13, -14, -3, 0, 2, -18, 2, 8, 20, -15, 3, -13, -12, -2, -19, 11, 11, -10, 1, 1, -10, -2, 12, 0, 17, -19, -7, 8,
     -19, -17, 5, -5, -10, 8, 0, -12, 4, 19, 2, 0, 12, 14, -9, 15, 7, 0, -16, -5, 16, -12, 0, 2, -16, 14, 18, 12, 13, 5,
     0, 5, 6], -59)
