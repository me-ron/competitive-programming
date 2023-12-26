class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        dic={heights[i]:names[i] for i in range(len(names))}
        heights.sort(reverse=True)
        for i in range(len(heights)):
            names[i]=dic[heights[i]]

        return names
