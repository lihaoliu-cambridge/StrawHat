class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_index = len(nums) - 1
        for i in range(last_index, -1, -1):
            if i == last_index:
                continue
            else:
                if nums[i] == nums[i+1]:
                    nums.pop(i+1)
        return len(nums)

    def removeDuplicates_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, only_nums = 0, []
        while i < len(nums):
            only_nums.append(nums[i])
            length_of_i = self.get_length_of_i(nums[i:])
            i += length_of_i

        return only_nums

    def get_length_of_i(self, sliced_nums):
        length_of_nums = len(sliced_nums)
        if length_of_nums == 1:
            return 1
        else:
            if sliced_nums[0] < sliced_nums[length_of_nums//2]:
                return self.get_length_of_i(sliced_nums[:length_of_nums//2])
            else:
                return length_of_nums//2 + self.get_length_of_i(sliced_nums[length_of_nums//2:])


s = Solution()
print s.removeDuplicates([2, 3, 4, 4, 4, 5])
