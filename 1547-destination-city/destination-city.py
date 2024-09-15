class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s_cities = []
        d_cities = []

        for start,end in paths:
            s_cities.append(start)
            d_cities.append(end)
        
        for city in d_cities:
            if city not in s_cities:
                return city