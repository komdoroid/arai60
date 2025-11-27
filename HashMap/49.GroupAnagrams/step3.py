class Solution(object):
    def groupAnagrams(self, strs):
        count_to_word = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for chr in word:
                count[ord(chr) - ord('a')] += 1
            key = tuple(count)
            count_to_word[key].append(word)
        return list(count_to_word.values())  