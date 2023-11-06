class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        # odds = []
        # evens = []

        # for char in nums:
        #     if int(char) % 2 == 0:
        #         evens.append(char)
        #     else:
        #         odds.append(char)

        """ def eoqsort(nums):
            pivot = len(nums) // 2
            l = 0
            r = len(nums) - 1 """ # not sure if this would even be necessary

        """ cnt = 0
        for i in range(len(nums)):
            if not nums[i] % 2:
                print('numsi ', nums[i], 'nums cnt', nums[cnt])
                nums[i], nums[cnt] = nums[cnt], nums[i]
                cnt += 1
        print(nums) """

        nums.sort(key = lambda x: x % 2) #this is beautiful


        print(nums)
        return nums
        # return evens + odds

if __name__ == "__main__":
    x = Solution()
    t = [3, 6, 1, 2, 5, 4, 7]
    x.sortArrayByParity(t)