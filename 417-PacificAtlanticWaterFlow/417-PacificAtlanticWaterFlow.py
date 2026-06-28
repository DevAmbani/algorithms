# Last updated: 6/28/2026, 1:12:23 PM
1from collections import defaultdict
2
3class Solution:
4    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
5        acc = defaultdict(list)
6        parent = {}
7        rank = {}
8
9        def find(node):
10            if node == parent[node]:
11                return node
12            elif node != parent[node]:
13                return find(parent[node])
14            
15        def union(x,y):
16            px = find(x)
17            py = find(y)
18
19            if px == py:
20                return False
21            
22            elif rank[px] > rank[py]:
23                parent[py] = px
24            elif rank[py] > rank[px]:
25                parent[px] = py
26            else:
27                parent[py] = px
28                rank[px] += 1
29            return True
30
31        for account in accounts:
32            for email in account[1:]:
33                if email not in parent:
34                    parent[email] = email
35                    rank[email] = 0
36        
37        for account in accounts:
38            anchor = account[1]
39            for email in account[2:]:
40                union(anchor, email)
41        
42        group = defaultdict(list)
43        for account in accounts:
44            for email in account[1:]:
45                root = find(email)
46                group[root].append(email)
47        
48        email_name = {}
49        for account in accounts:
50            name = account[0]
51            for email in account[1:]:
52                email_name[email] = name
53        
54        final = []
55        for root, email in group.items():
56            name = email_name[root]
57            final.append([name] + sorted(set(email)))
58        
59        return final
60