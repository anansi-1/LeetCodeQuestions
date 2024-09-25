class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = {}
        
        for str in strs:
            key = [0] * 26

            for c in str:
                key[ord(c) - ord('a')] += 1

            keytuple = tuple(key)

            if keytuple in map:
                map[keytuple].append(str)
            
            else:
                map[keytuple] = [str]

        
        return map.values()

        





        