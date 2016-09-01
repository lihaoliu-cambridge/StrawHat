import operator


class Solution(object):
    def twoSum(self, nums, target):
        nums_dict = {key: value for key, value in enumerate(nums)}
        nums_dict_sorted = sorted(nums_dict.items(), key=operator.itemgetter(1))
        start = 0
        end = len(nums_dict_sorted)-1
        while start < end:
            if nums_dict_sorted[start][1]+nums_dict_sorted[end][1] == target:
                break
            elif nums_dict_sorted[start][1]+nums_dict_sorted[end][1] > target:
                end -= 1
            else:
                start += 1
        return [nums_dict_sorted[start][0], nums_dict_sorted[end][0]]
