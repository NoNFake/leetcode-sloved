class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        return next(
            [seen[target-x], i]
            for i,x in enumerate(nums)
            if (target -x) in seen or seen.setdefault(x,i) is None
        )