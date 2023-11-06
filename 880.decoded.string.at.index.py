class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        if k == 1:
            return s[0]
        total = 0
        for char in s:
            if char.isdigit():
                total *= int(char)
            else:
                total += 1


        for i in reversed(s):
            k = k % total
            if k == 0 and i.isalpha():
                print(i)
                return i
            elif i.isdigit():
                total = total // int(i)
            else:
                total -= 1

if __name__ == "__main__":
    x = Solution()
    s = "leet2code3" # 10
    j = "ha22" #5
    z = "y959q969u3hb22odq595" #222_280_369
    fail = "a23b456789gh9999pqrs9999u99a9xyzpqrstuvw9" #76797
    x.decodeAtIndex(z, 222_280_369)
