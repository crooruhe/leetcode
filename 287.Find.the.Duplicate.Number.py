class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        bset = set()
        tset = set()

        l = 0
        r = len(nums) - 1

        while (l != r):
            blenpre = len(bset)
            tlenpre = len(tset)

            bset.add(nums[l])
            tset.add(nums[r])
            
            blenpost = len(bset)
            tlenpost = len(tset)

            if (blenpre == blenpost):
                print(nums[l])
                return nums[l]
            
            if (tlenpre == tlenpost):
                print(nums[r])
                return nums[r]

            l += 1
            r -= 1

            if (l == r):
                blenpre = len(bset)
                bset.add(nums[l])
                blenpost = len(bset)

                if (blenpre == blenpost):
                    print(nums[l])
                    return nums[l]
        
        result = bset & tset
        result = list(result)
        print(result[0])
        return result[0]

if __name__ == "__main__":
    t = [3,1,5,4,2,6,7,9,1]
    x = Solution()

    x.findDuplicate(t)