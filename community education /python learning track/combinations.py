from itertools import combinations
s,k = list(input().split())
s =sorted([i for i in s])
k = int(k)
for i in range(1, k+1):
    comb = list(combinations(s, i))
    for i in comb:
        print("".join(i))
