class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_to_word = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key not in sorted_to_word.keys():
                sorted_to_word[key] = [word]
            else:
                sorted_to_word[key].append(word)
        return list(sorted_to_word.values())