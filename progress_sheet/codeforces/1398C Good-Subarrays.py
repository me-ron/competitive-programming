for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,list(input())))
    ans=0
    c={0:1}
    run=0
    for i in range(n):
        if i!=0:
            lst[i]+=lst[i-1]
        if lst[i]-i-1 in c:
            ans+=c[lst[i]-i-1]  
        c[lst[i]-i-1]=c.get(lst[i]-i-1,0)
        c[lst[i]-i-1]+=1
    print(ans)
