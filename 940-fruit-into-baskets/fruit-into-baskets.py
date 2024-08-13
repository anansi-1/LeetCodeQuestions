class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        container = {}
        j = 0
        max_fruits = 0

        for i in range(len(fruits)):
            container[fruits[i]] = container.get(fruits[i], 0) +1
            while len(container) > 2:
                container[fruits[j]] -= 1
                if container[fruits[j]] == 0:
                    del container[fruits[j]]
                j += 1
            max_fruits = max(max_fruits, i - j +1)
        
        return max_fruits

                    
        