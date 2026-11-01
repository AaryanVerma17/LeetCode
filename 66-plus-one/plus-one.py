class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = int("".join(map(str, digits)))
        result +=1
        original_list = [int(char) for char in str(result)]
        return original_list