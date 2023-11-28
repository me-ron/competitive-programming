if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    arr2= list(arr)
    arr2.sort()
    print(arr2[-2])
