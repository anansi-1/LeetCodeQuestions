class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        double = {}
        for i in range(len(arr)):
            double[i] = double.get(i, 0) + (arr[i] * 2)
        for i in range(len(arr)):
            for j in range(len(arr)):
                if (i != j) and (arr[i] == double[j]):
                    return True
        return False