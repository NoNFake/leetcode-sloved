class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """
        - so slow...
        +--------+-------+-------+
        | 2155ms | Beats | 5.03% |
        +--------+-------+-------+

        size_f =  len(nums)
        d = [
            i for i in range(size_f)
            if i not in nums 
            ]      
        return size_f if d == [] else d[0]
        """

        n = len(nums)
        s = sum(nums)
        # print(n)
        # print(s)

        x = n*(1 + n ) //2 - s

        return x
        

for _ in [
    # [0,1],
    [1,2],
    [3, 0,1],
    # [0,1]
]:
    print(Solution().missingNumber(_))