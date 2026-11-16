class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = []
            for i in range(0, len(s), k):
                chunk = s[i : i + k]
                chunk_sum = sum(int(digit) for digit in chunk)
                new_s.append(str(chunk_sum))
            s = "".join(new_s)
        return s