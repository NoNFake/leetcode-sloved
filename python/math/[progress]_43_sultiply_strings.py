#!/usr/bin/python3

class Solution:

  
    
    def multiply(self, num1: str, num2: str) -> str:      

        return str(self.d(num1)*self.d(num2))
    
    def d(self, intg: str) -> int:
        n = 0
        for i in intg:  
            n = 10 * n+ (ord(i) - 48)
        return n

    
for _ in [
    # ["2", "3"],
    ["123", "456"]
]:
    print(
        Solution().multiply(
            _[0],
            _[1]
        )
    )