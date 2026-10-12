class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # without using *, /, or % operators.
        """
        # old
        abs_dividend, abs_divisor = abs(dividend), abs(divisor)
        ans = 0
        r = abs_dividend # 7
  

        while r >= abs_divisor: # 7 >= -3
            r -= abs_divisor
            ans += 1

        if dividend<= 0 and divisor<=0:
            return ans
        elif dividend <=0 or divisor<=0:
            ans = 0 - ans

        return(ans)"""
        INT_32_MIN = -2147483648
        INT_32_MAX = 2147483647
        neg = (dividend < 0 ) ^ (divisor < 0)
        a = abs(dividend)
        divisor = abs(divisor)
        
        m = 0

        while a >= divisor:
            temp_div = divisor
            r = 1
            # print(r)

            while a >= (temp_div << 1):
                temp_div <<= 1
                r <<= 1

                # print(f"{temp_div:}")
                # print(f"{r:}")
            
            a -= temp_div
            m += r
            # print(a)
            # print(m)
            # print(m)
        res = (-m if neg else m)
        return max(INT_32_MIN, min(INT_32_MAX, res))
for _ in [
    [7, -3],
    [10, 3],
    [-1, -1],
    [-2147483648, -1]

]:
    print(
        Solution().divide(
            _[0], _[1]
            #  dividend = 10, divisor = 3
            #  dividend = -1, divisor = -1

        )
    )