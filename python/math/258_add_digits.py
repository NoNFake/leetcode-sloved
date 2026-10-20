class Solution:
    def addDigits(self, num: int) -> int:
        n = str(num)
        while len(n) > 1:
            n = str(sum(int(i) for i in str(n)))
            # print(n)
        return int(n)





for _ in [
   38


]:
    print(
        Solution().addDigits(
            _
        )
    )