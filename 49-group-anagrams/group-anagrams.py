class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = defaultdict(list)
        for word in strs:
            sorted_word_list = sorted(word) #['a','e','t']
            sorted_word = "".join(sorted_word_list)
            dict[sorted_word].append(word)
        return dict.values()
