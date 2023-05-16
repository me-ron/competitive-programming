if __name__ == '__main__':
    N = int(input())
    lst=[]
    for i in range(N):
        inst, *num = input().split()
        e=list(map(int,num))
        if inst=="print":
            print(lst)
        if inst=="insert":
            lst.insert(e[0],e[1])
        elif inst=="remove":
            lst.remove(e[0])
        elif inst=="append":
            lst.append(e[0])
        elif inst=="sort":
            lst.sort()
        elif inst=="pop":
            lst.pop()
        elif inst=="reverse":
            lst.reverse()
