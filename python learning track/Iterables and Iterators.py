from itertools import combinations
n=int(input())
st=list(input().split())
k=int(input())
x=list(combinations(st,k))
ans=0
for i in x:
    if 'a' in i:
        ans+=1
print(ans/len(x))
