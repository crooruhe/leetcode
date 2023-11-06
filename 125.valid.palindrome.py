class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''.join([char for char in s if char.isalpha()]).lower()
        return word[::-1] == word




if __name__ == "__main__":
    x = Solution()
    # t = "A man, a plan, a canal: Panama"
    t = "race a car"
    x.isPalindrome(t)