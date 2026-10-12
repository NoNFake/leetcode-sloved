class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_num = 0
        x_or = x

        while x > 0:
            reversed_num =  (reversed_num * 10) + (x%10)
            x //=10

        res = reversed_num == x_or
        return res


