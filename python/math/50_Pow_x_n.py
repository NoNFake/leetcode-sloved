class Solution:
    def myPow(self, x: float, n: int) -> float:
        a = 1
        # print(n)
        for i in range(n):
            a *= x
            # print(i)

        # print(round(a))




for _ in [
    [2.00000, 10],
    [2.10000, 3],
    [2.00000, -2]
]:
    # print(_[1])
    Solution().myPow(
        _[0], _[1]
    )