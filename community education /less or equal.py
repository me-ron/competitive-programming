n,k=map(int,input().split())
l=[1]+sorted(list((map(int,input().split()))))
print(l[k] if k==n or l[k+1]-l[k] else -1)
