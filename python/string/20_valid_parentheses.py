class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        mem = []
        for c in s:
            if c in "({[":
                mem.append(c)
            else:
                if not mem:
                    return False
                last = mem.pop()

                if last != pairs[c]:
                    return False
        
        # print(mem)
        return (mem == [])