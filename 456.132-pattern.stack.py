class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        # i < j < k
        # nums[i] *one < nums[k] *two < nums[j] *three
        result = False
        staq = {}




        for i in reversed(nums):

        
        
        return result



if __name__ == "__main__":
    x = Solution()
    # t = [3,5,0,3,4]
    # t = [3,1,4,2]
    # t = [1,3,2,4,5,6,7,8,9,10]
    t = [-2,1,2,-2,1,2]
    x.find132pattern(t)