class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        a = 1
        b = 2


        for _ in range(2, n+1):
            c = a + b
            a = b
            b = c

        return a



for _ in [
    2,
    3,
    4, 
   
]:
    print(
        Solution().climbStairs(
            _
        )
    )
    