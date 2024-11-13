class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        combined_range= []
        for i in ranges:
            for i in range(i[0],i[-1]+1):
                combined_range.append(i)
        

        for i in range(left,right+1):
            if i in combined_range:
                continue
            else:
                return False
        return True


        return False
        print(cobined_range)