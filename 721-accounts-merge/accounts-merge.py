class UnionFind:
    def __init__(self):
        self.parent = {}
    
    def find(self, x):
        if x != self.parent.setdefault(x, x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parents = UnionFind()
        email_to_name = {}
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                parents.union(first_email, email)
                email_to_name[email] = name

        groups = defaultdict(list)
        for email in email_to_name:
            leader = parents.find(email)
            groups[leader].append(email)

        res = []
        for leader, emails in groups.items():
            name = email_to_name[leader]
            res.append([name] + sorted(emails))

        return res
