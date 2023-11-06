from collections import defaultdict

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        res = []

        sumdict = defaultdict(list)
        for idx, n in enumerate(numbers):
            if n in sumdict:
                res.append(sumdict[n][1])
                res.append(idx + 1)
            else:
                sumdict[target - n].append(n)
                sumdict[target - n].append(idx + 1)

        print(res)
        return res

if __name__ == "__main__":
    x = Solution()
    n = [2,3,4]
    t = 6
    x.twoSum(n, t)