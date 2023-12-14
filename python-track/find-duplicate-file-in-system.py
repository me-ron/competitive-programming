class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        paths=[i.split() for i in paths]
        count=defaultdict(list)
        for i in range(len(paths)):
            for j in range(1,len(paths[i])):
                if "(" in paths[i][j]:
                    s=paths[i][j].split("(")
                    count[s[1]].append(f"{paths[i][0]}/{s[0]}")
        print(count)
        return [i for i in count.values() if len(i)>1]