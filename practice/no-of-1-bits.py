class Solution:
    def hammingWeight(self, n: int) -> int:
        # print(n)
        bits = 0
        for i in range(32):
            bits += n&1
            n >>=1
        return bits
        