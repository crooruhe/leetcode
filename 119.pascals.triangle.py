# 119. Pascal's Triangle II

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            print([1, 1])
            return [1, 1]
        result = [1, 1]
        for i in range(2, rowIndex + 1):
            temp = [1]
            for x in range(1, len(result)):
                temp.append(result[x] + result[x - 1])

            temp.append(1)
            result = temp
        print(result)
        return result
###########################################################
"""         if rowIndex == 0:
            return [1]
        tmp = [0] + self.getRow(rowIndex-1) + [0]
        print(tmp)
        res = []
        for i in range(len(tmp)-1):
            res.append(tmp[i] + tmp[i+1])
        print('res ', res)
        return res """

if __name__ == "__main__":
    x = Solution()
    # t = 3
    z = 3
    x.getRow(z)