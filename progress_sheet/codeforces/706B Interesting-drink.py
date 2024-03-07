from bisect import bisect_right
n = int(input())
lst = sorted(list(map(int, input().split())))
for _ in range(int(input())):
    print(bisect_right(lst, int(input())))