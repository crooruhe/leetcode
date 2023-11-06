class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        print(n)
        if n == 1:
            print(True)
            return True
        elif n <= 0: 
            print(False)
            return False
        elif n % 4 != 0:
            print(False)
            return False

        else: self.isPowerOfFour(n / 4)


if __name__ == "__main__":
    x = Solution()
    n = 16
    x.isPowerOfFour(n)