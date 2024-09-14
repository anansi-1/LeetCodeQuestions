class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
            distinct = []
            count = defaultdict(int)
            for i in arr:
                count[i] += 1
            # print(count)
            for i, value in count.items():
                if value == 1:
                    distinct.append(i)
            if len(distinct) >= k:
                return distinct[k-1]
            else:
                return ""