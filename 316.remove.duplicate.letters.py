class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        sset = list(''.join(sorted(set(s))))
        cdict = {}
        alphabetical = []
        result = []

        for char in sset:
            cdict[char] = 0

        for char in s:
            cdict[char] += 1

        for char in cdict:
            alphabetical.append(char)

        for char in s:
            if char in result:
                cdict[char] -= 1
                continue

            if len(result) == 0:
                result.append(char)
                cdict[char] -= 1

            else:
                if result[-1] < char:
                    result.append(char)
                    cdict[char] -= 1
                
                else:
                    for c in reversed(result):
                        if cdict[c] > 0 and c > char:
                            result.pop()
                        else:
                            break
                    result.append(char)
                    cdict[char] -= 1

        print('result ', ''.join(result))
        return ''.join(result)
        

if __name__ == "__main__":
    x = Solution()
    # s = "cdadabcc"
    j = "cbacdcbc" #acdb
    l = "leetcode" #letcod
    k = "bcabc" #abc
    ab = "cbac" #bac
    z = "edebbed" #bed
    x.removeDuplicateLetters(j)
    print('-----')
    x.removeDuplicateLetters(l)
    print('-----')
    x.removeDuplicateLetters(k)
    print('-----')
    x.removeDuplicateLetters(ab)
    print('-----')
    x.removeDuplicateLetters(z)
    print('-----')