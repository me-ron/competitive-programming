n = int(input())
pos = list(map(int, input().split()))
speed = list(map(int, input().split()))
p_s = sorted(list(zip(pos, speed)))

def can(time):
    north = p_s[0][0] + (time * p_s[0][1])

    for i in range(1, n):
        down, up = p_s[i][0] - (time * p_s[i][1]), p_s[i][0] + (time * p_s[i][1])
        if down <= north:
           north = min(up, north) 
        else:
            return False
    return True

l, r = 0, max(pos)

while r - l > 1e-6:
    mid = (l + r) / 2

    if can(mid):
        r = mid
    else:
        l = mid

print(r)