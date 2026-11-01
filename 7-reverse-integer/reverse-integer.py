class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        l = []
        for i in str(x):
            l.append(i)
        l.reverse()
        s = "".join(l) 
        p = int(s) * sign
        if p < -2**31 or p > 2**31 - 1:
            return 0   
        return p