class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = {}
        for word in strs:
            count = [0]*26
            for letter in word:
                count[97 - ord(letter)] += 1
            if tuple(count) in dict:
                dict[tuple(count)].append(word) 
            else:
                dict[tuple(count)] = [word]
        return dict.values()
