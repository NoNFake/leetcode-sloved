class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n in [4,8]:
        #     b = (2)**int(n>>1) == n
        #     print(f"{n}: {2**int(n**0.5)}" )
        #     return b
        # b =(2)**int(n>>2) == n 

        return  n > 0 and (n & (n - 1)) == 0



for _ in [
    -1,
    3,
    1,
    4,
    8,
    16,
    3,


]:
    print(
        Solution().isPowerOfTwo(
            _
        )
    )