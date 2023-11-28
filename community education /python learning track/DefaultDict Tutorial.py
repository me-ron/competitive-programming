from collections import defaultdict
n, m = map(int, input().split())
A = defaultdict(list)
for i in range(n):
    A[input()].append(i+1)
for i in range(m):
    k = input()
    print(*(A[k] if k in A else [-1]), sep=' ')
