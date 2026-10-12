class Solution:
    def myPow(self, x: float, n: int) -> float:
        # take 1ms
        # print(x**n)

        # try make 0ms
        p = abs(n)
        res = 1.0


        while p > 0:
            if p % 2 ==1:
                res *= x
            x*=x
            p //=2
        # print(res)
        print( 1.0 / res if n < 0 else res)

for _ in [
    [2.00000, 10],
    [2.10000, 3],
    [2.00000, -2]
]:
    # print(_[1])
    Solution().myPow(
        _[0], _[1]
    )