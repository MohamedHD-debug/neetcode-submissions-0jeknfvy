class Solution:
    def climbStairs(self, n: int) -> int:
        d = [] 
        d.append(1)
        d.append(2)
        for i in range(2,n):
            d.append(d[i-1] + d[i-2])

        return d[n-1]