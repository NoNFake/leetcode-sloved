class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        f = int("".join([str(_) for _ in digits])) + 1
        h: list = [int(_) for _ in str(f)]
        return h

        

enumerate
for _ in [
    [1,2,3],
    [4,3,2,1],
    [9]
]:
    print(Solution().plusOne(
        _
    ))