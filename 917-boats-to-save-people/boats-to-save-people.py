class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) -1
        num_of_boat = 0

        while i <= j:
            if people[i] + people[j] > limit:
                num_of_boat += 1
                j -= 1
            else:
                num_of_boat += 1
                j -= 1
                i += 1
        return num_of_boat