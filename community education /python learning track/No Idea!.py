n,m=list(map(int,input().split()))
arr=list(map(int,input().split()))
a=list(set(map(int,input().split())))
b=list(set(map(int,input().split())))
happiness=0
for i in range(n):
    if arr[i] in a:
        happiness+=1
    elif arr[i] in b:
        happiness-=1
print(happiness)
