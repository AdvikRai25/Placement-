class Solution:
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        return 1162261467 % n == 0
sol = Solution()
num = int(input("Enter a number: "))
if sol.isPowerOfThree(num):
    print(f"{num} is a power of 3")
else:
    print(f"{num} is NOT a power of 3")
