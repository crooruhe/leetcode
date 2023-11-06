from functools import reduce

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = nums[:]
        # print('nums: ', nums)
        # for idx, val in enumerate(nums):
        #     if idx == 0:
        #         res.append(reduce(lambda x, y: x * y, nums[idx + 1:]))
        #     elif idx == len(nums) - 1:
        #         res.append(reduce(lambda x, y: x * y, nums[:-1]))
        #     else:
        #         temp = reduce(lambda x, y: x * y, nums[:idx])
        #         temp *= reduce(lambda x, y: x * y, nums[idx + 1:])
        #         res.append(temp)

        lsum = 1
        for l in range(len(nums)):
            res[l] = lsum
            lsum *= nums[l]

        rsum = 1
        for r in range(len(nums) - 1, -1, -1):
            res[r] *= rsum
            rsum *= nums[r]

        print(res)
        return res
        
if __name__ == "__main__":
    x = Solution()
    nums = [1,2,3,4]
    x.productExceptSelf(nums)