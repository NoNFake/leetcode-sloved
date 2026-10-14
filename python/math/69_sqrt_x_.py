class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        l=1
        r = x//2

      
        a = 0

        while l<=r:
            m = l + (r-l) // 2

            if m <= x /m:
                a = m
                l = m + 1

            else: 
                r = m -1

        return a
for _ in [
    1, 
    5, 
    6,
    4,
    8
]:
    print(
        Solution().mySqrt(
            _
        )
    )
    