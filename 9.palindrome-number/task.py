class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        sz = len(x)
        for i in range(sz // 2):
            if x[i] != x[-i - 1]:
                return False
        return True
