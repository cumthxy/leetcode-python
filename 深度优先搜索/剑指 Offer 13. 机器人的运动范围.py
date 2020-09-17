def sumnum(n):
    ans = 0
    while n:
        ans += n%10
        n = n//10
    return ans

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visted = set()
        def dfs(i,j):
            if i>=m or j>=n or k<sumnum(i)+sumnum(j) or (i,j) in visted:
                return 0
            visted.add((i,j))
            sum_track = 1+dfs(i+1,j)+dfs(i,j+1)

            return sum_track

        return dfs(0,0)



soulation = Solution()
a = soulation.movingCount(2,3,1)
print(a)
