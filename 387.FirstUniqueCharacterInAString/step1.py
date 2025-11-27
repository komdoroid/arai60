class Solution:
    def firstUniqChar(self, s: str) -> int:
        ch_to_index = {}

        for i in range(len(s)):
            if s[i] in ch_to_index:
                ch_to_index[s[i]] = -1
                continue
            ch_to_index[s[i]] = i
        
        for index in ch_to_index.values():
            if index < 0:
                continue
            return index
        return -1