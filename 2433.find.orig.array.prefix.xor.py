class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        res = [pref[0]]
        if len(pref) == 1:
            return res
        for i in range(1, len(pref)):
            res.append(pref[i - 1] ^ pref[i])

        print(res)


if __name__ == "__main__":
    x = Solution()
    n = [5,2,0,3,1]
    x.findArray(n)