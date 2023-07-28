t=int(input())
for i in range (t):
    n=int(input())
    lst=sorted(list(map(int,input().split())))
    if n==1:
        print("YES")
    else:
        j=1
        while j<n:
            if lst[j]-lst[j-1]>1:
                print("NO")
                break
            j+=1
        else:
            print("YES")
