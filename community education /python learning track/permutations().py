from itertools import permutations
s,k=input().split()
sk=list(permutations(s,int(k)))
sk.sort()
for i in range (len(sk)):
    for j in range (int(k)):
        print(sk[i][j],end="")
    print("")
