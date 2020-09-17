

class Solution:
    def pondSizes(self, land):

        def df(land, x, y):
            num = 0
            if (x < 0 or x >= len(land) or y < 0 or y >= len(land[0]) or land[x][y] != 0):
                return num
            num += 1
            land[x][y] = -1
            num += df(land, x + 1, y)
            num += df(land, x - 1, y)
            num += df(land, x, y + 1)
            num += df(land, x, y - 1)
            num += df(land, x + 1, y + 1)
            num += df(land, x + 1, y - 1)
            num += df(land, x - 1, y + 1)
            num += df(land, x - 1, y - 1)
            return num

        result = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                temp = df(land, i, j)
                if temp != 0:
                    result.append(temp)

        a = sorted(result)
        return a



a = [[1,2,3],[4,5,6]]
print(a)

