from itertools import product
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ab=list(product(a,b))
ab.sort()
for i in ab:
    print(i,end=" ")
