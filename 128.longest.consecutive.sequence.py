class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        x = list(set(nums))
        x.sort()
        print(x)
        c = 1
        hi = []
        # if len(nums) == 1:
        #     return 1
        if len(nums) == 0:
            return 0
        for idx in range(1, len(x)):
            if x[idx] == x[idx - 1] + 1 and idx < len(x):
                c += 1
                continue
            else:
                hi.append(c)
                # print('hi', hi)
                c = 1
        hi.append(c)
        print(max(hi))
        return c

if __name__ == "__main__":
    x = Solution()
    # t = [0,3,7,2,5,8,4,6,0,1]
    t = [100,4,200,1,3,2]
    # t = [9,1,4,7,3,-1,0,5,8,-1,6]
    x.longestConsecutive(t)