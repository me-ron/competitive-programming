n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    cmd, *num = input().split()
    e = list(map(int, num))
    if cmd == "pop":
        s.pop()
    elif cmd == "discard":
        s.discard(e[0])
    elif cmd == "remove":
        s.remove(e[0])     
print(sum(list(s)))
