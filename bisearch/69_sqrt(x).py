class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while 1:
            m = int((l+r)/2)
            if m*m <= x and (m+1)*(m+1) > x:
                return m
            elif (m+1)*(m+1) == x:
                return m+1
            elif m*m > x:
                r = m
            else:
                l = m
    