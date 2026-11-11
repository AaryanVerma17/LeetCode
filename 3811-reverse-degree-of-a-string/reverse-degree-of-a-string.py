class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        for i, char in enumerate(s, 1):
            reverse_pos = 27 - (ord(char.lower()) - 96)
            result += reverse_pos * i
        return result