class Solution(object):
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)

if __name__ == "__main__":
    s = Solution()
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Single number is:", s.singleNumber(nums))
