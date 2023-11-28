n=int(input())
lst=list(map(int,input().split()))
for i in lst:
    if((i+lst[0])%2==1):
        lst.sort()
        break
print(*lst)
