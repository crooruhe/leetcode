class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        rs = s
        rt = t

        def hashtag(word):
            while '#' in word:
                for idx, char in enumerate(word):
                    if char == '#' and idx != 0:
                        word = word[:idx - 1] + word[idx + 1:]
                        break
                    elif char == '#' and idx == 0:
                        word = word[:idx] + word[idx + 1:]
                        break
            return word

        print(hashtag(rs) == hashtag(rt))
        return hashtag(rs) == hashtag(rt)


if __name__ == "__main__":
    x = Solution()
    
    s = "a##c"
    t = "#a#c"
        
    x.backspaceCompare(s, t)        