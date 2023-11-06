class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        result = False
        if len(nums) < 3: 
            return result
        one = nums[0]
        three = nums[-2]
        two = nums[-1]
        
        i = 0
        j = len(nums) - 2
        k = len(nums) - 1

        rev = len(nums) - 2
        for idx in range(len(nums)):
            print('one:', one, 'three:', three, 'two ', two)
            print('-')
            print('i:  ', i, ' j:   ', j, 'k   ', k)
            print('--------------------------------')
            if i < j and j < k and one < two and two < three:
                result = True
                print(result)
                return result
            if nums[idx] < one or nums[rev] < one and one >= two:
                if nums[idx] < one:
                    one = nums[idx]
                    i = idx
                else:
                    one = nums[rev]
                    i = rev
            if nums[idx] > one:
                if idx > i and idx > j and nums[idx] < three and j < k:
                    two = nums[idx]
                    k = idx
                if idx < k and idx > i:
                    # if j
                        # two = three # problem exists somewhere here where two is changing when it shouldnt and i need to enforce k > j
                        # k = j
                    three = nums[idx]
                    j = idx

                continue

            if nums[rev] > three or nums[idx] > three:
                if nums[idx] > three:
                    three = nums[idx]
                    if nums[k] > two:
                        two = nums[k]
                        k = j
                    j = idx
                else:
                    three = nums[rev]
                    k = j
                    two = nums[k]
                    j = rev

            if i < j and j < k and one < two and two < three:
                result = True
                print(result)
                return result


            rev -= 1
            if rev < idx: 
                print(result)
                return result



if __name__ == "__main__":
    x = Solution()
    # t = [3,5,0,3,4]
    # t = [3,1,4,2]
    # t = [1,3,2,4,5,6,7,8,9,10]
    t = [-2,1,2,-2,1,2]
    x.find132pattern(t)