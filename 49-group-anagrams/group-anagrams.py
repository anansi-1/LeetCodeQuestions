class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = defaultdict(list)
        for word in strs:
            sorted_word_list = sorted(word) #['a','e','t']

            dict[tuple(sorted_word_list)].append(word)
        return dict.values()
