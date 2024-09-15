class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s_cities = set()
        d_cities = set()

        for start,end in paths:
            s_cities.add(start)
            d_cities.add(end)
        
        for city in d_cities:
            if city not in s_cities:
                return city