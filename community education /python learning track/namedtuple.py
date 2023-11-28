from collections import namedtuple
n = int(input())
a = namedtuple('A', input().split())
lst=[float(a(*input().split()).MARKS) for _ in range(n)]
print(sum(lst)/n)
