class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = defaultdict(int)
        lucky_max = -1
        for i in arr:
            count[i] += 1
        for i,value in count.items():
            if value == i:
                lucky_max = max(lucky_max, value)
        return lucky_max

