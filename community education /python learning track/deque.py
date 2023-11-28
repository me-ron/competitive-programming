from collections import deque
d = deque()
for i in range(int(input())):
    a,*n = input().split()
    exec(f'd.{a}({str(*n)})')
print(*d)
