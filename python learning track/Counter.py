n=int(input())
shoes= list(input().split())
c=int(input())
money=0
for i in range (c):
    s,p=input().split()
    p=int(p)
    if s in shoes:
        shoes.remove(s)
        money+=p
print(money)
