if __name__ == '__main__':
    nasc=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nasc.append([name,score])
    score=[]
    for i in range(0,len(nasc)):
        score.append(nasc[i][1])
    score2=list(set(score))
    score2.sort()
    num=score2[1]
    names=[]
    for i in range(0,len(nasc)):
        if nasc[i][1]==num:
            names.append(nasc[i][0])
    names.sort()
    for i in names:
        print(i)
            
